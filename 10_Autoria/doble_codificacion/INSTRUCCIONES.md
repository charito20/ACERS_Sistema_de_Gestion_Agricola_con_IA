# Instrucciones — doble codificación (kappa)

Esto es lo único que le falta a Danela de su lista. Se necesitan **dos personas
distintas** (por ejemplo Danela + Kamila, o Danela + otra compañera que no haya
hecho ya `02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv`).

## Qué hacer

1. Cada persona abre **por separado**, sin consultarse entre sí, las 6
   entrevistas ya elegidas (`ENTR-01, ENTR-05, ENTR-09, ENTR-12, ENTR-15,
   ENTR-17` — están en `02_Evidencias/Transcripciones/`).
2. Para cada entrevista, decide cuál es el **tema dominante** (el más
   presente) usando SOLO estos 12 códigos del codebook del equipo
   (`02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv`):

   | Código | Categoría |
   |---|---|
   | RCD | Registro de cultivos |
   | RCO | Registro de cosecha |
   | PLA | Plagas y enfermedades |
   | INV | Inventario de insumos |
   | TAR | Tareas laborales |
   | PER | Seguimiento de producción |
   | COS | Costos e ingresos |
   | ALA | Alertas automáticas |
   | AIa | Recomendaciones IA |
   | SAT | Registro de actividades |
   | DPL | Pérdida de datos |
   | RPT | Reportes |

   Si ninguno aplica claramente, se usa `no_aplica`.
3. Cada persona llena su propio archivo (`codificador_a.csv` la primera
   persona, `codificador_b.csv` la segunda) poniendo el código en la columna
   `categoria`, **sin ver lo que puso la otra persona** — esa independencia es
   justo lo que se está midiendo.
4. Cuando ambos archivos estén completos, se corre (con Python instalado):
   ```
   pip install --break-system-packages numpy scipy matplotlib
   cd 10_Autoria/doble_codificacion
   python3 calcular_kappa.py codificador_a.csv codificador_b.csv --output .
   ```
5. Eso genera automáticamente `correspondencia_kappa.csv`,
   `resultado_kappa.txt` y `grafico_kappa.png` dentro de la misma carpeta —
   esos 3 archivos son la evidencia que hay que subir al repositorio.

## Si quieren codificar más de 6 entrevistas

Se puede — solo hay que agregar más filas con el mismo formato
(`id_entrevista,categoria`) en los dos archivos, en el mismo orden, antes de
correr el script. Con 17 entrevistas en total, 6 es un tamaño razonable para
esta prueba de confiabilidad sin duplicar todo el trabajo de codificación.
