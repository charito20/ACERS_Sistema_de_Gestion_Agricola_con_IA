# Resultado de la doble codificación (kappa)

Codificadora A: Danela Arteaga. Codificadora B: Kamila Calle. Ambas codificaron, de forma
independiente y sin consultarse, el tema dominante de las mismas 6 entrevistas
(ENTR-01, ENTR-05, ENTR-09, ENTR-12, ENTR-15, ENTR-17), usando el codebook de 12
códigos descrito en `INSTRUCCIONES.md`. El cálculo se hizo con `calcular_kappa.py`
(kappa de Cohen), no a mano.

## Resultado

- Kappa de Cohen: **0.118**
- Acuerdo observado: 16.7% (1 de 6 entrevistas: ambas coincidieron en ENTR-12 = INV)
- Interpretación (Landis & Koch, 1977): **acuerdo leve**

Detalle entrevista por entrevista en `correspondencia_kappa.csv`.

## Interpretación honesta

El acuerdo entre las dos codificadoras fue bajo. Esto no se debe a un error en el
procedimiento — cada una codificó por separado, sin ver el archivo de la otra, y el
cálculo se hizo por script, tal como exige la guía. Un kappa bajo es en sí mismo un
resultado válido de la prueba de confiabilidad, no un fallo que deba ocultarse o
recalcularse hasta que "salga bien".

La causa más probable, revisando las discrepancias, es que la mayoría de las
entrevistas tocan varios temas con peso similar (por ejemplo, plagas, alertas
automáticas y tareas laborales suelen aparecer juntas en una misma entrevista), por
lo que elegir un único "tema dominante" es una decisión inherentemente subjetiva sin
una regla operativa más estricta (por ejemplo, contar minutos u oraciones dedicadas a
cada tema). Esto se documenta como una limitación real del codebook actual, útil para
una futura revisión de los criterios de codificación.

## Archivos de esta carpeta

- `codificador_a.csv`, `codificador_b.csv`: codificación independiente de cada persona.
- `correspondencia_kappa.csv`: tabla de coincidencia entrevista por entrevista.
- `resultado_kappa.txt`: salida completa del script (kappa, error estándar, IC95%).
- `grafico_kappa.png`: gráfico de dispersión de la doble codificación.
