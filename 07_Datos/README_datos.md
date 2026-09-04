# README_datos - Paquete de datos (07_Datos)

Este paquete contiene los datos crudos, el código de análisis y los resultados
del componente empírico del proyecto ACERS (Sistema de Gestión Agrícola con IA).

## Reproducción

> Un tercero clona el repositorio en una máquina limpia, ejecuta la orden única
> declarada aquí y obtiene, sin intervención manual, exactamente las mismas tablas
> y figuras que aparecen en los documentos. Si eso no ocurre, el paquete de datos
> no está terminado.

Desde la raíz del repositorio:

```bash
pip install -r 07_Datos/scripts/requirements.txt
python 07_Datos/scripts/run_all.py
```

La única orden de ejecución es `python 07_Datos/scripts/run_all.py`.

## Estructura

| Carpeta/archivo | Descripción |
|---|---|
| `datos_crudos/` | Datos sin procesar: cobertura legal por criterio y matriz de trazabilidad. |
| `datos_procesados/` | Datos transformados/limpiados durante el análisis (resultados intermedios). |
| `scripts/` | Código reproducible: `analisis_legalfirst.py` + orquestador `run_all.py`. |
| `resultados/` | Tablas y figuras generadas por los scripts (nunca a mano). |
| `diccionario_datos.csv` | Definición de cada columna de los datos. |
| `LICENSE-DATA.txt` | Licencia del conjunto de datos (CC BY 4.0). |
| `checksums_datos.sha256` | Hashes SHA-256 del contenido definitivo del paquete. |
| `desviaciones.md` | Desviaciones del protocolo respecto del registro OSF. |
| `registro_deposito.md` | Identificador persistente del depósito y su fecha. |

## Fuente de los datos

- `datos_crudos/cobertura_legal.csv`: matriz de cobertura de los 26 criterios
  (LOPDP, BPA y Bioseguridad) evaluados con enfoque convencional y con enfoque
  *legal-first*, derivada de `01_ERS/Modelo_Legal_LOPDP.md`.
- `datos_crudos/Matriz_Trazabilidad_v2.xlsx`: matriz de trazabilidad Ley→Mockup
  del proyecto (ver `04_Trazabilidad/`).

## Salidas generadas

- `resultados/tabla_mcnemar.csv`: prueba de McNemar (estadístico, valor p, b, c).
- `resultados/descriptivos_bloque.csv`: cobertura por bloque normativo.
- `resultados/curva_o_barras.png`: figura de cobertura antes/después por bloque.
