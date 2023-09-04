import os
import logging
import json
from enum import Enum


class LogLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    @staticmethod
    def is_present(log_level):
        return log_level.upper() in [level.value for level in LogLevel]


class Log(object):
    def __int__(self, client_id):
        log_level = os.getenv('LOG_LEVEL', 'INFO')

        if not Log.LogLevel.is_present(log_level):
            log_level = LogLevel.INFO.value
            logging.getLogger().setLevel(log_level)

            self.__client_id = client_id

        def info(self, message):
            logging.info(json.dumps({
                'client_id': self.__client_id,
                'message': message
            }))

        def debug(self, message):
            logging.debug(json.dumps({
                'client_id': self.__client_id,
                'message': message
            }))

        def warning(self, message):
            logging.warning(json.dumps({
                'client_id': self.__client_id,
                'message': message
            }))

        def error(self, message):
            logging.error(json.dumps({
                'client_id': self.__client_id,
                'message': message
            }))
