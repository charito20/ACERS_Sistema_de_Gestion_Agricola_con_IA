# Resultados - Enfoque 2 legal-first (Cobertura 26 criterios)

Proyecto: ACERS - Agricola Moreira
Integrante: Escudero Plaza Maria del Rosario
Estado: estructura actualizada a 2B; datos reales en 01_ERS/Modelo_Legal_LOPDP.md y 04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx

## Estructura 2B (real repo)

| Archivo | Descripcion | Fuente real |
|---|---|---|
| cobertura_legal.csv | Tabla pareada C1-C26: criterio,bloque,cubierto_convencional(0/1),cubierto_legalfirst(0/1) | Derivada de Matriz_Trazabilidad_v2.xlsx |
| descriptivos_bloque.csv | Proporcion por bloque LOPDP/BPA/Bioseguridad | Generado por analisis_legalfirst.py |
| tabla_mcnemar.csv | Resultado McNemar + IC95% bootstrap | Generado por script |
| conjunto_a_llm.csv | DEPRECADO Enfoque 1 | Conservar vacio |
| conjunto_b_ers.csv | DEPRECADO Enfoque 1 | Conservar vacio |
| figuras/curva y barras | Barras por bloque y tabla 2x2 | Generadas por script |

## Columnas cobertura_legal.csv (nueva)

criterio;bloque;articulo;cubierto_convencional;cubierto_legalfirst;requisitos_cubre
C1;LOPDP;Art.4,12(8);0;1;RF-22
...

## Reproducibilidad 2B

python 06_Experimento/scripts_analisis/analisis_legalfirst.py --matriz 04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx --out 06_Experimento/resultados/

Ninguna tabla manual. Todo via script McNemar.
