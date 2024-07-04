# Proyecto Marla - Informe de Encuesta

## Descripción

Este proyecto es una aplicación web desarrollada con Flask que permite a la empresa MK analizar los resultados de una encuesta realizada a los clientes del proyecto inmobiliario Marla. La aplicación calcula varias métricas clave y genera un informe en PDF basado en los datos de la encuesta almacenados en una base de datos MySQL (KPIs).

## Estructura del Proyecto

TGA/

- src/
  - main.py
  - requirements.txt
  - app/
    - config/
      - config.py
      - logger.py
    - db/
      - mysql.py
      - orm_queries.py
    - models/
      - survey.py
    - testing/
        - survey_test.py

## Créditos

Este proyecto fue desarrollado como parte de un desafío técnico para analizar y reportar los resultados de una encuesta para la empresa MK.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
