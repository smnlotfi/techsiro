# logging_utils.py
import logging

logger = logging.getLogger(__name__)


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)


def handle_error(logger, message, exception=None):
    """
    Custom error handling function to log errors.
    """
    logger.error(f"{message}: {exception}" if exception else message)
