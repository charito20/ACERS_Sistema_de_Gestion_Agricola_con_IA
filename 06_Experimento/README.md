# 06_Experimento

Carpeta con el protocolo del experimento y los comprobantes de registro/desviaciones (OSF).

| Archivo | Contenido |
|---|---|
| `protocolo.tex` | Protocolo del experimento. Compilar con `pdflatex`, luego `bibtex`, luego `pdflatex` dos veces más (usa `referencias.bib`). |
| `protocolo.pdf` | Documento compilado. |
| `osf_registration.tex` | Registro OSF del experimento. Compilar con `pdflatex`, dos pasadas seguidas (no requiere bibtex). |
| `osf_registration.pdf` | Documento compilado. |
| `osf_registration.png` | Captura del comprobante externo de registro en OSF. |
| `osf_deviations.tex` | Registro de desviaciones respecto del protocolo. Compilar con `pdflatex`, dos pasadas seguidas (no requiere bibtex). |
| `osf_deviations.pdf` | Documento compilado. |
| `referencias.bib` | Bibliografía usada por `protocolo.tex`. |
| `justificacion_muestra.md` | Justificación del tamaño de muestra y número de evaluadores, escrita antes de analizar. |
| `instrumentos/` | Instrumentos de recolección de datos. |
| `prompts_llm/` | Prompts usados con herramientas de IA en el experimento. |
| `resultados/` | Resultados del análisis experimental. |
| `scripts_analisis/` | Scripts para reproducir el análisis. |

Compilador: `pdflatex` (TeX Live o MiKTeX), verificado en este repositorio. No se requieren paquetes fuera de la distribución estándar.
