# Paquete de modelado — AgroMoreira (diagramas en inglés, mockups en español)

Este paquete reemplaza el borrador anterior en español de varias páginas. Cada diagrama es ahora un **archivo `.drawio` individual** (un `<diagram>` por archivo, sin pestañas internas), **en inglés** —así lo solicitó el ingeniero para los diagramas técnicos—, con el **mismo estilo visual, paleta de colores y convenciones de forma** que los 16 diagramas de referencia originales del equipo (diagramas de secuencia por capas BCE con fragmentos `alt` de UML y barras de activación, diagramas de actividad tipo swimlane, la paleta `light-dark(...)`). Cada diagrama también se exporta como imagen PNG en `Images/`, generada directamente desde el archivo `.drawio` para que los dos nunca queden desincronizados.

Los **mockups** (`Mockups/`) sí están en **español**, junto con este README y los documentos de especificación — son la parte del paquete que se presenta y se lee en la defensa.

## Qué cambió respecto a los 16 diagramas originales

Los 16 diagramas originales (AD01-03, CD01, COMP01, DEP01, SD01, SEQ01-09) se construyeron en una fase anterior del proyecto: solo 2 actores (Administrador, Jornalero), una numeración de RF más antigua (~RF-01 a RF-16), y un modelo de dominio sin entidades legales/de cumplimiento. Se conservan como **plantilla de formato** —su diagramación y estilo no cambiaron— pero cada referencia a RF/CU dentro de ellos se corrigió al catálogo **actual** (39 RF + 21 RNF, CU-01 a CU-14), y los diagramas de componentes/despliegue se ampliaron con un `ComplianceModule` y un nodo de sistema externo AGROCALIDAD.

Se agregaron 16 diagramas nuevos, en el mismo estilo, para cubrir lo que los originales no cubrían: los actores Técnico y AGROCALIDAD, el actor Sistema de IA, y el dominio de cumplimiento legal LOPDP/AGROCALIDAD (consentimiento, derechos ARCO+, visitas técnicas, riesgo laboral, aviso de plaga cuarentenaria, cumplimiento BPA).

## Índice de diagramas (`Diagrams/`, 32 archivos, en inglés)

| Archivo | Tipo | Cubre |
|---|---|---|
| CTX01_Context_Diagram | Contexto | Todos los actores ↔ sistema |
| CTX02_Power_Interest_Matrix | Matriz de interesados | Todos los interesados |
| ISTAR01_Strategic_Dependency_SD | i* SD | Todos los actores |
| ISTAR02_Strategic_Rationale_SR | i* SR | Administrador |
| UC01_General_Use_Case_Diagram | Casos de uso | CU-01 a CU-14, 5 actores |
| CD01_Refined_Class_Diagram | Clases (actualizado) | Dominio operativo central |
| CD02_Legal_Compliance_Class_Diagram | Clases (nuevo) | Dominio LOPDP/AGROCALIDAD |
| AD01-03 | Actividad (actualizado) | CU-02/03/05/06/07/08 |
| AD04-07 | Actividad (nuevo) | CU-09, CU-10/13, CU-11, CU-14 |
| SEQ01-09 | Secuencia (actualizado) | CU-01, CU-02, CU-03, CU-05, CU-04, CU-07, CU-09 |
| SEQ10-14 | Secuencia (nuevo) | CU-09 (consentimiento, ARCO+), CU-06 (confirmar/descartar/disentir), CU-10, CU-14 |
| SD01 | Estados (actualizado) | CU-07 (ciclo de vida de la tarea) |
| SD02 | Estados (nuevo) | CU-06 (ciclo de vida de la alerta de IA) |
| COMP01 | Componentes (actualizado) | Arquitectura completa incl. ComplianceModule |
| DEP01 | Despliegue (actualizado) | Despliegue completo incl. nodo AGROCALIDAD |

## Mockups (`Mockups/`, 9 pantallas individuales + 1 prototipo general — en español)

De `MU-01` a `MU-09`, un archivo HTML por pantalla, cada uno autocontenido y exportado también a `Mockups/Images/*.png`. `MU-00_Prototype.html` es el punto de entrada general: una carcasa clicable (barra lateral + escenario tipo teléfono) que enlaza todas las pantallas individuales entre sí, para poder abrirla y recorrerla como *el* prototipo, sin necesidad de tener los 9 archivos cargados de memoria.

## Texto de apoyo

- `00_Use_Case_Specifications.md` — especificación textual completa de CU-01 a CU-14 (en inglés).
- `00_User_Stories_Acceptance_Criteria.md` — HU/CA en formato Gherkin para los RF Must-have que tienen una asociada (en inglés).

## Trazabilidad

Ver `../04_Trazabilidad/Matriz_Trazabilidad_v2.csv` y su README — 60 filas cerradas, todos los IDs de este paquete (CU, Componente, Mockup) coinciden exactamente con la matriz.

## Regeneración

Todo lo de esta carpeta se produce con scripts de Python usando `gen_lib.py` (generador de diagramas que respeta el estilo de referencia) y `render_drawio.py` / `render_mockups.py` (exportación de PNG basada en Playwright), de modo que todo el paquete puede reconstruirse de forma determinista si el texto de los requisitos vuelve a cambiar.
