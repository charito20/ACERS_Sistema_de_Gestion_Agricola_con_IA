# Changelog
Todos los cambios notables de este proyecto se documentan en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto sigue el versionado semántico donde es aplicable.

## [Entrega Final - 2B] - 2026-09-05
Etiqueta de línea base: `v2.0-final` (commit `cc8cf4a`)

### Añadido
- Informe final del proyecto (`07_Publicacion/`), documento único generado desde LaTeX que integra la especificación auditada, el estudio empírico ejecutado y el análisis de resultados, con carátula obligatoria conforme a la sección 12 de la guía.
- Ejecución completa del componente empírico: recolección de datos primarios según el protocolo registrado, análisis reproducible mediante scripts versionados (`06_Experimento/scripts_analisis/`), magnitud del efecto con intervalo de confianza, acuerdo entre evaluadores y lista de verificación de reporte cumplimentada.
- Cierre de la matriz de trazabilidad extremo a extremo (`04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx`), con tabla de huérfanos y cadenas rotas resuelta y porcentaje de sincronización con el tablero calculado.
- Fichas de requisitos de los componentes de IA: requisitos funcionales, de rendimiento, de equidad y de explicabilidad con umbral, unidad y método de comprobación; clasificación de riesgo y base legal.
- Adenda ética de la ronda de campo correspondiente a esta entrega (`08_Etica/`), protocolo de disociación de datos personales y política de conservación y supresión.
- Declaraciones obligatorias completas (`07_Publicacion/declaraciones/`): contribución individual con roles, conflicto de interés, financiamiento, cumplimiento ético, consentimiento para difusión, disponibilidad de datos y de código, uso de inteligencia artificial y originalidad.
- Informe de control de similitud y revisión cruzada entre equipos con carta de respuesta fila por fila (`07_Publicacion/revision_cruzada/`).
- Presentación de defensa individual y banco de preguntas con respuestas ancladas a artefactos (`09_Defensa/`).
- Etiqueta de línea base final anotada, alcanzable desde la rama por defecto y publicada en el repositorio remoto.
- Depósito del paquete de replicación en Zenodo con DOI persistente `10.5281/zenodo.22307881`, registro previo del protocolo en OSF (`https://osf.io/7cvhy`), citado en `CITATION.cff` y en el README, conforme a la compuerta I5 de la guía.

### Cambiado
- <!-- ej. "Requisitos no funcionales ajustados tras la auditoría de calidad de la especificación" -->

### Corregido
- Cita cruzada corregida en la sección 6 (`sec6`) del informe final.
- <!-- ej. "Huérfanos y cadenas rotas de la matriz de trazabilidad cerrados tras la auditoría del repositorio" -->
- <!-- ej. "Referencias con campos incompletos o identificadores que no resolvían, verificadas una a una" -->

## [Entrega 3 - 2A] - 2026-07-29
### Añadido
- ERS/SRS completo v1.0 con requisitos funcionales, no funcionales, historias de usuario en formato Connextra y criterios de aceptación en Gherkin.
- Modelado UML completo: diagrama de casos de uso general, especificación textual de casos de uso, diagrama de clases refinado, diagramas de secuencia, actividad, estados, componentes y despliegue.
- Matriz de trazabilidad extendida (Ley → Objetivo → Interesado → EV → RF/RNF/RD → CU → HU → CA → Componente → Mockup).
- Priorización combinada MoSCoW + Kano + WSJF.
- Protocolo experimental y registro previo en OSF.
- Segunda ronda de trabajo de campo: nuevos consentimientos, entrevistas en video/audio, cuestionario ampliado.
- LICENSE, CITATION.cff, checksums.sha256, .gitignore.
### Cambiado
- <!-- ej. "Requisitos funcionales revisados según observaciones docentes de la Entrega 2 (1B)" -->
### Corregido
- <!-- ej. "Correcciones al diagrama de clases señaladas en la Entrega 2 (1B)" -->

## [Entrega 2 - 1B] - 2026-07-01
### Añadido
- ERS/SRS parcial: introducción, descripción general, requisitos preliminares.
- Primera ronda de trabajo de campo: entrevistas con administrador y trabajador de campo de Agrícola Moreira.
- Wireframes HTML del sistema (dashboard, tareas de personal, registro de cosechas, control de plagas, inventario de insumos).
- Documentación UML inicial (10 casos de uso, diagrama de casos de uso).

---
