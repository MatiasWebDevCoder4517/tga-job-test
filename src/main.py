# Project
from app.calculations.metrics import (
    get_known_company_answers,
    get_months_days,
    get_recomendations_avg,
    get_sng_general_satisfaction,
    get_sng_recomendation,
    get_total_comentaries,
)
from app.config import LOGGER
from app.db.mysql import mysql_db
from app.db.orm_queries import get_db_data


def main():

    LOGGER.info("Connecting to MySQL database... ")
    mysql_session = next(mysql_db())
    database_data = get_db_data(mysql_session)
    ##LOGGER.info(f"GENERAL_SATISFACTION: {database_data}")

    ## 1.a
    general_satisfaction_sng = get_sng_general_satisfaction(database_data)
    LOGGER.info(f"SNG_SATISFACTION: {general_satisfaction_sng}")

    ## 1.b
    total_company_known = get_known_company_answers(database_data)
    LOGGER.info(f"TOTAL_COMPANY_KNOWN: {total_company_known}")

    ## 1.c
    recomendations_sng = get_sng_recomendation(database_data)
    LOGGER.info(f"SNG_RECOMENDATIONS: {recomendations_sng}")

    ## 1.d
    recomendations_avg = get_recomendations_avg(database_data)
    LOGGER.info(f"RECOMENDATIONS_AVERAGE: {recomendations_avg}")

    ## 1.e
    all_comentaries = get_total_comentaries(database_data)
    LOGGER.info(f"TOTAL_COMENTARIES: {all_comentaries}")

    ## 1.f
    survey_date_length = get_months_days(database_data)
    LOGGER.info(f"SURVEY_LENGTH: {survey_date_length}")

    print("Finish breakpoint")

    return "Execution Finished!"


if __name__ == "__main__":
    main()
