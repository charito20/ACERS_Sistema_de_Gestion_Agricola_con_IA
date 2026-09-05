#!/usr/bin/env python3
"""
Verificación de trazabilidad: huérfanos y cadenas rotas.

Comprueba, contra los artefactos reales del repositorio y no contra lo que
declara la documentación:

  1. Cadenas rotas: celdas vacías en cualquier eslabón de la matriz
     (evidencia -> requisito -> caso de uso -> historia -> criterio de
     aceptación -> componente -> maqueta -> caso de prueba).
  2. Huérfanos hacia adelante: requisitos especificados en el ERS que no
     tienen fila en la matriz de trazabilidad.
  3. Huérfanos hacia atrás: identificadores de la matriz que no existen
     como requisito en el ERS.
  4. Casos de uso especificados en el paquete de modelado que no aparecen
     en ninguna fila de la matriz.
  5. Filas cuya evidencia de elicitación es "Sin evidencia", clasificadas
     por causa.

Uso:  python3 04_Trazabilidad/verificar_trazabilidad.py
Salida: informe por consola y código de salida 0 si no hay hallazgos
        bloqueantes, 1 si los hay.
"""

import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
MATRIZ = RAIZ / "04_Trazabilidad" / "Matriz_Trazabilidad_v2.xlsx"
ERS = RAIZ / "01_ERS" / "ERS_SRS_2B_v2.0.md"
CASOS_USO = RAIZ / "03_Modelado" / "00_Use_Case_Specifications.md"

ESLABONES = [
    "ID-EV", "ID-RF/RNF/RD", "ID-CU", "ID-HU",
    "ID-CA", "ID-Componente", "ID-Maqueta", "ID-Caso-Prueba",
]
VACIO = {None, "", "-", "N/A", "n/a"}


def cargar_matriz():
    hoja = openpyxl.load_workbook(MATRIZ).active
    filas = [list(f) for f in hoja.iter_rows(values_only=True) if any(f)]
    encabezado = [str(c).strip() for c in filas[0]]
    return encabezado, filas[1:]


def main():
    encabezado, filas = cargar_matriz()
    idx = {n: i for i, n in enumerate(encabezado)}
    hallazgos = 0

    print(f"Matriz: {len(filas)} filas x {len(encabezado)} columnas\n")

    # 1. cadenas rotas
    print("1. Cadenas rotas (celdas vacías en un eslabón)")
    rotas = 0
    for col in ESLABONES:
        if col not in idx:
            print(f"   AVISO: la columna {col} no existe en la matriz")
            continue
        vacias = [f for f in filas if str(f[idx[col]]).strip() in VACIO or f[idx[col]] is None]
        if vacias:
            rotas += len(vacias)
            print(f"   {col}: {len(vacias)} filas sin valor")
    print("   Sin cadenas rotas." if rotas == 0 else f"   TOTAL: {rotas}")
    hallazgos += rotas

    # 2 y 3. huérfanos entre ERS y matriz
    texto_ers = ERS.read_text(encoding="utf-8")
    req_ers = set(re.findall(r"^#+ ((?:RF|RNF)-\d+)\.", texto_ers, re.M))
    req_matriz = {str(f[idx["ID-RF/RNF/RD"]]).strip() for f in filas}

    print("\n2. Requisitos del ERS sin fila en la matriz (huérfanos hacia adelante)")
    sin_fila = sorted(req_ers - req_matriz)
    print(f"   Ninguno ({len(req_ers)} requisitos trazados)." if not sin_fila else f"   {sin_fila}")
    hallazgos += len(sin_fila)

    print("\n3. Identificadores de la matriz que no existen en el ERS (huérfanos hacia atrás)")
    sin_req = sorted(req_matriz - req_ers)
    print("   Ninguno." if not sin_req else f"   {sin_req}")
    hallazgos += len(sin_req)

    # 4. casos de uso
    print("\n4. Casos de uso especificados que no aparecen en la matriz")
    cu_spec = set(re.findall(r"CU-\d+", CASOS_USO.read_text(encoding="utf-8")))
    cu_matriz = set()
    for f in filas:
        cu_matriz |= set(re.findall(r"CU-\d+", str(f[idx["ID-CU"]])))
    faltan_cu = sorted(cu_spec - cu_matriz)
    print(f"   Ninguno ({len(cu_spec)} casos de uso trazados)." if not faltan_cu else f"   {faltan_cu}")
    hallazgos += len(faltan_cu)

    # 5. sin evidencia de elicitación, clasificado por causa
    print("\n5. Filas con evidencia de elicitación 'Sin evidencia' (no es un hallazgo: se clasifica)")
    sin_ev = [f for f in filas if "Sin evidencia" in str(f[idx["ID-EV"]])]
    por_tipo = Counter(str(f[idx["Tipo"]]).strip() for f in sin_ev)
    por_norma = Counter(str(f[idx["Ley/Norma"]]).strip() for f in sin_ev)
    print(f"   Total: {len(sin_ev)} de {len(filas)}")
    print(f"   Por tipo: {dict(por_tipo)}")
    for norma, n in por_norma.most_common():
        ids = [str(f[idx['ID-RF/RNF/RD']]) for f in sin_ev if str(f[idx["Ley/Norma"]]).strip() == norma]
        print(f"   - {norma}: {n} -> {', '.join(sorted(ids))}")

    print("\n" + "=" * 60)
    if hallazgos == 0:
        print("RESULTADO: sin huérfanos y sin cadenas rotas.")
        return 0
    print(f"RESULTADO: {hallazgos} hallazgo(s) que requieren acción.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
