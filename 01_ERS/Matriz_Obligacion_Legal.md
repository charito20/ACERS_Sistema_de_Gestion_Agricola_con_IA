# Matriz de correspondencia obligación legal → artículo → requisito

Construida a partir de los 26 criterios de cumplimiento legal definidos en
`01_ERS/Modelo_Legal_LOPDP.md` (método legal-first, Amaral et al. 2021) y de los
datos ya calculados y versionados en `07_Datos/datos_crudos/cobertura_legal.csv`
y `07_Datos/resultados/`. Ningún dato de esta matriz es nuevo: es la misma
evaluación de cobertura del manuscrito (Sección de Resultados), presentada aquí
como tabla de trazabilidad legal, tal como pide el reparto de roles del equipo
del 2026-09-02.

Responsable: Danela Arteaga (especificación de requisitos). Revisión independiente: Kamila Calle (gatekeeper P11).

## Bloque 1 — Ley Orgánica de Protección de Datos Personales (LOPDP)

| Criterio | Obligación legal | Artículo | Cubierto (convencional) | Cubierto (legal-first) | Requisito que la cubre |
|---|---|---|---|---|---|
| C1 | Identidad y contacto del responsable del tratamiento (Agrícola Moreira) | Art. 4, 12(8) | No | Sí | RF-22 |
| C2 | Identidad y contacto de cualquier encargado del tratamiento | Art. 4, 34-35 | No | Sí | RF-22 |
| C3 | Finalidad del tratamiento de datos personales | Art. 10(d) | No | Sí | RF-22 |
| C4 | Consentimiento libre, específico, informado e inequívoco | Art. 8 | No | Sí | RF-23 |
| C5 | Categorías de datos personales tratados | Art. 12(5) | No | Sí | RF-22 |
| C6 | Seguridad de datos con medidas técnicas y organizativas | Art. 37, 41 | No | Sí | RNF-08 / RNF-09 |
| C7 | Plazo de conservación y eliminación de datos personales | Art. 10(i) | No | Sí | RF-23 |
| C8 | Transferencia de datos a terceros con garantías | Art. 33, 36 | No | Sí | RF-23 |
| C9 | Notificación de vulneración de seguridad | Art. 43, 46 | No | Sí | RF-23 |
| C10 | Derechos ARCO+ del titular | Art. 13-19 | No | Sí | RF-23 |
| C11 | Delegado de protección de datos (si aplica) | Art. 48 | No | **No cubierto** | Condicional al volumen real de trabajadores/productores — pendiente de fijar con el administrador de la finca (ver nota de alcance en `Modelo_Legal_LOPDP.md`) |
| C12 | Contrato con el encargado del tratamiento | Art. 34-35 | No | Sí | RF-22 |
| C13 | Responsabilidad proactiva y demostrable | Art. 47(2)(3)(14) | No | Sí | RNF-08 |

## Bloque 2 — Trazabilidad agroindustrial (Resolución AGROCALIDAD 183)

| Criterio | Obligación legal | Artículo | Cubierto (convencional) | Cubierto (legal-first) | Requisito que la cubre |
|---|---|---|---|---|---|
| C14 | Registro digital del predio (identificación, croquis, dirección) | Art. 3 | Sí | Sí | RF-03 |
| C15 | Trazabilidad de extremo a extremo del lote | Art. 36 | Sí | Sí | RF-14 |
| C16 | Registro y conservación mínima de 2 años de los 14 tipos documentales | Art. 38 | Sí | Sí | RF-18 |
| C17 | Seguridad y salud del personal de campo | Art. 31-34 | No | Sí | RF-24 |
| C18 | Etiquetado y registro de procedencia por lote | Art. 27 | Sí | Sí | RF-19 |
| C19 | Registro de transporte por embarque | Art. 29 | Sí | Sí | RF-19 |
| C20 | Certificación BPA ante AGROCALIDAD | Art. 39-43 | No | Sí | RF-25 |

## Bloque 3 — Bioseguridad y manejo fitosanitario (Resolución AGROCALIDAD 0072)

| Criterio | Obligación legal | Artículo | Cubierto (convencional) | Cubierto (legal-first) | Requisito que la cubre |
|---|---|---|---|---|---|
| C21 | Análisis de suelo previo a siembra | Art. 8 Res.183 | Sí | Sí | RF-35 |
| C22 | Equipo de protección personal en aplicación de plaguicidas | Art. 18(g) Res.183 | Sí | Sí | RF-18 |
| C23 | Capacitación en manejo de plaguicidas y primeros auxilios | Art. 18(e) Res.183 | No | Sí | RF-36 |
| C24 | Aviso ante síntomas sospechosos de plaga cuarentenaria (Moko) | Art. 3.6.1(a) Res.0072 | No | Sí | RF-37 |
| C25 | Bitácora de bioseguridad de ingreso/salida del predio | Art. 3.6.1(d) Res.0072 | No | Sí | RF-38 |
| C26 | Capacitación fitosanitaria específica del personal | Art. 3.6.1(f)(g) Res.0072 | No | Sí | RF-39 |

## Resumen

25 de los 26 criterios quedan cubiertos tras aplicar el enfoque legal-first (96,2%), frente a 7 de 26 (26,9%) por elicitación convencional — cifras verificadas contra `07_Datos/resultados/tabla_mcnemar.csv` y `descriptivos_bloque.csv`, las mismas que reporta el manuscrito. El único criterio sin cobertura es C11, condicional al volumen real de trabajadores/productores del sistema.

## Vínculo con la matriz de trazabilidad (`04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx`)

Las filas de los 8 requisitos derivados (RF-22 a RF-25, RF-36 a RF-39) ya existen en la matriz de trazabilidad con su Ley/Norma y Artículo. Quedaba pendiente registrar, en esa misma matriz, que RF-01, RF-03, RF-14, RF-18, RF-19 y RF-35 —elicitados originalmente por entrevista— también cubren un criterio legal (cobertura indirecta), y ampliar la cita de artículo de RF-22 y RF-23 a los criterios adicionales que cada uno cubre. Esa corrección ya se aplicó en esta entrega (ver `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx`).
