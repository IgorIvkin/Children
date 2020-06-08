"""
Author: Igor
Date: 2020.06.07
"""

import logging
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

LOG_FORMATTING_STRING = logging.Formatter('%(asctime)s - %(module)s - %(filename)s - '
                                          '%(lineno)d  - %(levelname)s - %(message)s')


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
    """Returns a named logger that includes console logger that prints everything
    starting from 'debug' level and file logger that prints only the sensible errors starting
    from 'warning' level.

    How to use:
    (behind the scene application has a global variable log that
    points to this logger)

    from children import log

    log.warn('Test warn')
    log.debug('Test debug')
    log.error('Test error')

    You can put these output errors in any place of your code. It is recommended to avoid
    using it for the errors that are easily recoverable, for example not enough params in
    user input.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    return logger
