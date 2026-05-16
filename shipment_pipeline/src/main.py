from config.config import AWS_CONFIG, INPUT_FILE, BASE_DIR

from reader import read_shipments
from cleaner import clean_record
from validator import validate_record
from transformer import transform_record
from writer import write_shipments
from loader import insert_batch
from db import get_db_connection
from s3_uploader import upload_file_to_s3
from queries import *

from utils.logger import logger
import time
from datetime import datetime


def run_pipeline():
    pipeline_start = time.time()
    logger.info("Pipeline Started")
    processed_records = []
    seen_ids = set()
    total_records = 0
    duplicate_records = 0
    invalid_records = 0

    data_processing_start = time.time()
    for record in read_shipments(BASE_DIR / INPUT_FILE):
        try:
            total_records += 1

            cleaned = clean_record(record)

            shipment_id = record.get("shipment_id")

            if shipment_id in seen_ids:
                duplicate_records += 1
                logger.warning(f"Duplicate record skipped: {shipment_id}")
                continue

            seen_ids.add(shipment_id)

            if not validate_record(cleaned):
                invalid_records += 1
                logger.warning(f"Rejected record: {cleaned}")
                continue

            transformed = transform_record(cleaned)

            processed_records.append(transformed)
        except Exception as e:
            invalid_records += 1
            logger.warning(f"Error while processing a record: {record}\nErr:{str(e)}")

    data_processing_end = time.time()
    logger.info(
        f"Data processed(clean, validate, transform) in {(data_processing_end-data_processing_start):.2f} seconds"
    )

    logger.info(f"Total records read: {total_records}")
    logger.warning(f"Total duplicate records found: {duplicate_records}")
    logger.warning(f"Total invalid records found: {invalid_records}")
    logger.info(f"Total valid output records: {len(processed_records)}")

    output_path = BASE_DIR / "data/processed/processed_shipments.csv"
    file_write_start = time.time()
    write_shipments(output_path, processed_records)
    file_write_end = time.time()
    logger.info(
        f"Written to local file (data/processed/processed_shipments.csv) in {(file_write_end-file_write_start):.2f} seconds"
    )

    postgres_insert_start = time.time()
    with get_db_connection() as conn:
        insert_batch(conn, processed_records)
    postgres_insert_end = time.time()
    logger.info(
        f"Written to Postgres db in {(postgres_insert_end-postgres_insert_start):.2f} seconds"
    )

    logger.info("Showing Top Analytics Now:")

    analytics_start = time.time()

    with get_db_connection() as conn:

        delayed_shipments = get_delayed_shipments(conn)
        logger.info(f"delayed_shipments: {delayed_shipments}")

        average_delivery_time = get_average_delivery_time(conn)
        logger.info(f"average_delivery_time: {average_delivery_time}")

        revenue_by_route = get_revenue_by_route(conn)
        logger.info(f"revenue_by_route: {revenue_by_route}")

        top_customers = get_top_customers(conn)
        logger.info(f"top_customers: {top_customers}")

    analytics_end = time.time()
    logger.info("End of Analytics")
    logger.info(f"analytics executed in {(analytics_end-analytics_start):.2f} seconds")

    today = datetime.now()

    s3_key = (
        f"processed/shipments/"
        f"year={today.year}/"
        f"month={today.month:02d}/"
        f"day={today.day:02d}/"
        f"processed_shipments.csv"
    )
    s3_upload_start = time.time()
    upload_file_to_s3(
        BASE_DIR / "data/processed/processed_shipments.csv",
        AWS_CONFIG["bucket"],
        s3_key,
    )
    s3_upload_end = time.time()
    logger.info(f"Uploaded to s3 in {(s3_upload_end-s3_upload_start):.2f} seconds")

    pipeline_end = time.time()

    logger.info(f"Pipeline completed in {(pipeline_end-pipeline_start):.2f} seconds")


if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        logger.exception(f"Pipeline failed. Error: {str(e)}")
