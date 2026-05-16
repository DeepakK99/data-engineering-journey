# day 6 notes (problems with current architecture)

## Problems
- in memory processing
- no retry for s3
- no proper supervisor (orchestrator)
- schema rigid
- duplicate file processing
- parallel executions: cpu contention, memory pressure, s3 throttling, db exhaustion, logging chaos

## Future Improvements
- Replace in-memory processing with chunked processing
- Use PostgreSQL COPY for bulk inserts
- Add retry logic for S3 uploads
- Add orchestration with Airflow
- Move toward parquet-based storage
- Introduce Spark for distributed workloads