"""
Author: Igor
Date: 2020.06.07
"""

import logging
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

LOG_FORMATTING_STRING = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_file_handler():
    file_name = 'log/error.log.{0}'.format(datetime.utcnow().strftime("%Y%m%d"))
    file_handler = TimedRotatingFileHandler(filename=file_name, when='midnight')
    file_handler.setFormatter(LOG_FORMATTING_STRING)
    file_handler.setLevel(logging.WARN)
    file_handler.suffix = "%Y%m%d"
    return file_handler


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LOG_FORMATTING_STRING)
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    return logger
