# Análisis de huérfanos y cadenas rotas de trazabilidad

**Proyecto:** ACERS / AgroMoreira
**Versión:** 1.0 — 2026-09-05
**Artefacto analizado:** `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx` (66 filas × 13 columnas)
**Script de verificación:** `04_Trazabilidad/verificar_trazabilidad.py`

---

## 1. Qué se considera huérfano y qué cadena rota

La matriz encadena, para cada requisito, ocho eslabones: evidencia de elicitación → requisito →
caso de uso → historia de usuario → criterio de aceptación → componente → maqueta → caso de
prueba. Sobre esa estructura se definen tres defectos posibles:

| Defecto | Definición operativa |
|---|---|
| **Cadena rota** | Una fila con al menos un eslabón vacío: el rastro se interrumpe a mitad de camino |
| **Huérfano hacia adelante** | Un requisito especificado en el ERS que no tiene fila en la matriz: existe pero no se traza |
| **Huérfano hacia atrás** | Un identificador en la matriz que no corresponde a ningún requisito del ERS: se traza algo que no existe |

Se añade una cuarta comprobación de cobertura: casos de uso especificados en el paquete de
modelado que no aparecen en ninguna fila.

## 2. Método

La verificación **no se hizo leyendo la matriz a ojo**. Se automatizó en
`04_Trazabilidad/verificar_trazabilidad.py`, que lee los tres artefactos primarios —la matriz, el
ERS y la especificación de casos de uso— y contrasta los identificadores entre ellos. El script
es reproducible con una sola orden y devuelve código de salida 1 si encuentra un hallazgo
bloqueante:

```bash
python3 04_Trazabilidad/verificar_trazabilidad.py
```

## 3. Resultado

Ejecución del 2026-09-05 sobre el estado actual del repositorio:

| Comprobación | Resultado |
|---|---|
| Cadenas rotas (celdas vacías en cualquier eslabón) | **0** |
| Requisitos del ERS sin fila en la matriz | **0** (60 requisitos trazados: 39 RF + 21 RNF) |
| Identificadores en la matriz sin requisito en el ERS | **0** |
| Casos de uso especificados sin fila en la matriz | **0** (15 de 15 trazados) |
| Filas con evidencia de elicitación "Sin evidencia" | 16 de 66 — clasificadas en la Sección 4 |

Las 66 filas se descomponen en 60 filas base, una por requisito, y 6 filas secundarias para los
seis requisitos que dan servicio a un segundo caso de uso además del principal.

## 4. Las 16 filas sin evidencia de elicitación: causa y acción

Que una fila diga "Sin evidencia" en la columna de elicitación **no es una cadena rota**. Es la
consecuencia esperada del enfoque *legal-first* que la guía asigna a este proyecto: un requisito
derivado de una norma no nace de una entrevista, nace del articulado. Registrarlo como "Sin
evidencia" en vez de inventarle un código de entrevista es precisamente lo correcto. Las 16 filas
se agrupan en tres causas distintas, y cada una tiene una acción distinta.

### Causa A — Requisito derivado de norma legal (8 filas, tipo RD)

Su origen es un artículo, no un informante. La trazabilidad hacia atrás existe y es más fuerte
que una cita de entrevista: apunta al texto legal, verificable por cualquiera.

| Requisito | Norma y artículo | Objetivo |
|---|---|---|
| RF-22 | LOPDP, Art. 4, 8, 10(d), 12 | Consentimiento del trabajador para el tratamiento de sus datos |
| RF-23 | LOPDP, Art. 10(i), 13-19, 33, 36 | Derechos ARCO+ del trabajador |
| RF-24 | Res. AGROCALIDAD 183, Art. 33-34 | Certificado de salud del trabajador |
| RF-25 | Res. AGROCALIDAD 183, Art. 39-43 | Certificación BPA ante AGROCALIDAD |
| RF-36 | Res. AGROCALIDAD 183, Art. 18(e) | Capacitación en manejo de plaguicidas y primeros auxilios |
| RF-37 | Res. AGROCALIDAD 0072, Art. 3.6.1(a) | Aviso de síntomas sospechosos de plaga cuarentenaria |
| RF-38 | Res. AGROCALIDAD 0072, Art. 3.6.1(d) | Bitácora de bioseguridad de entrada y salida |
| RF-39 | Res. AGROCALIDAD 0072, Art. 3.6.1(f)(g) | Registros de capacitación fitosanitaria del personal |

**Acción:** ninguna corrección de trazabilidad. Se mantiene "Sin evidencia" como valor correcto y
se deja constancia aquí de que la fuente es el artículo citado en la propia fila. Estos ocho
requisitos son, además, el objeto del estudio empírico: son parte de los criterios de cobertura
legal que el componente empírico mide, y su ausencia de evidencia de elicitación **es el hallazgo
del estudio**, no un defecto de la matriz.

### Causa B — Requisito no funcional derivado de norma (2 filas)

| Requisito | Norma y artículo | Objetivo |
|---|---|---|
| RNF-09 | LOPDP, Art. 37, 41 | Seguridad de los datos personales almacenados |
| RNF-12 | Res. AGROCALIDAD 183, Art. 38 | Retención mínima de registros de trazabilidad (2 años) |

**Acción:** ninguna corrección. Igual que la causa A: la fuente es el artículo, y así consta en la
fila.

### Causa C — Atributo de calidad del componente de IA, especificado por el equipo (6 filas)

| Requisito | Objetivo |
|---|---|
| RNF-16 | Desempeño de detección/predicción del modelo |
| RNF-17 | Explicabilidad de las recomendaciones |
| RNF-18 | Equidad de desempeño entre cultivos |
| RNF-19 | Supervisión humana obligatoria |
| RNF-20 | Monitoreo continuo del desempeño en producción |
| RNF-21 | Clasificación de riesgo de las recomendaciones |

Estos seis no derivan de una entrevista ni de un artículo citado directamente en la fila: son
atributos de calidad que el equipo especificó para el componente de IA.

**Acción aplicada:** su fundamento se documentó en `01_ERS/Clasificacion_Riesgo_IA.md`, que
enlaza cada uno con la norma que lo respalda —el Art. 20 de la LOPDP para RNF-17 y RNF-19, la
Res. AGROCALIDAD 0072 y la 183 para RNF-21 y RNF-20, y el Anexo A13 del paquete ético para
RNF-16 y RNF-18— y con un plan de monitoreo con umbral, frecuencia y responsable. Con eso su
origen deja de ser "especificación del equipo" sin más y queda anclado.

## 5. Conclusión

La matriz no tiene huérfanos ni cadenas rotas: los 60 requisitos del ERS y los 15 casos de uso
están trazados, y ninguna fila deja un eslabón vacío. Las 16 filas sin evidencia de elicitación
están clasificadas por causa, con su acción, y ninguna de ellas es un defecto de trazabilidad:
ocho son requisitos derivados de norma, dos son requisitos no funcionales derivados de norma, y
seis son atributos de calidad del componente de IA cuyo fundamento normativo quedó documentado.

Esta conclusión es reproducible: cualquier evaluador puede ejecutar
`python3 04_Trazabilidad/verificar_trazabilidad.py` sobre un clon limpio y obtener el mismo
informe.
