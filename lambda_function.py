import json
import os
import logging
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def lambda_handler(event, context):
    logger.info("Lambda Python for the win!")
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    path = record['s3']['object']['key']
    size = get_size(bucket, path)
    return {
        'statusCode': 200,
        'idClient': os.environ['ID_CLIENT'],
        'size': size,
        'body': json.dumps(event)
    }

def get_size(bucket, path):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    total_size = 0

    for obj in my_bucket.objects.filter(Prefix=path):
        total_size = total_size + obj.size

    return total_size