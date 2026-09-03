# Declaración de uso de IA — Proyecto ACERS (SGA)

Este documento declara, sección por sección, el uso de herramientas de Inteligencia
Artificial (LLM) en la elaboración del ERS/SRS y del manuscrito, conforme a la
Entrega 4 (2B) y a las políticas editoriales de Elsevier y Springer Nature.

**Política aplicada:** El LLM se utilizó únicamente para **pulir la redacción** de
párrafos cuyo contenido ya fue escrito por el equipo con base en datos empíricos.
El LLM NO produjo resultados, cifras, tablas, figuras ni conclusiones. Todos los
datos proceden de los scripts versionados en `06_Experimento/scripts_analisis/` y
en `07_Datos/scripts/`.

> Nota para el equipo: confirmar/ajustar la herramienta exacta (modelo y versión
> usada por cada integrante) y la temperatura configurada antes del envío. Las
> columnas marcadas con `(*)` requieren verificación del integrante responsable.

## ERS/SRS (`01_ERS/ERS_SRS_2B_v2.0`)

| Sección | Herramienta | Para qué | Quién verificó | Método de verificación |
|---|---|---|---|---|
| Portada e historial | LLM (redacción) (*) | Redacción de metadatos y resumen | María Escudero (*) | Lectura y contraste con el contenido |
| Introducción (1) | — | Sin uso de IA | Equipo | Redacción propia sobre evidencia del dominio |
| Glosario y siglas | LLM (redacción) (*) | Pulido de definiciones | Kamila Calle (*) | Contraste con normas ISO citadas |
| Contexto y stakeholders | — | Sin uso de IA | Equipo | Basado en entrevistas (entries) |
| Requisitos funcionales (RF) | — | Sin uso de IA | Equipo | Derivados de entrevistas y matriz de trazabilidad |
| Requisitos no funcionales (RNF) | — | Sin uso de IA | Equipo | Basados en calidad (ISO 25010) |
| Modelo legal LOPDP | — | Sin uso de IA | Equipo | Derivado de la norma citada |
| Trazabilidad | — | Sin uso de IA | Equipo | Matriz Ley→Mockup en `04_Trazabilidad/` |
| Anexos | LLM (redacción) (*) | Pulido de anexos | Danela Arteaga (*) | Revisión editorial |

## Manuscrito (`07_Publicacion/manuscrito_final.tex`)

| Sección | Herramienta | Para qué | Quién verificó | Método de verificación |
|---|---|---|---|---|
| Título y resumen | LLM (redacción) (*) | Pulido y ajuste a plantilla | Jeanpierre Robinson (*) | Coherencia con datos y guía |
| Introducción | LLM (redacción) (*) | Pulido de párrafos ya escritos | Jeanpierre Robinson (*) | Contraste con evidencia del dominio |
| Trabajo relacionado | — | Sin uso de IA | Equipo | Referencias verificadas en `referencias.bib` |
| Metodología | — | Sin uso de IA | Equipo | Registro OSF + plantilla experimental |
| Resultados | — | Sin uso de IA (PROHIBIDO) | Equipo | Tablas/figuras generadas por script en `07_Datos/resultados/` |
| Discusión | LLM (redacción) (*) | Pulido de redacción | María Escudero (*) | Trazabilidad a datos de resultados |
| Amenazas a la validez | — | Sin uso de IA | Equipo | Basado en Wohlin et al. |
| Conclusiones | LLM (redacción) (*) | Pulido de redacción | Roselyn Sánchez (*) | Contraste con hallazgos de resultados |
| Referencias | — | Sin uso de IA | Equipo | DOIs verificados manualmente (anti-hallucination) |

---

**Resumen:** El LLM se empleó exclusivamente para la redacción (redacción editorial).
Toda cifra, tabla y figura procede de la ejecución reproducible de los scripts.
Declaración sujeta a revisión por el tribunal según la política de integridad de la
Entrega 4 (2B).
