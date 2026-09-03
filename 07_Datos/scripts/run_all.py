#!/usr/bin/env python3
"""
Orquestador único del paquete de datos ACERS.
Ejecuta: python run_all.py
Lee 07_Datos/datos_crudos/, produce 07_Datos/datos_procesados/ y genera todas
las tablas y figuras en 07_Datos/resultados/ que se citan en el ERS y el manuscrito.

TODO (equipo): reemplazar los pasos de ejemplo por el pipeline real una vez estén
depositados los datos crudos (matriz legal-requisito, hojas de evaluación
independiente, respuestas de cuestionario).
"""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
CRUDOS = RAIZ / "datos_crudos"
PROCESADOS = RAIZ / "datos_procesados"
RESULTADOS = RAIZ / "resultados"

def main():
    PROCESADOS.mkdir(exist_ok=True)
    RESULTADOS.mkdir(exist_ok=True)
    print(f"Leyendo datos crudos desde: {CRUDOS}")
    # TODO: cargar matriz_legal_requisito.csv, hojas_codificacion_*.csv, respuestas_cuestionario.csv
    # TODO: calcular kappa de Cohen con intervalo de confianza (evaluación independiente)
    # TODO: generar tabla de cobertura legal -> requisito en resultados/
    # TODO: generar figura/tabla de justificación de tamaño de muestra
    print("Pipeline placeholder: completar con el análisis real antes de depositar.")

if __name__ == "__main__":
    main()
