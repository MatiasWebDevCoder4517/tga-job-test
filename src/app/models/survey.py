# External
from sqlalchemy import TEXT, VARCHAR, BigInteger, Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Encuesta(Base):
    __tablename__ = "encuesta"
    secuencial = Column(BigInteger, primary_key=True)

    email = Column(VARCHAR(255), nullable=True)
    fecha = Column(VARCHAR(255), nullable=True)
    satisfeccion_general = Column(Integer, nullable=True)
    conocia_empresa = Column(VARCHAR(255), nullable=True)
    recomendacion = Column(Integer, nullable=True)
    recomendacion_abierta = Column(TEXT, nullable=True)
