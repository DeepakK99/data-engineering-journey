import os
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "pipeline.log"

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

AWS_CONFIG = {
    "bucket": os.getenv("AWS_BUCKET")
}

INPUT_FILE = os.getenv("INPUT_FILE")