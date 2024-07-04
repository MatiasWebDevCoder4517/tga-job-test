# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-07-04

### Added

- Montando bases estructurales y arquitectura del micro-servicio worker.

## [0.2.0] - 2024-07-04

### Added

- Modulo .env para variables globales privadas.
- Nueva implementacion de 'containerization' con Dockerfile, docker-compose y .dockerignore.
- Nueva implementacion de 'requirements.txt' con respectivas dependencias, se ocupa poetry para un mejor control de versionamiento.
- Nueva implementacion de logger y flujo de ordenamiento-codigo con libreria pre-commit.
- Nueva implementacion de variables globales y de entorno en modulo 'config/globals.py'.
- Nueva implementacion de estructura y logica para conexiones MySQL en modulo 'db/mysql.py', junto con ORM SQLAlchemy en modulo 'db/orm_queries.py' y mecanismo de captura de datos esenciales.
- Nuevo modelo 'survey.py' SQLAlchemy para encuesta y nuevo paquete 'models'.
- Nuevo modelo 'survey_test.py' pytest en paquete 'testing'.


## [0.3.0] - 2024-07-04

### Added

- Implementacion de modulo 'metrics' en paquete 'calculations' y construccion funcional de objectivos especificos
