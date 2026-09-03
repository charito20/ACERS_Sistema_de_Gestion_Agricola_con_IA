# Evaluación FAIR — Paquete de datos ACERS

**Fecha de evaluación:** Pendiente (ejecutar después del depósito en Zenodo)
**Herramienta:** F-UJI (https://www.fairdatainitiative.org/f-uji-test/)
**Evaluador:** Equipo ACERS

## Identificadores persistentes

| Elemento | Identificador | Estado |
|---|---|---|
| Repositorio GitHub | https://github.com/charito20/ACERS_Sistema_de_Gestion_Agricola_con_IA | ✅ Activo |
| DOI Zenodo | Pendiente de depósito | ⏳ Pendiente |
| OSF | https://osf.io/7cvhy | ✅ Activo, publico |
| SWHID | Pendiente de archivado | ⏳ Pendiente |

## Principios FAIR

### F1 — Se asigna un identificador global persistente y único

- **Repositorio:** DOI de Zenodo (pendiente)
- **Datos:** DOI de Zenodo bajo CC BY 4.0 (pendiente)
- **OSF:** https://osf.io/7cvhy (registrado 2026-08-02)

### F2 — Se describe el recurso con metadatos enriquecidos

- `CITATION.cff`: metadatos CFF 1.2.0 con autores, ORCID, licencia
- `07_Datos/README_datos.md`: descripción del paquete de datos
- `07_Datos/diccionario_datos.csv`: diccionario de datos

### F3 — Los metadatos incluyen el identificador del recurso

- `CITATION.cff` enlaza el repositorio GitHub
- El DOI de Zenodo se incorporará a `CITATION.cff` y al README tras el depósito

### F4 — El recurso se registra o busca en un repositorio de acceso abierto

- **Zenodo:** pendiente de depósito
- **Software Heritage:** pendiente de archivado (botón "Save code now")

### R1.1 — Los metadatos están bajo una licencia de acceso abierto

- Licencia del repositorio: MIT (código) + CC BY 4.0 (datos)
- `07_Datos/LICENSE-DATA.txt`: CC BY 4.0

### R1.2 — Los metadatos incluyen detalles de creación

- Autores con ORCID en `CITATION.cff`
- Fecha de liberación: 2026-08-30

### R1.3 — Los metadatos incluyen referencias a otros metadatos

- Referencias cruzadas a ERS, matriz de trazabilidad, transcripciones

### A1.1 — El recurso se puede recuperar por su identificador

- GitHub: accesible vía HTTPS
- Zenodo: accesible vía DOI (pendiente)

### A1.2 — El protocolo está claro y abierto

- OSF: preregistro público con protocolo completo

### I1.1 — Los metadatos usan un vocabulario de acceso abierto

- Términos Dublin Core vía CFF
- CIF (Crystallographic Information Framework) no aplica

### I1.2 — Los metadatos usan un vocabulario conforme a FAIR

- CFF 1.2.0 es un estándar reconocido

### I2.1 — Los metadatos están representados en un formato de acceso abierto

- CFF: YAML (acceso abierto)
- CSV: formato tabular abierto

### L1.1 — El contenido se publica con una licencia de acceso abierto

- MIT para código
- CC BY 4.0 para datos

---

*Este assessment se convertirá en `fair_assessment.pdf` tras ejecutar F-UJI con la URL del depósito Zenodo.*
