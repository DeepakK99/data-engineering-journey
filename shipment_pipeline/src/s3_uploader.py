import boto3
from utils.logger import logger

s3 = boto3.client("s3")

def upload_file_to_s3(localfile, bucket, s3_key):
    try:
        logger.info(f"uploading {localfile} to {s3_key}")
        s3.upload_file(
            localfile,
            bucket,
            s3_key
        )

        logger.info(f"uploaded {localfile} to {s3_key}")
    except Exception as e:
        logger.error(f"S3 upload failed: {e}")