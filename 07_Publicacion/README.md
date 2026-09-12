# 07_Publicacion

Carpeta con el manuscrito final preparado para envío a revista.

| Archivo | Contenido |
|---|---|
| `manuscrito_final.tex` | Manuscrito final. Compilar con `pdflatex`, luego `bibtex`, luego `pdflatex` dos veces más (usa `referencias.bib` y las clases `sn-jnl.cls` incluidas en esta misma carpeta, junto con los estilos `sn-*.bst`). |
| `manuscrito_final.pdf` | Documento compilado, 10 páginas. |
| `referencias.bib` | Bibliografía del manuscrito. |
| `referencias_verificacion.csv` | Verificación de las referencias citadas. |
| `analisis_revistas.md` | Análisis de revistas objetivo para el envío. |
| `dataset_zenodo/` | Paquete de datos preparado para depósito en Zenodo. |
| `sn-jnl.cls`, `sn-*.bst` | Clase y estilos bibliográficos de Springer Nature requeridos para compilar `manuscrito_final.tex`. No modificar ni mover. |

Compilador: `pdflatex` (TeX Live o MiKTeX), verificado en este repositorio. Todas las dependencias (clase y estilos) ya están incluidas en esta carpeta, no es necesario instalar nada externo.
