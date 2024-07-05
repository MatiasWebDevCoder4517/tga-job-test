# External
from sqlalchemy import select
from sqlalchemy.orm import Session

# Project
from app.models.survey import Encuesta


def get_db_data(db_session: Session) -> list[dict]:
    orm_query = select(
        Encuesta.email,
        Encuesta.fecha,
        Encuesta.satisfeccion_general,
        Encuesta.conocia_empresa,
        Encuesta.recomendacion,
        Encuesta.recomendacion_abierta,
    )
    data = db_session.execute(orm_query).mappings()
    data_result = []
    for data_item in data:
        data_result.append(
            {
                "email": data_item["email"],
                "fecha": data_item["fecha"],
                "satisfeccion_general": data_item["satisfeccion_general"],
                "conocia_empresa": data_item["conocia_empresa"],
                "recomendacion": data_item["recomendacion"],
                "recomendacion_abierta": data_item["recomendacion_abierta"],
            }
        )
    return data_result
