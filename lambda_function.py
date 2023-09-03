import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def lambda_handler(event, context):
    print('## ENVIRONMENT VARIABLES')
    print(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    print(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
    print('## EVENT')
    print(event)
    logger.info("Lambda Python for the win!")
    return {
        'statusCode': 200,
        'idClient': os.environ['ID_CLIENT'],
        'body': json.dumps(event)
    }
