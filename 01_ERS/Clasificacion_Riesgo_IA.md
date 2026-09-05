# Clasificación de riesgo del componente de IA, base legal y plan de monitoreo

**Proyecto:** ACERS / AgroMoreira — Sistema de Gestión Agrícola de Verde y Cacao con IA
**Versión:** 1.0 — 2026-09-05
**Documentos de los que depende:** `01_ERS/ERS_SRS_2B_v2.0.md` (RF-09, RF-10, RNF-16 a RNF-21),
`01_ERS/Modelo_Legal_LOPDP.md`, `01_ERS/Matriz_Obligacion_Legal.md`,
`08_Etica/A13_Protocolo_IA_Verde_Cacao.pdf`, `08_Etica/A11_Analisis_Riesgos_AgricolaMoreira.pdf`

---

## 1. Alcance y estado real del componente

El componente de inteligencia artificial del sistema está **especificado, no desplegado**. Esta
distinción condiciona todo lo que sigue y se declara aquí de forma expresa para no atribuir al
sistema propiedades que hoy no tiene.

| Elemento | Estado verificable |
|---|---|
| RF-09 — Alerta de plaga/enfermedad asistida por IA con verificación humana obligatoria | Especificado (Must have). Fuera del MVP actual |
| RF-10 — Diagnóstico de plagas por imagen | Especificado (Could have). Fuera del MVP actual |
| RNF-16 a RNF-21 — atributos de calidad del componente de IA | Especificados con métrica, unidad y umbral |
| Modelo entrenado | **No existe.** No hay pesos, ni conjunto de entrenamiento, ni tarjeta de modelo |

En consecuencia, este documento clasifica el riesgo **del componente tal como está especificado** y
fija las condiciones que deben cumplirse *antes* de que exista un modelo en producción. Los campos
de la tarjeta de modelo del Anexo A13 (tipo de modelo, procedencia y licencia de los datos de
entrenamiento, métricas obtenidas) permanecen deliberadamente sin llenar: llenarlos hoy sería
declarar resultados de un modelo que no se ha construido.

## 2. Marco de clasificación adoptado

La clasificación se hace en dos niveles complementarios, porque responden a preguntas distintas:

**Nivel A — Riesgo del sistema como tratamiento de datos.** Se conserva la clasificación del
protocolo de investigación y del Anexo A13: **Categoría C, riesgo mínimo operativo**. El
fundamento es verificable: el componente de IA opera sobre material vegetal (hojas, frutos,
mazorcas) y sobre datos operativos de la finca (rendimiento, fechas, insumos). No procesa datos
clínicos ni biométricos de personas, y el Anexo A13 declara formalmente que no se capturarán,
procesarán ni almacenarán imágenes, videos ni datos biométricos de personas reales.

**Nivel B — Riesgo por tipo de recomendación.** Es la clasificación que exige RNF-21 y la que
faltaba desarrollar. El criterio es el **impacto de seguir la recomendación sin verificarla**,
medido en tres dimensiones: consecuencia agronómica y económica para la unidad productiva,
consecuencia sanitaria para el cultivo y terceros, y consecuencia legal o regulatoria.

| Nivel | Definición operativa |
|---|---|
| **Alto** | Seguir la recomendación sin verificar puede causar daño económico o fitosanitario difícilmente reversible, o incumplir una obligación regulatoria |
| **Medio** | Puede causar pérdida económica acotada o trabajo innecesario, reversible en el ciclo productivo |
| **Bajo** | El error se traduce en ruido informativo o en una tarea desestimada, sin consecuencia material |

## 3. Clasificación por tipo de recomendación (cumple RNF-21)

| # | Tipo de recomendación | Requisito | Nivel | Justificación del nivel | Control obligatorio |
|---|---|---|---|---|---|
| A-01 | Sugerencia de aplicación fitosanitaria derivada de una alerta de plaga o enfermedad | RF-09 | **Alto** | Una aplicación innecesaria implica costo de insumo, residuo en el producto y riesgo de resistencia; una omisión permite la propagación. El Anexo A13 identifica explícitamente la "aplicación innecesaria de fitosanitarios" como riesgo económico | Confirmación humana explícita (RNF-19) + factor explicativo visible (RNF-17) + etiqueta de nivel de riesgo visible (RNF-21) |
| A-02 | Sospecha de plaga cuarentenaria (Moko, Sigatoka Negra, Moniliasis, Escoba de Bruja) | RF-09, RF-37 | **Alto** | Activa una obligación de aviso ante la autoridad (Art. 3.6.1(a) Res. AGROCALIDAD 0072). Un falso negativo tiene consecuencia regulatoria además de sanitaria | Confirmación de un perfil técnico antes de emitir el aviso; el sistema no notifica a la autoridad por sí mismo |
| A-03 | Diagnóstico de plaga/enfermedad a partir de imagen | RF-10 | **Alto** | Es la entrada de A-01: si el diagnóstico por imagen se toma como definitivo, arrastra la decisión de aplicación | Mismo flujo de confirmación humana que RF-09, declarado en el propio RF-10. Se presenta siempre como sugerencia |
| A-04 | Recomendación de ventana de cosecha | RF-05, RF-09 | **Medio** | Una ventana mal recomendada afecta calidad y precio del lote, pero el daño se acota al ciclo | Confirmación humana; el sistema muestra los datos que sustentan la ventana |
| A-05 | Alerta de bajo stock de insumos derivada de consumo estimado | RF-08 | **Bajo** | Un falso positivo genera una compra anticipada; un falso negativo, un desabastecimiento detectable por inventario | Revisión en pantalla de inventario antes de comprar |
| A-06 | Sugerencia de priorización de tareas por lote | RF-11 | **Bajo** | Reordena trabajo, no compromete el cultivo | El responsable puede reasignar libremente |

**Regla transversal:** ninguna recomendación de nivel Alto puede ejecutarse sobre los datos del
sistema sin confirmación explícita de una persona (RNF-19, umbral: 0 acciones automáticas). Para
los niveles Alto, la confirmación debe provenir de un perfil con competencia técnica
(administrador de finca o técnico agrónomo), no de cualquier usuario autenticado.

## 4. Base legal aplicable

| Norma y artículo | Qué obliga | Cómo lo cumple el sistema |
|---|---|---|
| **LOPDP, Art. 20** — derecho a no ser objeto de una decisión basada única o parcialmente en valoraciones automatizadas | El titular puede exigir explicación motivada de cualquier sugerencia del sistema, conocer los datos usados e impugnarla | Es la base legal directa de la explicabilidad: RNF-17 exige que el 100% de las alertas muestre al menos un factor que la motivó; RF-33 habilita la vía de impugnación (bandeja de sugerencias); RNF-19 garantiza que ninguna decisión se ejecuta sin persona |
| **LOPDP, Art. 7 y 8** — licitud y consentimiento | Base de licitud del tratamiento | Los datos operativos de la finca se tratan bajo el aval de la unidad productiva (C1); no hay datos personales en el flujo del componente de IA |
| **LOPDP, Art. 10 lit. e** — pertinencia y minimización | Solo los datos estrictamente necesarios | El componente consume datos del lote e histórico de tratamientos; no incorpora datos personales de trabajadores |
| **LOPDP, Art. 10 lit. j** — seguridad | Medidas técnicas de protección | Cifrado AES-256 de la zona restringida de evidencias |
| **Res. AGROCALIDAD 0072, Art. 3.6.1(a)** — aviso ante síntomas sospechosos de plaga cuarentenaria | Obligación de notificar | A-02 clasificada como Alto; el aviso lo emite una persona, no el modelo |
| **Res. AGROCALIDAD 183, Art. 39-43** — Buenas Prácticas Agrícolas | Registro y trazabilidad de aplicaciones | Toda alerta y su resolución (confirmada, descartada, disputada) queda registrada (RNF-20), lo que produce el rastro exigido |
| **Anexo A13 (protocolo de IA del PFC)** | Human-in-the-loop, no despliegue sin validación de campo, tarjeta de modelo | Recogido en RNF-19 y en la condición de habilitación de la Sección 5 |

**Nota de alcance honesta:** el Art. 20 de la LOPDP protege a personas frente a decisiones
automatizadas. En este sistema, las recomendaciones de IA recaen sobre el cultivo, no sobre
personas. El artículo se aplica de forma indirecta pero real en un caso: cuando una alerta deriva
en la asignación de tareas a un trabajador identificado (RF-11), la trazabilidad de esa asignación
sí involucra a una persona. Por eso el derecho a explicación y a impugnación se implementa como
requisito del sistema y no solo como buena práctica.

## 5. Condiciones de habilitación (puerta previa al despliegue)

Ninguna de estas condiciones está cumplida hoy, porque no hay modelo. Se declaran como puerta
verificable:

1. RNF-16 — exactitud ≥80% y sensibilidad ≥75% en el conjunto de validación.
2. RNF-18 — diferencia ≤10 puntos porcentuales en falsos negativos entre cacao y plátano.
3. RNF-21 — 100% de los tipos de alerta con nivel de riesgo asignado y visible (Sección 3 de este documento cubre la asignación; falta la visibilidad en interfaz).
4. Tarjeta de modelo publicada con procedencia y licencia de los datos (Anexo A13, Sección 5).
5. Validación de campo supervisada por el ingeniero agrónomo de la finca (Anexo A13, punto 4.4).

## 6. Plan de monitoreo en producción

| Indicador | Métrica y umbral | Fuente del dato | Frecuencia | Responsable | Acción si se incumple |
|---|---|---|---|---|---|
| Desempeño real del modelo | Exactitud ≥80%, sensibilidad ≥75%, calculadas sobre alertas confirmadas/descartadas | Registro de resolución de alertas (RNF-20) | Mensual | Técnico agrónomo | Suspender las alertas de nivel Alto y reentrenar antes de rehabilitarlas |
| Cobertura de retroalimentación | ≥90% de alertas con resolución registrada dentro de 7 días | Registro de alertas | Semanal | Administrador de finca | Recordatorio a los responsables; si persiste 2 semanas, el indicador de desempeño se declara no confiable |
| Explicabilidad efectiva | 100% de alertas emitidas con al menos un factor explicativo | Auditoría de la interfaz sobre muestra de alertas | Mensual | Equipo técnico | Bloquear la emisión de alertas sin factor explicativo |
| Supervisión humana | 0 acciones aplicadas automáticamente sin confirmación | Bitácora del sistema | Continuo, revisión mensual | Equipo técnico | Incidente de seguridad: revertir la acción y corregir el flujo |
| Equidad entre cultivos | Diferencia ≤10 pp en falsos negativos cacao vs. plátano | Registro de resolución segmentado por cultivo | Trimestral | Técnico agrónomo | Reentrenar con refuerzo del cultivo desfavorecido |
| Deriva del contexto | Variación >20% en la tasa de confirmación respecto del trimestre anterior | Registro de resolución | Trimestral | Técnico agrónomo | Revisar si cambiaron variedades, clima o prácticas; revalidar el modelo |
| Impugnaciones | Toda sugerencia disputada (RF-33) recibe respuesta motivada | Bandeja de sugerencias | Continuo | Administrador de finca | Responder y, si la impugnación es fundada, registrar el caso como error del modelo |

**Registro del monitoreo:** los resultados de cada revisión se anotan con fecha, responsable y
decisión tomada, de modo que el cumplimiento del Art. 20 (explicación motivada) y de la Res. 183
(trazabilidad de aplicaciones) sea auditable a posteriori y no solo declarativo.

## 7. Trazabilidad de este documento

| Sección | Requisito que desarrolla | Norma que lo fundamenta |
|---|---|---|
| 2, Nivel A | Clasificación de categoría del PFC | Anexo A13; protocolo A1 |
| 3 | RNF-21 | Res. 0072 Art. 3.6.1(a); Res. 183 Art. 39-43 |
| 4 | RNF-17, RNF-19 | LOPDP Art. 20, 7, 8, 10(e), 10(j) |
| 5 | RNF-16, RNF-18, RNF-21 | Anexo A13, secciones 4 y 5 |
| 6 | RNF-20, RNF-16, RNF-18 | LOPDP Art. 20; Res. 183 |

## 8. Lo que este documento no resuelve

Se declara de forma expresa para que no se lea como cumplimiento donde no lo hay:

- No hay modelo entrenado, por lo tanto no hay métricas de desempeño reales ni tarjeta de modelo
  completa. Las cifras de la Sección 5 son umbrales de habilitación, no resultados.
- La visibilidad del nivel de riesgo en la interfaz (RNF-21) está especificada y clasificada aquí,
  pero no implementada en el MVP.
- El plan de monitoreo de la Sección 6 es ejecutable solo desde que exista un modelo en operación.
