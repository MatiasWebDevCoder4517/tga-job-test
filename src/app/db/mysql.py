# Standard Library
from typing import Generator

# External
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

# Project
from app.config import LOGGER, MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_USER


db_connection = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DATABASE}"
db_engine = create_engine(db_connection, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def mysql_db() -> Generator[Session, None, None]:
    db_session = SessionLocal()
    try:
        yield db_session
    except SQLAlchemyError as e:
        db_session.rollback()
        LOGGER.error(f"Database session error: -> {db_session}")
        LOGGER.debug(e)
    finally:
        db_session.close()
