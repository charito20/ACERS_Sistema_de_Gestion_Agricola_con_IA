# Evaluación FAIR: Paquete de datos ACERS

**Herramienta:** F-UJI (https://www.fairdatainitiative.org/f-uji-test/)
**Evaluador:** Equipo ACERS
**Ejecución:** con la URL del depósito Zenodo, como paso de comprobación final antes del corte. Objetivo institucional: puntaje agregado de al menos 60 %.

## Identificadores persistentes

| Elemento | Identificador | Estado |
|---|---|---|
| Repositorio GitHub | https://github.com/charito20/ACERS_Sistema_de_Gestion_Agricola_con_IA | Activo |
| DOI Zenodo | Se asigna al publicar el depósito | Por depositar |
| OSF | https://osf.io/7cvhy | Activo, público |
| SWHID | Se obtiene con "Save code now" tras el commit de cierre | Por archivar |

## Principios FAIR

### F1: Se asigna un identificador global persistente y único

- **Repositorio:** DOI de Zenodo, asignado al depositar.
- **Datos:** DOI de Zenodo bajo CC BY 4.0.
- **OSF:** https://osf.io/7cvhy (registrado 2026-08-02).

### F2: Se describe el recurso con metadatos enriquecidos

- `CITATION.cff`: metadatos CFF 1.2.0 con autores, ORCID, licencia.
- `07_Datos/README_datos.md`: descripción del paquete de datos.
- `07_Datos/diccionario_datos.csv`: diccionario de datos.

### F3: Los metadatos incluyen el identificador del recurso

- `CITATION.cff` enlaza el repositorio GitHub.
- El DOI de Zenodo se incorpora a `CITATION.cff` y al README en cuanto se asigna.

### F4: El recurso se registra o busca en un repositorio de acceso abierto

- **Zenodo:** indexa y hace buscable el paquete de datos al depositarse.
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
- Zenodo: accesible vía DOI en cuanto se publica el depósito.

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

| Métrica F-UJI | Puntaje | Fecha de ejecución |
|---|---|---|
| Localizable (F) | | |
| Accesible (A) | | |
| Interoperable (I) | | |
| Reutilizable (R) | | |
| Agregado | | |

La tabla anterior se completa ejecutando F-UJI sobre la URL del depósito en Zenodo, como paso de comprobación final antes del corte. Este documento corresponde al `fair_assessment.pdf` de la raíz del repositorio, exigido por la guía de la Entrega 4.
