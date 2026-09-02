#!/usr/bin/env python3
"""
analisis_legalfirst.py - McNemar para Enfoque 2 legal-first
26 criterios C1-C26 pareados antes/después. Repo real: Modelo_Legal_LOPDP.md + Matriz_Trazabilidad_v2.xlsx
"""
import pandas as pd
from statsmodels.stats.contingency_tables import mcnemar
import numpy as np

def cargar_cobertura(path="06_Experimento/resultados/cobertura_legal.csv"):
    return pd.read_csv(path, sep=";")

def mcnemar_test(df):
    # tabla 2x2: [[a,b],[c,d]] donde a=00, b=01, c=10, d=11
    a = ((df.cubierto_convencional==0) & (df.cubierto_legalfirst==0)).sum()
    b = ((df.cubierto_convencional==0) & (df.cubierto_legalfirst==1)).sum()
    c = ((df.cubierto_convencional==1) & (df.cubierto_legalfirst==0)).sum()
    d = ((df.cubierto_convencional==1) & (df.cubierto_legalfirst==1)).sum()
    table = [[a,b],[c,d]]
    res = mcnemar(table, exact=False, correction=True)
    return {"tabla": table, "stat": res.statistic, "p": res.pvalue, "b": b, "c": c}

def bootstrap_diff(df, n=10000):
    diffs=[]
    for _ in range(n):
        s=df.sample(frac=1, replace=True)
        diffs.append(s.cubierto_legalfirst.mean() - s.cubierto_convencional.mean())
    return np.percentile(diffs, [2.5,97.5])

if __name__=="__main__":
    df=cargar_cobertura()
    r=mcnemar_test(df)
    ci=bootstrap_diff(df)
    print(f"Tabla 2x2: {r['tabla']}")
    print(f"McNemar chi2={r['stat']:.3f} p={r['p']:.4f} b={r['b']} c={r['c']}")
    print(f"Diferencia cobertura: {df.cubierto_legalfirst.mean()-df.cubierto_convencional.mean():.3f} IC95% {ci}")
    print(f"Por bloque:")
    print(df.groupby("bloque")[["cubierto_convencional","cubierto_legalfirst"]].mean())
