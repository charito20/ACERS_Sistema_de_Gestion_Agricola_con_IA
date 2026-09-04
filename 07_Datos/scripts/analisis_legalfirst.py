#!/usr/bin/env python3
"""
analisis_legalfirst.py - McNemar para Enfoque 2 legal-first
26 criterios C1-C26 pareados antes/después. Repo real: Modelo_Legal_LOPDP.md + Matriz_Trazabilidad_v2.xlsx

Versión para el paquete de datos 07_Datos/: lee de datos_crudos/ y
persiste todas sus salidas en resultados/ (no solo imprime en consola).
"""
import os
import argparse
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # modo headless para generar figuras sin display
import matplotlib.pyplot as plt
from statsmodels.stats.contingency_tables import mcnemar

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(RAIZ, "datos_crudos")
RESUL = os.path.join(RAIZ, "resultados")


def cargar_cobertura(path=None):
    if path is None:
        path = os.path.join(DATA, "cobertura_legal.csv")
    return pd.read_csv(path, sep=";")


def mcnemar_test(df):
    # tabla 2x2: [[a,b],[c,d]] donde a=00, b=01, c=10, d=11
    a = ((df.cubierto_convencional == 0) & (df.cubierto_legalfirst == 0)).sum()
    b = ((df.cubierto_convencional == 0) & (df.cubierto_legalfirst == 1)).sum()
    c = ((df.cubierto_convencional == 1) & (df.cubierto_legalfirst == 0)).sum()
    d = ((df.cubierto_convencional == 1) & (df.cubierto_legalfirst == 1)).sum()
    table = [[int(a), int(b)], [int(c), int(d)]]
    res = mcnemar(table, exact=False, correction=True)
    return {"tabla": table, "stat": res.statistic, "p": res.pvalue, "b": int(b), "c": int(c)}


def bootstrap_diff(df, n=10000):
    rng = np.random.default_rng(42)
    diffs = []
    idx = df.index.to_numpy()
    for _ in range(n):
        s = df.sample(n=len(df), replace=True, random_state=rng)
        diffs.append(s.cubierto_legalfirst.mean() - s.cubierto_convencional.mean())
    return np.percentile(diffs, [2.5, 97.5])


def cobertura_long_csv(df, path):
    """Transforma la tabla ancha (una columna por metodo) a formato largo
    (una fila por criterio-metodo). Esta es la version 'procesada' que se
    usa como insumo intermedio antes de los descriptivos y la figura."""
    largo = df.melt(
        id_vars=[c for c in df.columns if c not in ("cubierto_convencional", "cubierto_legalfirst")],
        value_vars=["cubierto_convencional", "cubierto_legalfirst"],
        var_name="metodo",
        value_name="cubierto",
    )
    largo["metodo"] = largo["metodo"].str.replace("cubierto_", "", regex=False)
    largo.to_csv(path, index=False, sep=";")
    return largo


def ic_bootstrap_csv(df, ci, path, n=10000):
    diff = df.cubierto_legalfirst.mean() - df.cubierto_convencional.mean()
    pd.DataFrame([{
        "estimador": "diferencia_cobertura",
        "valor": float(diff),
        "ic_inf": float(ci[0]),
        "ic_sup": float(ci[1]),
        "n_replicas": int(n),
        "seed": 42,
        "metodo": "percentil bootstrap",
    }]).to_csv(path, index=False, sep=";")


def tabla_mcnemar_csv(r, path):
    pd.DataFrame([{
        "estadistico": "McNemar chi2",
        "valor": r["stat"],
        "p": r["p"],
        "b": r["b"],
        "c": r["c"],
        "tabla_2x2": str(r["tabla"]),
    }]).to_csv(path, index=False, sep=";")


def descriptivos_bloque_csv(df, path):
    desc = df.groupby("bloque")[["cubierto_convencional", "cubierto_legalfirst"]].agg(
        ["mean", "count", "sum"]
    )
    desc.columns = [f"{a}_{b}" for a, b in desc.columns]
    desc = desc.reset_index()
    desc["cobertura_convencional_pct"] = desc["cubierto_convencional_sum"] / desc["cubierto_convencional_count"] * 100
    desc["cobertura_legalfirst_pct"] = desc["cubierto_legalfirst_sum"] / desc["cubierto_legalfirst_count"] * 100
    desc.to_csv(path, index=False, sep=";")


def figura_curva(df, path):
    por_bloque = df.groupby("bloque")[["cubierto_convencional", "cubierto_legalfirst"]].mean()
    x = np.arange(len(por_bloque))
    w = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - w / 2, por_bloque["cubierto_convencional"], w, label="Convencional")
    ax.bar(x + w / 2, por_bloque["cubierto_legalfirst"], w, label="Legal-first")
    ax.set_xticks(x)
    ax.set_xticklabels(por_bloque.index)
    ax.set_ylabel("Cobertura (proporción)")
    ax.set_title("Cobertura de criterios por bloque normativo (antes/después)")
    ax.legend()
    ax.set_ylim(0, 1.05)
    fig.tight_layout()
    fig.savefig(path, dpi=150, metadata={"Software": "matplotlib", "Creator": "ACERS"})
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description="Análisis legal-first (Enfoque 2) para 07_Datos")
    ap.add_argument("--data-dir", default=DATA, help="Ruta a datos_crudos/")
    ap.add_argument("--out-dir", default=RESUL, help="Ruta a resultados/")
    ap.add_argument("--proc-dir", default=os.path.join(RAIZ, "datos_procesados"), help="Ruta a datos_procesados/")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    os.makedirs(args.proc_dir, exist_ok=True)

    df = cargar_cobertura(os.path.join(args.data_dir, "cobertura_legal.csv"))

    # Paso de procesamiento: tabla ancha -> formato largo, insumo para los pasos siguientes
    cobertura_long_csv(df, os.path.join(args.proc_dir, "cobertura_legal_long.csv"))

    r = mcnemar_test(df)
    ci = bootstrap_diff(df)

    # Persistir salidas
    tabla_mcnemar_csv(r, os.path.join(args.out_dir, "tabla_mcnemar.csv"))
    descriptivos_bloque_csv(df, os.path.join(args.out_dir, "descriptivos_bloque.csv"))
    ic_bootstrap_csv(df, ci, os.path.join(args.out_dir, "ic_bootstrap.csv"))
    figura_curva(df, os.path.join(args.out_dir, "curva_o_barras.png"))

    # Reporte en consola (para inspección)
    print(f"Tabla 2x2: {r['tabla']}")
    print(f"McNemar chi2={r['stat']:.3f} p={r['p']:.4f} b={r['b']} c={r['c']}")
    print(f"Diferencia cobertura: {df.cubierto_legalfirst.mean()-df.cubierto_convencional.mean():.3f} IC95% {ci}")
    print(f"Salidas persistidas en {args.out_dir}/")


if __name__ == "__main__":
    main()