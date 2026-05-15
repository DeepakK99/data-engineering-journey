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
            password="<REDACTED>",
            port="5432"
        )
        logging.info("Database Connection Successful")
        yield conn
    
    except Exception as e:

        logging.error(f"Database connection failed: {e}")
        conn = None
        yield conn

    finally:
        if conn:
            conn.close()