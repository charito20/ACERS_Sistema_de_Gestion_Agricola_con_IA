# Evaluación FAIR: Paquete de datos ACERS

**Herramienta:** F-UJI (https://www.f-uji.net/), metric v0.8
**Evaluador:** Equipo ACERS
**Fecha de ejecución:** 2026-09-04, sobre el DOI del depósito en Zenodo. Puntaje agregado obtenido: 92.3 % (objetivo institucional: al menos 60 %).

## Identificadores persistentes

| Elemento | Identificador | Estado |
|---|---|---|
| Repositorio GitHub | https://github.com/charito20/ACERS_Sistema_de_Gestion_Agricola_con_IA | Activo |
| DOI Zenodo | 10.5281/zenodo.22307881 | Publicado |
| OSF | https://osf.io/7cvhy | Activo, público |
| SWHID | `swh:1:snp:465aaeba1b5d8a07e1c7bca122fc8277812e825a` | Archivado (2026-09-04) |

## Principios FAIR

### F1: Se asigna un identificador global persistente y único

- **Repositorio:** DOI de Zenodo `10.5281/zenodo.22307881`.
- **Datos:** DOI de Zenodo bajo CC BY 4.0.
- **OSF:** https://osf.io/7cvhy (registrado 2026-08-02).

### F2: Se describe el recurso con metadatos enriquecidos

- `CITATION.cff`: metadatos CFF 1.2.0 con autores, ORCID, licencia.
- `07_Datos/README_datos.md`: descripción del paquete de datos.
- `07_Datos/diccionario_datos.csv`: diccionario de datos.

### F3: Los metadatos incluyen el identificador del recurso

- `CITATION.cff` enlaza el repositorio GitHub y el DOI de Zenodo.
- El DOI de Zenodo está incorporado a `CITATION.cff` y al README.

### F4: El recurso se registra o busca en un repositorio de acceso abierto

- **Zenodo:** indexa y hace buscable el paquete de datos.
- **Software Heritage:** archiva el código y lo hace buscable por SWHID.

### R1.1: Los metadatos están bajo una licencia de acceso abierto

- Licencia del repositorio: MIT (código) + CC BY 4.0 (datos).
- `07_Datos/LICENSE-DATA.txt`: CC BY 4.0.

### R1.2: Los metadatos incluyen detalles de creación

- Autores con ORCID en `CITATION.cff`.
- Fecha de liberación: 2026-08-30.

### R1.3: Los metadatos incluyen referencias a otros metadatos

- Referencias cruzadas a ERS, matriz de trazabilidad, transcripciones.

### A1.1: El recurso se puede recuperar por su identificador

- GitHub: accesible vía HTTPS.
- Zenodo: accesible vía DOI `10.5281/zenodo.22307881`.

### A1.2: El protocolo está claro y abierto

- OSF: preregistro público con protocolo completo.

### I1.1: Los metadatos usan un vocabulario de acceso abierto

- Términos Dublin Core vía CFF.

### I1.2: Los metadatos usan un vocabulario conforme a FAIR

- CFF 1.2.0 es un estándar reconocido.

### I2.1: Los metadatos están representados en un formato de acceso abierto

- CFF: YAML (acceso abierto).
- CSV: formato tabular abierto.

### L1.1: El contenido se publica con una licencia de acceso abierto

- MIT para código.
- CC BY 4.0 para datos.

## Resultado de la verificación automática

| Métrica F-UJI | Puntaje | Nivel | Fecha de ejecución |
|---|---|---|---|
| Localizable (F) | 7 de 7 | avanzado | 2026-09-04 |
| Accesible (A) | 7 de 7 | avanzado | 2026-09-04 |
| Interoperable (I) | 4 de 6 | moderado | 2026-09-04 |
| Reutilizable (R) | 6 de 6 | moderado | 2026-09-04 |
| Agregado | 24 de 26 (92.3 %) | avanzado | 2026-09-04 |

Evaluación ejecutada sobre `10.5281/zenodo.22307881` con F-UJI versión 4.0.0, especificación de métrica v0.8 (https://doi.org/10.5281/zenodo.15045911). El puntaje agregado supera el objetivo institucional de 60 %. Este documento corresponde al `fair_assessment.pdf` de la raíz del repositorio, exigido por la guía de la Entrega 4.
