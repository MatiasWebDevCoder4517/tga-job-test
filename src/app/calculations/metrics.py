# Standard Library
from datetime import datetime

# Project
from app.config import LOGGER, PDF_FILENAME


YES_ANSWER = "Sí"


## Objective 1.a
def get_sng_general_satisfaction(db_data: list[dict]) -> int:
    total_satisfaction = 0
    total_dissatisfaction = 0
    total_neutrals = 0
    total_answers = len(db_data)

    if not total_answers or total_answers == 0:
        LOGGER.error("No valid data found!")
        return 0

    for item in db_data:
        satisfaction_value = item.get("satisfeccion_general")

        if isinstance(satisfaction_value, int):
            if 6 <= satisfaction_value <= 7:
                total_satisfaction += 1
            elif 1 <= satisfaction_value <= 4:
                total_dissatisfaction += 1
            elif satisfaction_value == 5:
                total_neutrals += 1
        else:
            LOGGER.info("Invalid satisfeccion_general!")
            continue
    return round(total_satisfaction * 100 / total_answers) - round(
        total_dissatisfaction * 100 / total_answers
    )


## Objective 1.b
def get_known_company_answers(db_data: list[dict]) -> int:
    total_known = 0
    total_unknown = 0

    for item in db_data:
        known_value = item.get("conocia_empresa", "")

        if isinstance(known_value, str):
            if known_value == YES_ANSWER:
                total_known += 1
            else:
                total_unknown += 1
        else:
            LOGGER.info("Invalid conocia_empresa!")
            continue
    return total_known


## Objective 1.c
def get_sng_recomendation(db_data: list[dict]) -> int:
    total_satisfaction = 0
    total_dissatisfaction = 0
    total_neutrals = 0
    total_answers = len(db_data)

    if not total_answers or total_answers == 0:
        LOGGER.error("No valid data found!")
        return 0

    for item in db_data:
        recomendation_value = item.get("recomendacion")

        if isinstance(recomendation_value, int):
            if 6 <= recomendation_value <= 7:
                total_satisfaction += 1
            elif 1 <= recomendation_value <= 4:
                total_dissatisfaction += 1
            elif recomendation_value == 5:
                total_neutrals += 1
        else:
            LOGGER.info("Invalid recomendacion!")
            continue
    return round(total_satisfaction * 100 / total_answers) - round(
        total_dissatisfaction * 100 / total_answers
    )


## Objective 1.d
def get_recomendations_avg(db_data: list[dict]) -> float:
    accumulator = 0
    total_answers = len(db_data)

    if not total_answers or total_answers == 0:
        LOGGER.error("No valid data found!")
        return 0.0

    for item in db_data:
        recomendation_value = item.get("recomendacion")

        if not isinstance(recomendation_value, int):
            LOGGER.info("Invalid recomendacion!")
            continue
        accumulator += recomendation_value
    return float(f"{(accumulator / total_answers):.2f}")


## Objective 1.e
def get_total_comentaries(db_data: list[dict]) -> int:
    total_comentaries = 0
    total_nones = 0
    for item in db_data:
        comentary_value = item.get("recomendacion_abierta", "")

        if not isinstance(comentary_value, str):
            total_nones += 1
            continue

        total_comentaries += 1
    return total_comentaries


## Objective 1.f
def get_months_days(db_data: list[dict]):
    dates = [datetime.strptime(item["fecha"], "%Y-%m-%d %H:%M:%S") for item in db_data]
    min_date = min(dates)
    max_date = max(dates)
    duration_days = max_date - min_date
    duration_months = max_date.month - min_date.month
    return {
        "duration_days": duration_days.days,
        "duration_months": duration_months,
    }


## Objective 3.
def filename_date():
    today = datetime.now()
    date_str = today.strftime("%d-%m-%Y")
    name, ext = PDF_FILENAME.rsplit(".", 1)
    return f"{name}_{date_str}.{ext}"
