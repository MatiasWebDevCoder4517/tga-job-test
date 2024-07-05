# Local
from .globals import (
    API_KEY_CHATGPT,
    MYSQL_DATABASE,
    MYSQL_PASSWORD,
    MYSQL_SERVER,
    MYSQL_USER,
    PDF_FILENAME,
    PROJECT_NAME,
)
from .logger import create_logger


LOGGER = create_logger()

__all__ = [
    "LOGGER",
    "PROJECT_NAME",
    "MYSQL_SERVER",
    "MYSQL_USER",
    "MYSQL_PASSWORD",
    "MYSQL_DATABASE",
    "API_KEY_CHATGPT",
    "PDF_FILENAME",
]
