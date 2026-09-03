#!/usr/bin/env python3
"""
run_all.py - Orquestador único del paquete de datos 07_Datos/

Ejecuta todo el pipeline con una sola orden, desde datos crudos hasta los
resultados finales, de forma reproducible:

    python scripts/run_all.py

(o desde la raíz del repositorio). Todas las tablas y figuras de los documentos
se generan aquí, sin intervención manual.
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    # Ejecutar el análisis legal-first, que lee datos_crudos/ y escribe resultados/
    analisis = os.path.join(RAIZ, "scripts", "analisis_legalfirst.py")
    print("[1/1] Ejecutando análisis legal-first (McNemar, descriptivos, figura)...")
    subprocess.run([sys.executable, analisis], check=True)

    print("\nPipeline completado.")
    resultados = os.path.join(RAIZ, "resultados")
    for f in sorted(os.listdir(resultados)):
        print(f"  -> {f}")
    print("\nVerificación: compara estas salidas con las tablas/figuras del manuscrito.")


if __name__ == "__main__":
    main()
