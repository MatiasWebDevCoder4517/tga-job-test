# Standard Library

# Project
from app.calculations.metrics import (
    filename_date,
    get_known_company_answers,
    get_months_days,
    get_recomendations_avg,
    get_sng_general_satisfaction,
    get_sng_recomendation,
    get_total_comentaries,
)
from app.chatgpt.api import feelings_analysis, get_main_issues_conclusion
from app.config import LOGGER
from app.db.mysql import mysql_db
from app.db.orm_queries import get_db_data
from app.files.generate import get_pdf_file


def main():
    LOGGER.info("Connecting to MySQL database... ")
    mysql_session = next(mysql_db())
    database_data = get_db_data(mysql_session)
    ##LOGGER.info(f"GENERAL_SATISFACTION: {database_data}")

    if not database_data:
        LOGGER.critical("Empty data received!")
        return None

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

    ## 2.a
    chatgpt_psychological_analysis = feelings_analysis(database_data)
    LOGGER.info(f"CHATGPT_ANALYSIS: {chatgpt_psychological_analysis}")

    ## 2.b
    biggest_issues = get_main_issues_conclusion(chatgpt_psychological_analysis)
    LOGGER.info(f"BIGGEST_ISSUES: {biggest_issues}")

    ## 3.
    filename = filename_date()
    build_pdf = get_pdf_file(chatgpt_psychological_analysis, biggest_issues, filename)
    LOGGER.info(f"PDF_BUILD: {build_pdf}")

    print("END BREAKPOINT")

    return "Execution Finished!"


if __name__ == "__main__":
    main()
