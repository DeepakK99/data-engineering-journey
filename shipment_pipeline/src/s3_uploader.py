import boto3
import logging

s3 = boto3.client("s3")

def upload_file_to_s3(localfile, bucket, s3_key):
    try:
        logging.info(f"uploading {localfile} to {s3_key}")
        s3.upload_file(
            localfile,
            bucket,
            s3_key
        )

        logging.info(f"uploaded {localfile} to {s3_key}")
    except Exception as e:
        logging.error(f"S3 upload failed: {e}")