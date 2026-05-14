# day 4 notes (python + postgres[psycopg2])

## concepts
- batch processing/loading
- proper logging

## Better Production Approach
- idempotency (primary key for db level constraint)
- handle on conflicts
- batch processing (e.g. 100 rows E-T-L) [currenly processed_records]
- execute_batch()
