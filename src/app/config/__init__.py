# Local
from .globals import MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_USER, PROJECT_NAME
from .logger import create_logger


LOGGER = create_logger()

__all__ = [
    "LOGGER",
    "PROJECT_NAME",
    "MYSQL_SERVER",
    "MYSQL_USER",
    "MYSQL_PASSWORD",
    "MYSQL_DATABASE",
]
