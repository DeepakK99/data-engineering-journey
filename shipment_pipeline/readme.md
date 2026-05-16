# Shipment ETL Pipeline

## Overview

This project is a modular ETL pipeline built using Python.

The pipeline:
- reads shipment data from CSV
- cleans and validates records
- transforms shipment metrics
- loads data into PostgreSQL
- uploads processed files to AWS S3
- runs analytical SQL queries

The project focuses on building production-style data engineering practices including:
- config-driven design
- structured logging
- exception handling
- scalability analysis
- modular architecture

## Architecture Flow
```plaintext
CSV File
   ↓
Reader
   ↓
Cleaner
   ↓
Validator
   ↓
Transformer
   ↓
PostgreSQL + Processed CSV
   ↓
AWS S3 Upload
   ↓
Analytics Queries
```

## Project Structure
```plaintext
project/
│
├── config/
├── data/
├── notes/
├── utils/
├── db.py 
├── reader.py
├── cleaner.py
├── validator.py
├── transformer.py
├── loader.py
├── writer.py
├── s3_uploader.py
├── main.py
└── README.md
```

## Features
- Modular ETL pipeline
- Config-driven setup
- Environment variable management
- Structured logging
- Duplicate handling
- Invalid record filtering
- PostgreSQL integration
- AWS S3 upload
- SQL analytics
- Timing metrics
- Scalability reflection

## Tech Stack
- Python
- PostgreSQL
- AWS S3
- Pandas
- psycopg2
- boto3
- python-dotenv

## Setup

### Clone Repository

```bash
git clone <repo-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
...
```

### Run Pipeline

```bash
python main.py
```

## Example Logs
```plaintext2026-05-16 10:22:01 INFO Pipeline Started
2026-05-16 10:22:02 INFO Total records read: 5000
2026-05-16 10:22:03 WARNING Duplicate records found: 32
2026-05-16 10:22:04 INFO Inserted 4968 rows into PostgreSQL
2026-05-16 10:22:05 INFO Uploaded file to S3
```

## Scalability Considerations

Current limitations identified:
- in-memory processing
- large batch insert bottlenecks
- lack of orchestration
- retry handling improvements needed

## Future Improvements

- Add Airflow scheduling
- Add Docker support
- Introduce Spark transformations
- Add retry mechanisms
- Add data quality monitoring
- Add unit tests