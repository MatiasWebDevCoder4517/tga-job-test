#### DOCUMENTACION

## Descripción

- Este micro-servicio worker está diseñado para capturar datos desde una DB MySQL, para luego calcular ciertas metricas y finalmente generar un informe pdf de KPIs simples.

## Requisitos Previos e Instalacion:

# Requisitos Previos

- Python 3.12
- requirements.txt
- environment variables (.env)
- Cliente MySQL
- OpenAI API KEY

# Instalacion Inicial

- Clona este repositorio en tu máquina local.
- Navega al directorio del proyecto.
- Crea y activa un entorno virtual:
   python -m venv venv       # En Linux distro: venv/bin/activate
   source venv/bin/activate  # En Windows: venv\Scripts\activate
- Asegurarse de que todas las dependencias estén instaladas y configuradas correctamente -> requirements.txt

Alternativamente:

- Utilizar e instalar correctamente Docker con la imagen configurada en el Dockerfile.

## Características

- Microservicio tipo Worker.

## Instrucciones

- Ejecucion simple a travez de python main.py o Ejecucion simple a travez de Dockerfile.

-> Dockerfile:
sudo docker-compose -f <name_docker_compose.yml> up -d
