# Resultado de la doble codificación (kappa)

Codificadora A: Danela Arteaga. Codificadora B: Kamila Calle. Las dos codificaron por
separado, sin consultarse, el tema dominante de las 17 entrevistas (ENTR-01 a ENTR-17),
usando el codebook de 12 códigos de `INSTRUCCIONES.md`. El cálculo se hizo con el
script `calcular_kappa.py` (kappa de Cohen), no a mano.

## Ronda piloto (6 entrevistas)

Primero se codificaron solo 6 entrevistas (ENTR-01, ENTR-05, ENTR-09, ENTR-12,
ENTR-15, ENTR-17):

- Kappa de Cohen: 0.250
- Acuerdo observado: 33.3% (2 de 6: ENTR-01 = PLA y ENTR-12 = INV)
- Interpretación (Landis y Koch, 1977): acuerdo aceptable

El intervalo de confianza de esa ronda ([-0.988, 1.000]) cruzaba cero. Con solo 6
entrevistas no se podía distinguir un acuerdo real de uno por casualidad. Por eso se
completó la codificación con las 17 entrevistas.

## Resultado final (17 entrevistas)

- Kappa de Cohen: **0.577**
- Acuerdo observado: **64.7% (11 de 17)**
- Error estándar: 0.2629
- IC95%: **[0.061, 1.000]** (ya no cruza cero)
- Interpretación (Landis y Koch, 1977): **acuerdo moderado**

Detalle entrevista por entrevista en `correspondencia_kappa.csv`. Las 6 entrevistas
donde no coincidieron: ENTR-03 (RCO vs. SAT), ENTR-05 (ALA vs. PLA), ENTR-07 (ALA vs.
PLA), ENTR-09 (ALA vs. TAR), ENTR-15 (RCO vs. SAT) y ENTR-17 (RCD vs. PLA).

## Interpretación honesta

Con las 17 entrevistas el acuerdo subió de aceptable a moderado, y el intervalo de
confianza ya no cruza cero. Esto confirma lo que se sospechaba en la ronda piloto: con
6 entrevistas la muestra era muy chica para medir el acuerdo con precisión.

Las 6 entrevistas donde no coincidieron siguen un patrón parecido al de la ronda
piloto: varias entrevistas tocan más de un tema con peso similar (por ejemplo, plagas,
alertas automáticas y tareas laborales suelen salir juntas en la misma entrevista), así
que elegir un solo tema dominante deja margen de interpretación entre las dos personas.
Esto queda documentado como una limitación del codebook actual, útil si en algún
momento se quiere revisar los criterios de codificación.

## Archivos de esta carpeta

- `codificador_a.csv`, `codificador_b.csv`: codificación independiente de cada persona (17 entrevistas).
- `correspondencia_kappa.csv`: tabla de coincidencia entrevista por entrevista.
- `resultado_kappa.txt`: salida completa del script (kappa, error estándar, IC95%).
- `grafico_kappa.png`: gráfico de dispersión de la doble codificación.
