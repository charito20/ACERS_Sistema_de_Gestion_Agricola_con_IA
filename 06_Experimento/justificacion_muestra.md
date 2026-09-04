# Justificación del tamaño de muestra y del número de personas evaluadoras

**Autora:** María del Rosario Escudero Plaza
**Fecha de elaboración:** Antes de la ejecución del análisis estadístico (pre-registrado)
**Proyecto:** ACERS - Sistema de Gestión Agrícola con IA para cacao y plátano verde

---

## 1. Unidades de análisis: 26 criterios legales

El estudio compara la proporción de criterios cubiertos antes y después de aplicar el enfoque legal-first sobre **26 criterios de cumplimiento legal** (C1–C26), organizados en tres bloques normativos:

| Bloque | Criterios | Norma de referencia |
|---|---|---|
| LOPDP | C1–C13 (13 criterios) | Ley Orgánica de Protección de Datos Personales del Ecuador |
| BPA cacao | C14–C20 (7 criterios) | Resolución 183 de AGROCALIDAD |
| Bioseguridad | C21–C26 (6 criterios) | Resolución 0072 de AGROCALIDAD |

**Justificación del número 26:** Los 26 criterios se derivan del articulado de las tres normas identificadas como aplicables a Agrícola Moreira. Cada criterio corresponde a una obligación o derecho verificable del texto legal, documentado en `01_ERS/Modelo_Legal_LOPDP.md`. No se artificialmente infló ni redujo el número de criterios: es el conjunto completo de obligaciones relevantes para un sistema de gestión agrícola que maneja datos personales de trabajadores y trazabilidad de cultivos.

## 2. Diseño muestral: comparación pareada

El diseño es una **comparación de proporciones pareadas** sobre las mismas 26 unidades (criterios). Cada criterio se evalúa en dos momentos:
- **Momento 1 (antes):** cobertura por los RF y RNF elicitados con métodos convencionales
- **Momento 2 (después):** cobertura tras aplicar el enfoque legal-first

Al ser datos pareados (mismas 26 unidades evaluadas dos veces), la unidad de análisis es el criterio legal, no el participante. La prueba estadística apropiada es la **prueba de McNemar** para datos binarios pareados.

## 3. Potencia estadística

### 3.1 Cálculo a priori

Para la prueba de McNemar con datos binarios pareados:
- **Nivel de significancia (α):** 0.05
- **Potencia deseada (1 − β):** 0.80
- **Tamaño del efecto esperado:** La literatura sobre enfoque legal-first (Amaral et al., 2021) reporta incrementos de cobertura del 30% al 50% en obligaciones legales. Se asumió un efecto conservador del 30% (proporción de discordancia esperada b/(b+c) ≈ 0.30).

Con estos parámetros, el cálculo de potencia para McNemar indica que **26 unidades son suficientes** para detectar un efecto del 30% con potencia ≥ 0.80 al nivel α = 0.05.

### 3.2 Resultado observado

El análisis ejecutó la prueba de McNemar sobre los 26 criterios y obtuvo:
- **χ² = 16.056, p < 0.0001**
- Discordancia: 18 criterios cubiertos solo después del legal-first, 0 cubiertos solo antes
- Diferencia de proporciones: 0.692 (IC95% por bootstrap: [0.500, 0.846])

El efecto observado (diferencia de 69.2 puntos porcentuales) supera con creces el 30% asumido a priori, lo que confirma que el tamaño de muestra fue adecuado.

## 4. Número de personas evaluadoras

### 4.1 Evaluación de la cobertura legal

La evaluación de si cada criterio legal está cubierto por un requisito funcional o no funcional fue realizada por:
- **Evaluador primario:** María del Rosario Escudero Plaza (responsable del registro OSF y del análisis estadístico)
- **Evaluador secundario independiente:** Kamila Annabella Calle Delgado (verificación cruzada)

**Justificación de 2 evaluadores:** La evaluación de cobertura legal es una tarea de juicio experto donde se determina si un requisito verificable y medible satisface un criterio legal. Con dos evaluadores independientes se puede calcular el acuerdo inter-evaluador (kappa) y resolver discrepancias por discusión, siguiendo la práctica estándar en estudios de cobertura de requisitos (Amaral et al., 2021; Breaux y Antón, 2008).

### 4.2 Evaluación de la evidencia de campo

Las entrevistas y sesiones de validación fueron conducidas por los siguientes miembros del equipo:

**Entrevistas (17 totales):**
- María Escudero: 6 entrevistas
- Jeanpierre Robinson: 8 entrevistas
- Roselyn Sánchez: 2 entrevistas
- Sin atribuir en este documento: 1 entrevista (el conteo de 17 se verificó contra 17 audios y 17 consentimientos firmados; el desglose por integrante de esta última entrevista queda pendiente de confirmar)

**Walkthroughs / sesiones de validación (9 totales):**
- María Escudero: 4 walkthroughs
- Robinson Espinoza: 5 walkthroughs

**Total: 17 entrevistas + 9 walkthroughs = 26 sesiones de campo**

**Justificación del número de participantes de campo:** El criterio de saturación se alcanzó cuando dos sesiones consecutivas no aportaron requisitos nuevos. La curva de saturación (`02_Evidencias/Codificacion_Tematica/curva_saturacion.csv`) muestra estabilización a partir de la sesión 14, lo que confirma que 17 entrevistas fueron suficientes para el dominio estudiado.

> **Nota de reconciliación (2026-09-04):** este documento y `06_Experimento/protocolo.tex` corrigieron el conteo de 16 a 17 entrevistas tras verificar que hay 17 audios y 17 consentimientos firmados. Sigue pendiente confirmar con el equipo si los 9 walkthroughs son sesiones separadas de las 17 entrevistas (como se trata en este documento) o si son un subconjunto de ellas, como sugiere el manuscrito final y el ERS/SRS (que asignan 7 de los 17 códigos ENTR también como walkthrough). Mientras no se confirme, ambas cifras (25 aquí, 17 en el manuscrito) deben tratarse como no reconciliadas.

## 5. Referencias

- Amaral et al. (2021). Conceptual model for compliance verification. *Requirements Engineering*.
- Breaux y Antón (2008). Engineering privacy requirements. *RE*.
- McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions. *Psychometrika*.
