# Day 5 — AWS + S3 Fundamentals (Cloud Data Engineering)

## What I Learned Today

Today I moved from local data engineering to **cloud-based data engineering** using AWS.

The main shift was understanding:

> From local files → to distributed object storage (S3)

---

# Core Concepts

## 1. Cloud Thinking

- Local systems store files on disk
- Cloud systems store data in distributed object storage
- Cloud provides scalability, durability, and global access

---

## 2. AWS CLI Basics

AWS CLI allows interaction with AWS services from the terminal.

### Commands used:

Check CLI installation:
```bash
aws --version
```

Configure AWS credentials:
```bash
aws configure
```

List S3 buckets:
```bash
aws s3 ls
```

Create S3 bucket:
```bash
aws s3api create-bucket --bucket bucket-name --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
```

List contents of a bucket:
```bash
aws s3 ls s3://bucket-name/
```

Upload file to S3:
```bash
aws s3 cp file.csv s3://bucket-name/path/
```

Download file from S3:
```bash
aws s3 cp s3://bucket-name/file.csv .
```

List all objects recursively:
```bash
aws s3 ls s3://bucket-name/ --recursive
```

## S3
- S3 is object storage, not a filesystem
- Data is stored as:
    - bucket + object key
- “Folders” are only logical prefixes

## Partitioning Concept
- ideal way : year=2026/month=05/day=15/

## Python sdk
- pip install boto3
- sdk usage
    ```python
        import boto3

        s3 = boto3.client("s3")

        s3.upload_file(
            "local_file.csv",
            "bucket-name",
            "raw/shipments/year=2026/month=05/file.csv"
        )
        ```