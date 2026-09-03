# Replication package for "Cobertura de requisitos legales de protección de datos y de trazabilidad agroindustrial mediante un enfoque legal-first: un estudio de caso en un sistema de gestión agrícola ecuatoriano"

Conjunto de datos y materiales de replicación del estudio empírico sobre la cobertura de requisitos legales de protección de datos y de trazabilidad agroindustrial en AgroMoreira, un sistema de gestión agrícola con inteligencia artificial para el cultivo de cacao y plátano verde en Ecuador. El estudio aplica el enfoque legal-first de Amaral et al. (2021) para comparar la cobertura de 26 criterios legales, en tres bloques normativos, antes y después de derivar requisitos directamente del texto legal.

El DOI de Zenodo, la referencia del manuscrito asociado y la URL del registro OSF del protocolo se incorporan a este encabezado en el momento del depósito. La licencia es CC BY 4.0 para los datos y la documentación y MIT para el código, según el archivo `LICENSE` del repositorio.

## Autoría

| Nombre | ORCID |
|---|---|
| Jeanpierre Robinson Espinoza | 0009-0005-3302-1822 |
| Kamila Annabella Calle Delgado | 0009-0002-8249-9601 |
| Danela Dayana Arteaga Álava | 0009-0006-0318-1531 |
| María del Rosario Escudero Plaza | 0009-0007-3212-9924 |
| Roselyn Andreina Sánchez Centeno | 0009-0008-7204-8448 |
| Gleiston Cicerón Guerrero Ulloa (docente supervisor) | 0000-0001-5990-2357 |

## Contenido del depósito

El depósito reúne el paquete de análisis reproducible de `07_Datos/` del repositorio junto con la evidencia de campo anonimizada.

| Elemento | Origen en el repositorio | Descripción |
|---|---|---|
| `07_Datos/` | carpeta completa | Datos crudos, scripts de análisis en Python, resultados y diccionario de datos |
| `07_Datos/datos_crudos/cobertura_legal.csv` | | Matriz de cobertura de los 26 criterios legales, antes y después del enfoque legal-first |
| `07_Datos/datos_crudos/Matriz_Trazabilidad_v2.xlsx` | copia de `04_Trazabilidad/` | Matriz de trazabilidad de la ley al requisito, al caso de uso, al componente y al mockup |
| `07_Datos/scripts/` | | `analisis_legalfirst.py` y el orquestador `run_all.py` |
| `07_Datos/resultados/` | | Tabla de McNemar, descriptivos por bloque y figura de cobertura, todo producido por los scripts |
| transcripciones anonimizadas | `02_Evidencias/Transcripciones/` | 17 entrevistas en Markdown, con código de participante en lugar de nombres |
| respuestas del cuestionario | `02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario.csv` | Respuestas sin columnas de nombre, correo, teléfono ni IP |
| corpus de requisitos | `01_ERS/ERS_SRS_2B_v2.0` y `01_ERS/priorizacion_moscow_kano.csv` | Los 39 requisitos funcionales y 15 no funcionales con su prioridad y su evidencia |
| manuscrito | `07_Publicacion/manuscrito_final.pdf` | Versión compilada del manuscrito asociado |
| `ANONYMIZATION.md` | esta carpeta | Cómo se trató cada tipo de dato antes de publicarlo |
| `ETHICS.md` | esta carpeta | Resumen del proceso de consentimiento y del marco legal del estudio |

## Cómo reproducir el análisis

Desde la raíz del repositorio, con Python 3.10 o superior:

```
pip install -r 07_Datos/scripts/requirements.txt
python 07_Datos/scripts/run_all.py
```

El script lee `07_Datos/datos_crudos/cobertura_legal.csv`, ejecuta la prueba de McNemar pareada sobre los 26 criterios y escribe en `07_Datos/resultados/` la tabla de McNemar, los descriptivos por bloque normativo y la figura de cobertura, que son las que aparecen en el manuscrito. Las dependencias son pandas, numpy, scipy, statsmodels, matplotlib y seaborn, con las versiones fijadas en `requirements.txt`.

## Diccionario de datos

El archivo `07_Datos/diccionario_datos.csv` define cada columna. Para `cobertura_legal.csv`, separado por punto y coma, las columnas son:

| Columna | Tipo | Valores |
|---|---|---|
| `criterio` | texto | C1 a C26 |
| `bloque` | categórico | LOPDP, BPA, Bioseguridad |
| `articulo` | texto | referencia al articulado de la LOPDP, la Resolución 183 o la Resolución 0072 |
| `cubierto_convencional` | binario | 0 o 1 |
| `cubierto_legalfirst` | binario | 0 o 1 |
| `requisitos_cubre` | texto | identificadores de requisito, o un guion si el criterio no queda cubierto |

## Cómo citar este conjunto de datos

La cita se genera a partir del `CITATION.cff` del repositorio una vez asignado el DOI de Zenodo, con el formato siguiente:

> Calle Delgado, K. A., Arteaga Álava, D. D., Escudero Plaza, M. del R., Sánchez Centeno, R. A., Espinoza, J. R., y Guerrero Ulloa, G. C. (2026). Replication package for "Cobertura de requisitos legales de protección de datos y de trazabilidad agroindustrial mediante un enfoque legal-first" [conjunto de datos]. Zenodo.

## Principios seguidos

Este paquete sigue los principios FAIR, localizable, accesible, interoperable y reutilizable, de Wilkinson et al. (2016), y los principios de citación de software de Smith et al. (2016). El resultado de la autoevaluación FAIR está en `07_Datos/fair_assessment.md`.
