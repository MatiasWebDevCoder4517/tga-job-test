# metrics_test.py
# Standard Library

# External

# Project
from app.calculations.metrics import (
    get_known_company_answers,
    get_months_days,
    get_recomendations_avg,
    get_sng_general_satisfaction,
    get_sng_recomendation,
    get_total_comentaries,
)


def test_get_sng_general_satisfaction():
    db_data = [
        {"satisfeccion_general": 7},
        {"satisfeccion_general": 6},
        {"satisfeccion_general": 4},
        {"satisfeccion_general": 1},
        {"satisfeccion_general": 5},
        {"satisfeccion_general": "invalid"},
    ]
    result = get_sng_general_satisfaction(db_data)
    assert result == 0


def test_get_known_company_answers():
    db_data = [
        {"conocia_empresa": "Sí"},
        {"conocia_empresa": "No"},
        {"conocia_empresa": "Sí"},
        {"conocia_empresa": 1},
        {"conocia_empresa": "Sí"},
    ]
    result = get_known_company_answers(db_data)
    assert result == 3


def test_get_sng_recomendation():
    db_data = [
        {"recomendacion": 7},
        {"recomendacion": 6},
        {"recomendacion": 4},
        {"recomendacion": 1},
        {"recomendacion": 5},
        {"recomendacion": "invalid"},
    ]
    result = get_sng_recomendation(db_data)
    assert result == 0


def test_get_recomendations_avg():
    db_data = [
        {"recomendacion": 7},
        {"recomendacion": 6},
        {"recomendacion": 4},
        {"recomendacion": 1},
        {"recomendacion": 5},
        {"recomendacion": "invalid"},
    ]
    result = get_recomendations_avg(db_data)
    assert result == 4.6


def test_get_total_comentaries():
    db_data = [
        {"recomendacion_abierta": "Comment 1"},
        {"recomendacion_abierta": "Comment 2"},
        {"recomendacion_abierta": None},
        {"recomendacion_abierta": ""},
        {"recomendacion_abierta": 123},
    ]
    result = get_total_comentaries(db_data)
    assert result == 2


def test_get_months_days():
    data = [
        {"fecha": "2023-01-01 00:00:00"},
        {"fecha": "2023-06-01 00:00:00"},
        {"fecha": "2023-12-01 00:00:00"},
    ]
    result = get_months_days(data)
    assert result == {"duration_days": 334, "duration_months": 11}
