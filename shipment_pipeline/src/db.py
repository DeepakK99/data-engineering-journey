import logging
import psycopg2
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="shipment_db",
            user="postgres",
            password="postgres",
            port="5432"
        )
        logging.info("Database Connection Successful")
        yield conn
    
    except Exception as e:

        logging.error(f"Database connection failed: {e}")

        return None

    finally:
        if conn:
            conn.close()