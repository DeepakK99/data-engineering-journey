from reader import read_shipments
from cleaner import clean_record
from validator import validate_record
from transformer import transform_record
from writer import write_shipments
from loader import insert_batch
from db import get_db_connection
from s3_uploader import upload_file_to_s3
from queries import *

import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "pipeline.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Pipeline Started")
    processed_records = []
    seen_ids = set()

    for record in read_shipments(BASE_DIR / "data/raw/shipments.csv"):

        cleaned = clean_record(record)

        shipment_id = record.get("shipment_id")

        if shipment_id in seen_ids:
            logging.warning(f"Duplicate record skipped: {shipment_id}")
            continue

        seen_ids.add(shipment_id)

        if not validate_record(cleaned):
            logging.warning(f"Rejected record: {cleaned}")
            continue

        transformed = transform_record(cleaned)

        processed_records.append(transformed)

    # output_path = BASE_DIR / "data/processed/processed_shipments.csv"
    # write_shipments(output_path, processed_records)

    with get_db_connection() as conn:
        insert_batch(conn, processed_records)

    logging.info(f"Pipeline completed. Records written: {len(processed_records)}")

    logging.info("Showing Top Analytics Now:")

    with get_db_connection() as conn:

        delayed_shipments = get_delayed_shipments(conn)
        logging.info(f"delayed_shipments: {delayed_shipments}")

        average_delivery_time = get_average_delivery_time(conn)
        logging.info(f"average_delivery_time: {average_delivery_time}")

        revenue_by_route = get_revenue_by_route(conn)
        logging.info(f"revenue_by_route: {revenue_by_route}")

        top_customers = get_top_customers(conn)
        logging.info(f"top_customers: {top_customers}")

    logging.info("End of Analytics")

    upload_file_to_s3(BASE_DIR / "data/processed/processed_shipments.csv", 
                      "<REDACTED>", 
                      "processed/shipments/year=2026/month=05/day=15/processed_shipments.csv")

if __name__ == "__main__":
    run_pipeline()
