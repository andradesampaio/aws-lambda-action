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
    key = record['s3']['object']['key']
    return {
        'statusCode': 200,
        'idClient': os.environ['ID_CLIENT'],
        'size': check_size(bucket, key),
        'body': json.dumps(event)
    }


def check_size(bucket, key):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    mega_byte = 1024 * 1024;
    obj = my_bucket.objects.filter(Prefix=key)

    if obj.size > 1 * mega_byte:
        logger.info("Objeto muito grande")
    else:
        logger.info("Objeto dentro do tamanho")
