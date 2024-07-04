# Standard Library
from os import getenv


PROJECT_NAME = "TGA"
MYSQL_USER = getenv("MYSQL_USER", "")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD", "")
MYSQL_SERVER = getenv("MYSQL_SERVER", "")
MYSQL_DATABASE = getenv("MYSQL_DATABASE", "")
