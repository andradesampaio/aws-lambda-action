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
    check_size(bucket, key)
    return {
        'statusCode': 200,
        'idClient': os.environ['ID_CLIENT'],
        'body': json.dumps(event)
    }


def check_size(bucket, key):
    s3 = boto3.resource('s3')
    objeto_s3 = s3.head_object(bucket, key)
    mega_byte = 1024 * 1024
    tamanho_arquivo_bytes = objeto_s3['ContentLength']

    if tamanho_arquivo_bytes > 1 * mega_byte:
        logger.info("Objeto muito grande")
    else:
        logger.info("Objeto dentro do tamanho")
