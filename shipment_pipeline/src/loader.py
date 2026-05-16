from utils.logger import logger
from psycopg2.extras import execute_batch

def insert_batch(conn, records):
    if not conn:
        return
    
    try:

        cursor = conn.cursor()

        query = """
        INSERT INTO shipment_analytics (
            shipment_id,
            customer_name,
            origin,
            destination,
            shipment_date,
            delivery_date,
            status,
            cost,
            delivery_days,
            delayed_flag
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (shipment_id) DO NOTHING
        """

        values = [
            (
                r["shipment_id"],
                r["customer_name"],
                r["origin"],
                r["destination"],
                r["shipment_date"],
                r["delivery_date"],
                r["status"],
                r["cost"],
                r["delivery_days"],
                r["delayed_flag"]
            )
            for r in records
        ]

        execute_batch(cursor, query, values)

        conn.commit()

    except Exception as e:

        conn.rollback()

        logger.error(f"Batch insert failed: {e}")

def insert_record(conn, record):

    try:

        cursor = conn.cursor()

        query = """
        INSERT INTO shipment_analytics (
            shipment_id,
            customer_name,
            origin,
            destination,
            shipment_date,
            delivery_date,
            status,
            cost,
            delivery_days,
            delayed_flag
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (shipment_id) DO NOTHING.   -- idempotency
        """

        values = (
            record["shipment_id"],
            record["customer_name"],
            record["origin"],
            record["destination"],
            record["shipment_date"],
            record["delivery_date"],
            record["status"],
            record["cost"],
            record["delivery_days"],
            record["delayed_flag"]
        )

        cursor.execute(query, values)

        conn.commit()

    except Exception as e:

        conn.rollback()

        logger.error(f"Insertion failed: {e}")
