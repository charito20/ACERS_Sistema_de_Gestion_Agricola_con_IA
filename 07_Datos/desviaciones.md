# Desviaciones del protocolo respecto del registro OSF

Este archivo documenta las desviaciones del análisis efectivo respecto del
protocolo pre-registrado en el OSF, requeridas por la práctica transparente y por
la guía de desarrollo del proyecto.

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

## Desviación 3: ENTR-01 se grabó en video, pero el consentimiento solo autoriza el audio; ENTR-02 se registró solo en audio

**Descripción:** Las dos primeras entrevistas de campo (`ENTR-01` y `ENTR-02`)
tienen un registro audiovisual distinto al del resto. `ENTR-01` se grabó en video
durante la sesión, pero el consentimiento informado que el participante firmó
autoriza el uso de su voz y no el de su imagen; por eso el video se conserva con
la pista visual anonimizada (en negro) y la pista de audio íntegra. `ENTR-02` se
registró únicamente en audio. Las demás entrevistas (`ENTR-03` en adelante) tienen
video y audio completos.

**Razón:** En las primeras sesiones el equipo todavía no había fijado el
procedimiento de captura y archivo del video. En `ENTR-01`, además, el participante
marcó en el consentimiento solo la casilla de grabación de audio, por lo que el
equipo optó por preservar la evidencia sin exponer su imagen en lugar de descartar
la grabación. Desde `ENTR-03` el video se grabó y archivó de forma sistemática y
sin excepciones.

**Momento en que se detectó:** Al generar con `ffprobe` el inventario real de
audio y video de las 17 entrevistas para las fichas técnicas
(`02_Evidencias/fichas_tecnicas.csv`), durante la preparación de la entrega.

**Mitigación aplicada:** El video de `ENTR-01`
(`2026-06-20_Administrador_ENTR-01_Entrevista.mp4`, hash SHA-256
`76cc008c5a18f5716b1733fecc8ad392bab2178b23fe480ca3cf5d49d1f2446d`, 702 segundos)
se conserva dentro del contenedor cifrado de la zona restringida, con la imagen en
negro y el audio completo, y su duración real se contabiliza en el total. Con esto
el inventario de video queda en 16 archivos y 243,1 minutos acumulados. `ENTR-02`
sigue sin registro en video y se mantiene como una brecha conocida y documentada,
no oculta; su contenido está íntegro en el audio y en la transcripción. Las dos
entrevistas cuentan con audio completo, consentimiento firmado y transcripción
anonimizada, por lo que su evidencia cualitativa no se pierde. No se sustituyó
ninguna ausencia con material generado artificialmente.

**Artefacto:** `02_Evidencias/00_Restringido/evidencias_restringidas.part01.rar`
a `part28.rar`, `02_Evidencias/fichas_tecnicas.csv`,
`02_Evidencias/Consentimientos/2026-06-20_Administrador_ENTR-01_Consentimiento.jpeg`.

## Desviación 4: Revisión del enfoque del registro OSF y enmienda

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

## Desviación 5: Codificación de la cobertura legal, segunda codificación y kappa

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

## Desviación 6: El cuestionario no alcanzaba las 60 respuestas del perfil dominante (resuelta)

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
son del perfil "Agricultor", por encima del mínimo de 60. El archivo
`02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario.csv` se
actualizó con las 114 respuestas, y se conserva el export original de 66
respuestas (`cuestionario_respuestas_2026-08-30.xlsx`) junto al nuevo export
completo (`cuestionario_respuestas_2026-09-04.xlsx`) para trazabilidad. El
manuscrito se actualizó en la Sección 3 con la cifra final (114 personas, 68
del perfil dominante). No se descartó ni se recodificó ninguna respuesta
anterior; el cierre es aditivo sobre el mismo instrumento.

**Anonimización aplicada (2026-09-05):** el export completo y el CSV derivado
se sustituyeron por una versión anonimizada en la que la marca temporal se
generalizó a nivel de fecha, sin hora, minuto ni segundo. La marca temporal
exacta de envío es un cuasi-identificador: combinada con el perfil declarado y
el rango de edad, permite reidentificar a una persona dentro de una unidad
productiva pequeña. La generalización se aplicó únicamente a esa columna: se
verificó celda por celda que las 114 respuestas y sus 9 columnas de contenido
quedaron idénticas (0 diferencias fuera de la columna de marca temporal). El
conteo por perfil no cambia: 114 respuestas totales, 68 del perfil dominante
"Agricultor". El mismo tratamiento se aplicó al export histórico
`cuestionario_respuestas_2026-08-30.xlsx` (66 respuestas), que se conserva por
trazabilidad: sus 66 marcas temporales quedaron igualmente generalizadas a
nivel de fecha, con 0 cambios de contenido verificados celda por celda. De este
modo ningún archivo publicado del cuestionario conserva la hora exacta de
envío. Esta medida es coherente con el protocolo de anonimización del paquete
ético (`08_Etica/C3_Protocolo_Anonimizacion_Agricola_Moreira.pdf`).

## Desviación 7: Las fotografías de evidencia no conservan sus metadatos EXIF originales

**Descripción:** La guía de desarrollo (elemento A11) exige que cada fotografía
del proyecto conserve sus metadatos originales, con la fecha de captura tomada
de los metadatos y el dispositivo. Al preparar el inventario
`10_Autoria/exif_inventario.csv` se verificó archivo por archivo que ninguna de
las fotografías del repositorio conserva metadatos EXIF: las 22 fotografías de
`02_Evidencias/Fotos_Entorno/` y las 5 fotografías de aplicación del
cuestionario en `02_Evidencias/Cuestionario/Fotos_Aplicacion/` tienen
únicamente una cabecera JFIF, sin fecha de captura ni información del
dispositivo. Por eso las columnas de fecha y dispositivo de
`exif_inventario.csv` figuran vacías.

**Razón:** Las fotografías se compartieron entre los integrantes del equipo a
través de aplicaciones de mensajería, que eliminan los metadatos EXIF al
comprimir la imagen. En al menos un caso, además, la fotografía se editó para
cubrir un elemento identificable, y la edición también elimina los metadatos.

**Momento en que se detectó:** Durante la preparación del inventario EXIF para
la entrega final (2026-09-06), al intentar extraer la fecha de captura y el
dispositivo de cada fotografía.

**Mitigación aplicada:** Las fotografías se conservan como evidencia del
proceso de campo, ya que su contenido es real y verificable (se observa el
entorno de la finca y, en el caso del cuestionario, el formulario abierto
durante su aplicación). La fecha aproximada de cada fotografía de entorno se
mantiene en el propio nombre del archivo, en formato AAAA-MM-DD, a partir del
registro que llevó el equipo en su momento. Para el inventario se registra el
nombre, el hash SHA-256 real de cada archivo y la nota de que los metadatos no
se conservaron. En futuras rondas de campo, las fotografías se transferirán por
un medio que preserve los metadatos y se registrará su ficha técnica el mismo
día de la captura.

## Desviación 8: Las notas de campo no se registraron de forma manuscrita por sesión

**Descripción:** La guía de desarrollo (elemento A5) pide una nota de campo
manuscrita y escaneada por cada sesión de elicitación, con la fecha visible, el
lugar, la duración y el observador. La carpeta `10_Autoria/notas_campo/` del
repositorio no contiene notas de campo: solo tiene el archivo de descripción de
la carpeta.

**Razón:** Durante las rondas de campo (junio y agosto de 2026) el equipo no
asignó a nadie la responsabilidad explícita de tomar y conservar una nota de
campo manuscrita por sesión. La información contextual de cada entrevista (el
ambiente, la actitud del participante, las condiciones de la sesión) se recogió
dentro de las grabaciones y de las transcripciones, no en un cuaderno de campo
separado.

**Momento en que se detectó:** Durante la auditoría de cierre para la entrega
final, al revisar el contenido de la carpeta `10_Autoria/notas_campo/` contra
el elemento A5 de la guía.

**Mitigación aplicada:** El equipo reconoce el vacío y no lo cubre con notas
redactadas después de las sesiones y presentadas como manuscritas originales,
porque eso comprometería la integridad de la evidencia. La información
contextual de cada una de las 17 sesiones queda disponible en su transcripción
y en su grabación (zona restringida cifrada). Para futuras rondas de campo,
cada entrevistador redactará una nota de campo breve inmediatamente después de
cada sesión, con fecha, lugar, duración y observador, y la digitalizará el
mismo día.

## Desviación 9: Las sesiones de validación (walkthrough) se realizaron dentro de las entrevistas, no como sesiones separadas

**Descripción:** La guía de desarrollo (Sección 5) pide al menos 6 sesiones de
validación cerradas (walkthrough), 3 con usuarios técnicos y 3 con usuarios no
técnicos, cada una con acta firmada por el participante y grabación en el
contenedor cifrado. El equipo realizó 7 sesiones de walkthrough (3 con perfil
técnico: ENTR-07, ENTR-10, ENTR-16; y 4 con perfil no técnico: ENTR-08,
ENTR-11, ENTR-12, ENTR-15), lo que cumple el mínimo de cantidad y de mezcla de
perfiles. Sin embargo, esas sesiones no se realizaron como reuniones
independientes: se integraron en la segunda parte de la entrevista
semiestructurada del mismo participante, donde el equipo compartía pantalla y
presentaba el prototipo para recoger retroalimentación.

**Razón:** Para no duplicar la carga sobre los participantes de la finca, que
ya habían dedicado tiempo a la entrevista, el equipo optó por presentar el
prototipo y recoger su validación en la misma sesión, en lugar de convocarlos
de nuevo para una reunión aparte.

**Momento en que se detectó:** Durante la reconciliación del conteo de sesiones
para la entrega final, al confrontar la tabla de correspondencia entre
evidencias y códigos de entrevista del ERS con la exigencia de la guía sobre
sesiones separadas.

**Mitigación aplicada:** Se redactó un acta por cada una de las 7 sesiones de
walkthrough en `02_Evidencias/Validacion_Walkthrough/`, a partir del tramo de
validación de la transcripción original de cada entrevista, identificando qué
se validó, las observaciones del participante y la conclusión de la sesión.
Cada participante firmó el consentimiento informado de su entrevista, que cubre
también el tramo de walkthrough. Las grabaciones de esas sesiones están dentro
del video y del audio de las entrevistas correspondientes, en el contenedor
cifrado de la zona restringida. No se solicitó una firma nueva sobre las actas,
redactadas después de las sesiones, para no atribuir a los participantes la
validación de un documento que no llegaron a revisar.

