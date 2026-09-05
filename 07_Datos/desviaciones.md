# Desviaciones del protocolo respecto del registro OSF

Este archivo documenta las desviaciones del análisis efectivo respecto del
protocolo pre-registrado en el OSF, requeridas por la práctica transparente y por
la rúbrica de la Entrega 4 (2B).

## Desviación 1: Inicio del trabajo de campo antes del registro formal en OSF

**Descripción:** Parte del trabajo de campo de elicitación comenzó antes del
registro formal en OSF, como trabajo exploratorio de entregas anteriores del curso
(Entregas 1A a 3/2A).

**Razón:** El componente empírico se construyó de forma incremental a lo largo del
ciclo del proyecto; la elicitación inicial con informantes de la finca Agrícola
Moreira se realizó en las primeras entregas, antes de formalizar el protocolo en el
OSF.

**Momento en que se detectó:** Durante la preparación del registro OSF en la
Entrega 3 (2A).

**Mitigación aplicada:** El plan de análisis completo (tabla pareada de los 26
criterios, estadísticos descriptivos, prueba de McNemar, bootstrap) se registró en
el OSF antes de la evaluación formal de la cobertura legal. Ninguna decisión de
análisis se tomó a partir de resultados preliminares.

## Desviación 2: El enfoque metodológico pasó por dos formulaciones previas

**Descripción:** El enfoque metodológico del componente empírico pasó por dos
formulaciones previas antes de fijarse en el diseño *legal-first*.

**Razón:** Asignación explícita de la guía oficial de la entrega, que orientó al
equipo ACERS (SGA) hacia el Enfoque 2 (*legal-first*) sobre cobertura de requisitos
legales.

**Momento en que se detectó:** Antes del registro final en el OSF.

**Mitigación aplicada:** El diseño definitivo *legal-first* quedó fijado y
registrado previamente; las formulaciones previas se descartaron y no se combinaron
con el análisis final.

## Desviación 3: Dos entrevistas (ENTR-01 y ENTR-02) sin registro en video (resuelta para ENTR-01, 2026-09-04)

**Descripción:** Las dos primeras entrevistas de la primera ronda de campo
(`ENTR-01`, 2026-06-20, y `ENTR-02`, 2026-06-21) se registraron únicamente en
audio, sin video. Como consecuencia, el total de video queda en 15 archivos con
231,4 minutos acumulados, por debajo del mínimo terminal de 16 archivos con 240
minutos que establece la guía (Sección 5, tabla de evidencia mínima). El total de
audio sí alcanza el mínimo: 16 archivos.

**Razón:** En esas dos primeras sesiones de elicitación, realizadas al inicio del
proyecto (Entrega 1A), el equipo no contaba todavía con el protocolo de captura en
video definido; solo se grabó audio con el consentimiento correspondiente. El
protocolo de registro en video simultáneo se formalizó a partir de la tercera
sesión de campo (`ENTR-03` en adelante), y desde entonces se mantuvo sin
excepciones.

**Momento en que se detectó:** Durante la verificación técnica de las fichas de
evidencia (`fichas_tecnicas.csv`) con `ffprobe`, en la preparación de la Entrega 4
(2B), al generar el inventario real de audios y videos de las 17 entrevistas.

**Mitigación aplicada:** Se verificó primero que los videos de `ENTR-01` y
`ENTR-02` no existieran en ninguna otra ubicación del equipo antes de dar la
ausencia por definitiva. Ambas entrevistas cuentan con audio completo, consentimiento
firmado y transcripción, por lo que la evidencia cualitativa de esas dos sesiones
no se pierde, solo el registro audiovisual en video. No se sustituyó la ausencia
con ningún archivo generado artificialmente.

Para `ENTR-01` se localizó y recuperó un archivo de video real (2026-09-04):
702 segundos (11,7 minutos) de duración, con la pista de audio completa de la
entrevista al administrador. El participante autorizó el uso de su voz pero no
de su imagen, por lo que el equipo anonimizó la pista visual (queda en negro
durante toda la grabación) antes de incorporarla, en vez de descartar el video
o de usar uno sin el consentimiento correspondiente. Esto eleva el total a 16
archivos de video con 243,1 minutos acumulados, cumpliendo el mínimo de la guía
(≥16 archivos, ≥240 minutos). El archivo
(`2026-06-20_Administrador_ENTR-01_Entrevista.mp4`, hash SHA-256
`76cc008c5a18f5716b1733fecc8ad392bab2178b23fe480ca3cf5d49d1f2446d`) se insertó en
`eVIDENCIAS/vIDEOS/` dentro del paquete cifrado
`02_Evidencias/00_Restringido/evidencias_restringidas.7z` (protegido con
contraseña, 7zAES), re-empaquetado en un nuevo conjunto de volúmenes RAR
(`evidencias_restringidas.part01.rar` a `part28.rar`, reemplazando el conjunto
anterior de 24 partes) y verificado con una prueba de integridad completa y una
extracción de control cuyo hash coincide exactamente con el original. `ENTR-02`
sigue sin registro en video; con el mínimo ya alcanzado por los otros 16, esto ya
no bloquea el criterio, pero se mantiene como una brecha conocida y documentada,
no oculta.

**Artefacto:** `02_Evidencias/00_Restringido/evidencias_restringidas.part01.rar`
a `part28.rar` (paquete cifrado con el video de ENTR-01 ya incorporado),
`02_Evidencias/fichas_tecnicas.csv`,
`02_Evidencias/Consentimientos/2026-06-20_Administrador_ENTR-01_Consentimiento.jpeg`.

## Desviación 4: Revisión del enfoque del registro OSF y enmienda (2026-09-04)

**Descripción:** El registro OSF original `7cvhy` (creado el 2026-08-02) se titulaba
"Protocolo de validación de explicabilidad - AgroMoreira", correspondiente al
enfoque (Enfoque 1) de explicabilidad del módulo de diagnóstico por imagen. Tras la
orientación de la guía oficial hacia el Enfoque 2 (*legal-first*) sobre cobertura de
requisitos legales, el enfoque del componente empírico se revisó al *legal-first*,
con el mismo diseño estadístico pre-registrado (comparación pareada de 26 criterios
C1-C26, prueba de McNemar, IC por bootstrap α=0.05).

**Razón:** Ajuste metodológico derivado de la asignación explícita del Enfoque 2 por
la guía oficial de la Entrega 4 (2B). En lugar de abandonar el registro `7cvhy` (que
sí tiene una marca temporal, 2026-08-02, anterior a la recolección final de datos), se
optó por **enmendarlo**: se agregó una actualización a `7cvhy` donde consta la
revisión al enfoque *legal-first* y se conserva el sello temporal original. El plan
de análisis comprometido (McNemar pareado, 26 criterios, bootstrap 10k, α=0.05) no
cambió entre la versión original y la enmienda.

**Momento en que se detectó:** Durante la coordinación del depósito FAIR (2026-09-04),
al verificar frente a la API pública de OSF que `7cvhy` es un preregistro formal y que
`gc9au` (proyecto asociado del legal-first) es un proyecto, no un preregistro.

**Mitigación aplicada:** Se enmendó el registro `7cvhy` con la nota de actualización
que documenta el cambio a *legal-first* y la coherencia del plan de análisis. El
manuscrito y este archivo documentan la relación entre el preregistro (`7cvhy`), el
proyecto asociado (`gc9au`) y la ejecución efectiva del estudio. La decisión de
análisis (McNemar sobre los 26 criterios) se mantuvo idéntica a la comprometida en el
registro.

## Desviación 5: Codificación de la cobertura legal, segunda codificación y kappa (2026-09-04)

**Descripción inicial:** La tabla de cobertura de los 26 criterios legales
(`07_Datos/datos_crudos/cobertura_legal.csv`), que alimenta la prueba de McNemar
del componente empírico, fue codificada inicialmente por un solo integrante del
equipo. No se había calculado un coeficiente de acuerdo entre codificadores
(kappa de Cohen) sobre esa evaluación binaria de cubierto o no cubierto.

**Razón:** La evaluación de cobertura se deriva directamente del articulado de
las tres normas (LOPDP, Resolución 183 de AGROCALIDAD y Resolución 0072), una
asignación objetiva y verificable contra la fuente. Se priorizó inicialmente una
codificación única con verificación contra el texto normativo, dada la
restricción de tiempo de la ronda terminal de la entrega.

**Momento en que se detectó:** Durante la preparación del depósito FAIR y la
lista de verificación previa al cierre (2026-09-04).

**Mitigación aplicada (resuelta):** Se realizó la segunda codificación
independiente de los 26 criterios por un segundo integrante del equipo
(Escudero Plaza, María del Rosario), generando
`07_Datos/datos_crudos/cobertura_legal_codificador_b.csv`. Se calculó el
coeficiente kappa de Cohen para cobertura binaria legal con el script
`10_Autoria/doble_codificacion/calcular_kappa_legal.py`. Resultado:

- **Kappa convencional:** 1.000 (acuerdo casi perfecto)
- **Kappa legal-first:** 1.000 (acuerdo casi perfecto)
- **Coincidencia total:** 26/26 = 100%

El acuerdo perfecto se explica porque la fuente
(`01_ERS/Modelo_Legal_LOPDP.md`) documenta de forma explícita y no ambigua
qué requisitos cubren qué criterios, haciendo que la codificación sea
reproducible y no dependiente de juicio interpretativo. Los resultados
completos están en `10_Autoria/doble_codificacion/resultado_kappa_legal.txt`.

## Desviación 6: El cuestionario no alcanzaba las 60 respuestas del perfil dominante (resuelta, 2026-09-04)

**Descripción:** El protocolo y la guía de la Entrega 4 (2B) fijan un mínimo de
60 respuestas del perfil dominante del cuestionario, o en su defecto una
justificación por cálculo de potencia estadística. Al cierre de la auditoría
interna, el cuestionario tenía 66 respuestas en total, con el perfil dominante
"Agricultor" en 21 respuestas, por debajo del mínimo de 60. El manuscrito,
antes de esta corrección, afirmaba por error que se había alcanzado el mínimo
de 60; la afirmación no coincidía con los datos y se corrigió en su momento en
la Sección 3 (Participantes y reclutamiento).

**Razón:** El levantamiento del cuestionario se cerró junto con el resto del
trabajo de campo terminal sin verificar antes el conteo por perfil contra el
mínimo de la guía.

**Momento en que se detectó:** Durante la auditoría de cierre de la Entrega 4
(2B) (2026-09-04), al contrastar `respuestas_cuestionario.csv` con la tabla de
mínimos empíricos de la guía oficial.

**Mitigación aplicada:** Se optó por la ruta (a): recolectar respuestas
adicionales del perfil "Agricultor" compartiendo de nuevo el mismo formulario
de Google Forms (no uno nuevo, para no fragmentar el dataset). El levantamiento
se cerró el mismo día (2026-09-04) con 114 respuestas totales, de las cuales 68
son del perfil "Agricultor" — por encima del mínimo de 60. El archivo
`02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario.csv` se
actualizó con las 114 respuestas, y se conserva el export original de 66
respuestas (`cuestionario_respuestas_2026-08-30.xlsx`) junto al nuevo export
completo (`cuestionario_respuestas_2026-09-04.xlsx`) para trazabilidad. El
manuscrito se actualizó en la Sección 3 con la cifra final (114 personas, 68
del perfil dominante). No se descartó ni se recodificó ninguna respuesta
anterior; el cierre es aditivo sobre el mismo instrumento.

---

*Estas desviaciones se reutilizan de la sección de metodología del manuscrito y
quedan registradas en la sección "Deviations from pre-registration" del OSF, con su
razón, momento de detección y mitigación.*
