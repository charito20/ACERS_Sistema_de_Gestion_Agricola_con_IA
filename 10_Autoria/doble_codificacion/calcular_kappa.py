#!/usr/bin/env python3
"""
calcular_kappa.py
Calcula el coeficiente de acuerdo inter-codificador (kappa de Cohen) con su
intervalo de confianza al 95%, exigido en A7 de la Guia ACERS.

Requiere DOS hojas de codificacion tematica independientes, de DOS integrantes
distintos, aplicadas al MISMO subconjunto de entrevistas.

Entrada (CSVs con cabecera):
    columna id_entrevista : identificador de la entrevista (debe coincidir entre
                            ambos archivos y en el mismo orden)
    columna categoria      : codigo tematico asignado (RCD, RCO, PLA, INV, TAR,
                            PER, COS, ALA, AIa, SAT, DPL, RPT o "no_aplica")

Salida:
    - correspondencia_kappa.csv  (matriz de confusion / tabla de clasificacion cruzada)
    - resultado_kappa.txt        (kappa, IC95%, interpretacion de Landis y Koch)
    - grafico_kappa.png          (diagrama de dispersion de doble codificacion)

Uso:
    pip install --break-system-packages numpy scipy matplotlib
    python3 calcular_kappa.py codificador_a.csv codificador_b.csv --output doble_codificacion

Nota: el kappa se calcula por SCRIPT a partir de los datos de ambos codificadores,
NO a mano (requisito literal de la guia).
"""
import argparse
import csv
import sys
from pathlib import Path

try:
    import numpy as np
    from scipy.stats import norm
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("Faltan dependencias: pip install --break-system-packages numpy scipy matplotlib")

ID_A = "id_entrevista"
ID_B = "id_entrevista"
CAT = "categoria"
CAT_B = "categoria"


def leer_codificacion(path: Path, columna) -> list[str]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit(f"No hay filas en {path}")
    claves = {CAT, CAT_B}
    for k in rows[0].keys():
        if k.strip().lower().replace(" ", "_") in ("categoria", "codigo", "codigo_tematico"):
            claves.add(columna)
    # busqueda robusta de la columna categoria
    keys = list(rows[0].keys())
    cat_key = None
    for k in keys:
        if k.strip().lower() in ("categoria", "codigo", "codigo_tematico", "code", "categoría"):
            cat_key = k
            break
    if cat_key is None:
        sys.exit(f"No se encontro columna de categoria en {path}. Claves: {keys}")
    result = []
    for r in rows:
        v = r.get(cat_key, "").strip()
        result.append(v if v else "no_aplica")
    return result


def kappa_y_ic(obs_a: list[str], obs_b: list[str]):
    """Kappa de Cohen con varianza de Fleiss (aprox. normal) e IC95%."""
    cats = sorted(set(obs_a) | set(obs_b))
    n = len(obs_a)
    rango = {c: i for i, c in enumerate(cats)}
    matriz = np.zeros((len(cats), len(cats)), dtype=float)
    for a, b in zip(obs_a, obs_b):
        matriz[rango[a], rango[b]] += 1.0
    matriz /= n

    p_o = float(np.trace(matriz))
    p_i = matriz.sum(axis=1)
    p_j = matriz.sum(axis=0)
    p_a = float(np.sum(p_i * p_j))
    if 1 - p_a == 0:
        return 1.0, 0.0, matriz, rango, cats
    kappa = (p_o - p_a) / (1 - p_a)

    # Formula de varianza de Fleiss (1969), se = sqrt(var)/sqrt(n)
    var = 0.0
    for ii in range(len(cats)):
        for jj in range(len(cats)):
            pij = matriz[ii, jj]
            a = p_i[ii] + p_j[jj]
            var += pij * (a * (1 - p_o) - 2 * (1 - p_o) * (p_a - a)) ** 2
    var /= (1 - p_o) ** 2
    if var < 0:
        var = 0.0
    se = float(np.sqrt(var) / np.sqrt(n))
    return float(kappa), se, matriz, rango, cats


def interpretar(k):
    r = [
        (0.81, "acuerdo casi perfecto"),
        (0.61, "acuerdo sustancial"),
        (0.41, "acuerdo moderado"),
        (0.21, "acuerdo aceptable"),
        (0.00, "acuerdo leve"),
    ]
    for umbral, txt in r:
        if k >= umbral:
            return txt
    return "sin acuerdo"


def plot(matriz, rango, cats, n, out_png):
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(matriz, cmap="Blues")
    ax.set_xticks(range(len(cats)))
    ax.set_yticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=45, ha="right")
    ax.set_yticklabels(cats)
    ax.set_xlabel("Codificador B")
    ax.set_ylabel("Codificador A")
    for i in range(len(cats)):
        for j in range(len(cats)):
            ax.text(j, i, f"{matriz[i, j]*n:,.0f}", ha="center", va="center",
                    color="white" if matriz[i, j] > 0.5 * matriz.max() else "black")
    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cod_a", help="CSV del codificador A")
    ap.add_argument("cod_b", help="CSV del codificador B")
    ap.add_argument("--output", default="doble_codificacion", help="Carpeta de salida")
    args = ap.parse_args()

    a = leer_codificacion(Path(args.cod_a), CAT)
    b = leer_codificacion(Path(args.cod_b), CAT_B)

    if len(a) != len(b):
        sys.exit(f"Los archivos tienen distinto numero de filas: A={len(a)}, B={len(b)}. "
                 "Deben codificar el MISMO subconjunto de entrevistas.")
    n = len(a)
    kappa, se, matriz, rango, cats = kappa_y_ic(a, b)
    lo, hi = kappa - 1.96 * se, kappa + 1.96 * se

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    # estado de coincidencia
    coincidencia = [1 if x == y else 0 for x, y in zip(a, b)]

    with open(out / "correspondencia_kappa.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "codificador_A", "codificador_B", "coincide"])
        for i, (x, y) in enumerate(zip(a, b), start=1):
            w.writerow([i, x, y, 1 if x == y else 0])

    with open(out / "resultado_kappa.txt", "w", encoding="utf-8") as f:
        f.write(f"Coefficiente de acuerdo inter-codificador (kappa de Cohen)\n")
        f.write(f"Entrevistas codificadas dos veces (n): {n}\n")
        f.write(f"Total de codigos distintos: {len(cats)}\n")
        f.write(f"Proporcion de acuerdo observado (Po): {np.trace(matriz):.4f}\n")
        f.write(f"Acuerdo esperado (Pe): {np.sum(matriz.sum(axis=1)*matriz.sum(axis=0)):.4f}\n")
        f.write(f"Kappa de Cohen: {kappa:.3f}\n")
        f.write(f"Error estandar: {se:.4f}\n")
        f.write(f"IC95%: [{max(lo, -1.0):.3f}, {min(hi, 1.0):.3f}]\n")
        f.write(f"Interpretacion (Landis & Koch 1977): {interpretar(kappa)}\n")

    plot(matriz, rango, cats, n, out / "grafico_kappa.png")

    print(f"Kappa = {kappa:.3f}  IC95% = [{max(lo, -1.0):.3f}, {min(hi, 1.0):.3f}]")
    print(f"Acuerdo: {sum(coincidencia)/n:.1%}  ({sum(coincidencia)}/{n})")
    print(f"Salida -> {out}/")


if __name__ == "__main__":
    main()