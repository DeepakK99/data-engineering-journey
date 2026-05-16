from utils.logger import logger
import psycopg2
from contextlib import contextmanager
from config.config import DB_CONFIG

@contextmanager
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            database=DB_CONFIG["DB_CONFIG"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"],
        )
        logger.info("Database Connection Successful")
        yield conn
    
    except Exception as e:

        logger.error(f"Database connection failed: {e}")
        conn = None
        raise

    finally:
        if conn:
            conn.close()