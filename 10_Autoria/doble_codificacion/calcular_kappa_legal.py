#!/usr/bin/env python3
"""
calcular_kappa_legal.py - Kappa de Cohen para cobertura legal binaria (0/1)

Compara dos codificaciones independientes de los 26 criterios legales (C1-C26)
y calcula kappa de Cohen para cada columna binaria (cubierto_convencional y
cubierto_legalfirst).

Uso:
    python calcular_kappa_legal.py cobertura_legal.csv cobertura_legal_codificador_b.csv

Salida:
    - resultado_kappa_legal.txt
    - grafico_kappa_legal.png
"""
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
    sys.exit("Faltan dependencias: pip install numpy scipy matplotlib")


def leer_columna_binaria(path, columna):
    """Lee una columna binaria (0/1) de un CSV con separador ';'."""
    vals = []
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            v = row[columna].strip()
            vals.append(int(v) if v in ("0", "1") else -1)
    return vals


def kappa_binario(a, b):
    """Kappa de Cohen para datos binarios (0/1)."""
    n = len(a)
    # Tabla 2x2: [[TP, FP], [FN, TN]] donde 1=cubierto, 0=no cubierto
    tp = sum(1 for x, y in zip(a, b) if x == 1 and y == 1)
    tn = sum(1 for x, y in zip(a, b) if x == 0 and y == 0)
    fp = sum(1 for x, y in zip(a, b) if x == 0 and y == 1)
    fn = sum(1 for x, y in zip(a, b) if x == 1 and y == 0)

    p_o = (tp + tn) / n  # acuerdo observado
    p_pos_a = (tp + fn) / n  # prop 1s del codificador A
    p_pos_b = (tp + fp) / n  # prop 1s del codificador B
    p_neg_a = (tn + fp) / n
    p_neg_b = (tn + fn) / n
    p_e = p_pos_a * p_pos_b + p_neg_a * p_neg_b  # acuerdo esperado

    if 1 - p_e == 0:
        return 1.0, 0.0, [[tp, fp], [fn, tn]]

    kappa = (p_o - p_e) / (1 - p_e)

    # Error estándar (varianza de Fleiss)
    var = 0
    p = [[tp/n, fp/n], [fn/n, tn/n]]
    p_i = [p_pos_a, p_neg_a]
    p_j = [p_pos_b, p_neg_b]
    for ii in range(2):
        for jj in range(2):
            pij = p[ii][jj]
            a_val = p_i[ii] + p_j[jj]
            var += pij * (a_val * (1 - p_o) - 2 * (1 - p_o) * (p_e - a_val)) ** 2
    var /= (1 - p_o) ** 2 if (1 - p_o) ** 2 > 0 else 1
    se = float(np.sqrt(max(var, 0)) / np.sqrt(n))

    return float(kappa), se, [[tp, fp], [fn, tn]]


def interpretar(k):
    if k >= 0.81: return "acuerdo casi perfecto"
    if k >= 0.61: return "acuerdo sustancial"
    if k >= 0.41: return "acuerdo moderado"
    if k >= 0.21: return "acuerdo aceptable"
    if k >= 0.00: return "acuerdo leve"
    return "sin acuerdo"


def plot_kappa_binario(matriz, n, kappa_a, kappa_lf, out):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, title, vals in [
        (axes[0], "Convencional", matriz["conv"]),
        (axes[1], "Legal-first", matriz["lf"]),
    ]:
        tp, fp, fn, tn = vals
        data = np.array([[tp, fp], [fn, tn]])
        im = ax.imshow(data, cmap="Blues")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(["No cubierto (0)", "Cubierto (1)"])
        ax.set_yticklabels(["No cubierto (0)", "Cubierto (1)"])
        ax.set_xlabel("Codificador B")
        ax.set_ylabel("Codificador A")
        ax.set_title(f"{title}\nn={n}")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, str(data[i, j]), ha="center", va="center",
                        color="white" if data[i, j] > data.max() / 2 else "black",
                        fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def main():
    if len(sys.argv) < 3:
        sys.exit("Uso: python calcular_kappa_legal.py cod_a.csv cod_b.csv")

    path_a = sys.argv[1]
    path_b = sys.argv[2]

    # Leer ambas codificaciones
    conv_a = leer_columna_binaria(path_a, "cubierto_convencional")
    conv_b = leer_columna_binaria(path_b, "cubierto_convencional")
    lf_a = leer_columna_binaria(path_a, "cubierto_legalfirst")
    lf_b = leer_columna_binaria(path_b, "cubierto_legalfirst")

    n = len(conv_a)
    if len(conv_b) != n or len(lf_a) != n or len(lf_b) != n:
        sys.exit("Los archivos tienen distinto número de filas")

    # Calcular kappa para cada columna
    kappa_conv, se_conv, mat_conv = kappa_binario(conv_a, conv_b)
    kappa_lf, se_lf, mat_lf = kappa_binario(lf_a, lf_b)

    lo_c, hi_c = kappa_conv - 1.96 * se_conv, kappa_conv + 1.96 * se_conv
    lo_l, hi_l = kappa_lf - 1.96 * se_lf, kappa_lf + 1.96 * se_lf

    # Calcular kappa promedio (macro)
    kappa_prom = (kappa_conv + kappa_lf) / 2

    # Acuerdo observado (% de criterios donde ambos coinciden exactamente)
    coinciden_conv = sum(1 for a, b in zip(conv_a, conv_b) if a == b)
    coinciden_lf = sum(1 for a, b in zip(lf_a, lf_b) if a == b)
    coinciden_total = sum(1 for a, b, c, d in zip(conv_a, conv_b, lf_a, lf_b)
                          if a == b and c == d)

    out_dir = Path("10_Autoria/doble_codificacion")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Guardar resultado
    with open(out_dir / "resultado_kappa_legal.txt", "w", encoding="utf-8") as f:
        f.write("Kappa de Cohen — Cobertura legal binaria (26 criterios C1-C26)\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Criterios evaluados: {n}\n")
        f.write(f"Codificador A: (original de cobertura_legal.csv)\n")
        f.write(f"Codificador B: (segunda codificación independiente)\n\n")
        f.write("--- Convencional (antes del enfoque legal-first) ---\n")
        f.write(f"  Kappa:    {kappa_conv:.3f}\n")
        f.write(f"  IC95%:    [{max(lo_c, -1):.3f}, {min(hi_c, 1):.3f}]\n")
        f.write(f"  Po:       {coinciden_conv}/{n} = {coinciden_conv/n:.1%}\n")
        f.write(f"  Interpretación: {interpretar(kappa_conv)}\n\n")
        f.write("--- Legal-first (después del enfoque) ---\n")
        f.write(f"  Kappa:    {kappa_lf:.3f}\n")
        f.write(f"  IC95%:    [{max(lo_l, -1):.3f}, {min(hi_l, 1):.3f}]\n")
        f.write(f"  Po:       {coinciden_lf}/{n} = {coinciden_lf/n:.1%}\n")
        f.write(f"  Interpretación: {interpretar(kappa_lf)}\n\n")
        f.write(f"Kappa promedio (macro): {kappa_prom:.3f}\n")
        f.write(f"Coincidencia total (ambas columnas): {coinciden_total}/{n} = {coinciden_total/n:.1%}\n")

    # Guardar gráfico
    plot_kappa_binario(
        {"conv": mat_conv, "lf": mat_lf}, n, kappa_conv, kappa_lf,
        out_dir / "grafico_kappa_legal.png"
    )

    # Guardar correspondencia fila a fila
    with open(out_dir / "correspondencia_kappa_legal.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["criterio", "bloque",
                     "conv_A", "conv_B", "conv_match",
                     "lf_A", "lf_B", "lf_match"])
        for i in range(n):
            # Leer bloque del CSV original
            with open(path_a, encoding="utf-8-sig") as fa:
                reader = csv.DictReader(fa, delimiter=";")
                rows_a = list(reader)
            bloque = rows_a[i].get("bloque", "")
            w.writerow([
                f"C{i+1}", bloque,
                conv_a[i], conv_b[i], 1 if conv_a[i] == conv_b[i] else 0,
                lf_a[i], lf_b[i], 1 if lf_a[i] == lf_b[i] else 0,
            ])

    print(f"Kappa convencional: {kappa_conv:.3f}  IC95% [{max(lo_c,-1):.3f}, {min(hi_c,1):.3f}]")
    print(f"Kappa legal-first:  {kappa_lf:.3f}  IC95% [{max(lo_l,-1):.3f}, {min(hi_l,1):.3f}]")
    print(f"Kappa promedio:     {kappa_prom:.3f}")
    print(f"Acuerdo total:      {coinciden_total}/{n} = {coinciden_total/n:.1%}")
    print(f"\nSalidas en {out_dir}/")


if __name__ == "__main__":
    main()
