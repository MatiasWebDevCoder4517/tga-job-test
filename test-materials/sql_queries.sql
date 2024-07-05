-- SELECT * FROM encuesta;

-- Objetivo 1.a

SELECT (
        ROUND(
            SUM(
                CASE
                    WHEN satisfeccion_general IN (6, 7) THEN 1
                    ELSE 0
                END
            ) * 100.0 / COUNT(*)
        ) - ROUND(
            SUM(
                CASE
                    WHEN satisfeccion_general IN (1, 2, 3, 4) THEN 1
                    ELSE 0
                END
            ) * 100.0 / COUNT(*)
        )
    ) AS SNG_GENERAL_SATISFACTION
FROM encuesta;

-- Objectivo 1.b
SELECT COUNT(conocia_empresa) as total_conocia_empresa
FROM encuesta
WHERE
    conocia_empresa = "Si";

-- Objetivo 1.c

SELECT (
        ROUND(
            SUM(
                CASE
                    WHEN recomendacion IN (6, 7) THEN 1
                    ELSE 0
                END
            ) * 100.0 / COUNT(*)
        ) - ROUND(
            SUM(
                CASE
                    WHEN recomendacion IN (1, 2, 3, 4) THEN 1
                    ELSE 0
                END
            ) * 100.0 / COUNT(*)
        )
    ) AS SNG_RECOMENDATION
FROM encuesta;

-- Objetivo 1.d
SELECT SUM(recomendacion) / COUNT(*) AS RECOMENDATION_AVG
FROM encuesta;

-- Objetivo 1.e

SELECT COUNT(recomendacion_abierta) AS total_comentaries
FROM encuesta
WHERE
    recomendacion_abierta IS NOT NULL;

-- Objetivo 1.f

SELECT
    MIN(fecha) AS min_date,
    MAX(fecha) AS max_date,
    DATEDIFF(MAX(fecha), MIN(fecha)) AS duration_days
FROM encuesta;
