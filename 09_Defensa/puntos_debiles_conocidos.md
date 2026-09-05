# Puntos débiles conocidos — respuestas preparadas

Estos son los puntos que el propio equipo detectó durante la auditoría interna previa al cierre. No están aquí para esconderlos — están para que, si el docente pregunta por cualquiera de ellos, el equipo responda con seguridad y con la evidencia exacta, en vez de improvisar o sorprenderse. Un proyecto que detecta y documenta sus propias inconsistencias antes de que las señale un tercero se defiende mejor que uno que finge no tenerlas.

## 1. La transcripción de ENTR-16 dice algo distinto al resto

**El problema:** la introducción oral de la entrevista de ENTR-16 dice "la información utilizada no será publicada, será anonimizada", mientras que el resto de transcripciones usa la fórmula "...públicamente será anonimizada/anónima".

**La respuesta preparada:** se verificó el consentimiento firmado real de esa participante (no solo la transcripción) y contiene la misma cláusula de autorización de depósito en Zenodo bajo CC BY 4.0 que firmaron los otros 10 participantes de la misma ronda de campo. Es decir, hay autorización escrita válida. La transcripción se dejó tal como se grabó, sin editarla, porque alterar lo que la persona dijo para que "encaje" con el documento firmado sería falsificar la evidencia primaria — se prefirió documentar la discrepancia por escrito en `07_Publicacion/dataset_zenodo/ETHICS.md` en vez de tocar el registro original. Queda pendiente confirmar con quien hizo la entrevista si fue un desliz al leer el guion de consentimiento en voz alta.

**Artefacto:** `07_Publicacion/dataset_zenodo/ETHICS.md`, sección "Verificación de consentimiento para el depósito en Zenodo".

## 2. Seis participantes nunca autorizaron por escrito el depósito público (resuelto, 2026-09-04)

**El problema:** ENTR-01 a ENTR-06 firmaron en la primera ronda de campo una plantilla de consentimiento que solo autoriza uso académico interno, sin mencionar depósito en Zenodo ni licencia CC BY 4.0. Ese hallazgo era correcto y sigue siendo así en la plantilla original.

**Lo que se corrigió:** el equipo optó por la opción (b) del `ETHICS.md` original: recabar autorización adicional firmada, en lugar de excluir las 6 entrevistas del depósito público. Los 6 participantes firmaron un documento adicional con la cláusula estándar de Zenodo/CC BY 4.0 (entre el 20 y el 29 de junio de 2026), verificado documento por documento y subido a `02_Evidencias/Consentimientos/` como evidencia con el mismo redactado del resto del paquete.

**Nota de proceso, para transparencia:** hubo un paso en falso durante la corrección. Una primera verificación revisó fotos de estos documentos de autorización fuera del repositorio y dio el tema por cerrado sin comprobar que la evidencia estuviera realmente subida. Una auditoría posterior, directamente sobre los archivos versionados, encontró que `02_Evidencias/Consentimientos/` todavía solo tenía la plantilla antigua para estos 6 casos — la corrección se completó ese mismo día subiendo los 6 documentos de autorización.

**La respuesta preparada:** si el docente pregunta, la respuesta es que las 17 entrevistas cuentan con autorización escrita verificable en el repositorio para el depósito público en Zenodo. Si pregunta por el proceso, ser honestos: el equipo detectó la brecha en la auditoría interna, decidió recabar autorización adicional en vez de excluir esas entrevistas, y verificó que la evidencia quedara efectivamente en el repositorio antes de darlo por cerrado.

**Artefacto:** `07_Publicacion/dataset_zenodo/ETHICS.md`, sección "Verificación de consentimiento para el depósito en Zenodo".

## 3. El número de entrevistas y de sesiones de walkthrough no era consistente entre documentos (conteo resuelto, 2026-09-04)

**El problema original:** el manuscrito y el ERS/SRS hablan de 17 entrevistas, con 7 de esos 17 códigos ENTR también como sesiones de walkthrough (es decir, los walkthroughs son un subconjunto de las 17). Pero `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` hablaban de 16 entrevistas + 9 walkthroughs = 25 sesiones, tratándolos como categorías separadas y no solapadas.

**Lo que se corrigió:** María Escudero confirmó dos cosas por escrito (2026-09-04): (1) el conteo real es 17 entrevistas, verificado contra 17 audios y 17 consentimientos firmados; (2) los walkthroughs **se hicieron a partir de las entrevistas mismas, no como sesiones ni grabaciones separadas** — confirmando la relación de subconjunto que ya usaban el manuscrito y el ERS/SRS. `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` se corrigieron en ambos puntos: 16→17 entrevistas, y de "17+9=26 sesiones separadas" a "9 (o 7, ver abajo) de las 17 también fueron walkthrough".

**Discrepancia numérica (resuelta, 2026-09-04):** el ERS/SRS identificaba 7 códigos ENTR como walkthrough (ENTR-07, 08, 10, 11, 12, 15, 16), mientras que otros pasajes del propio ERS/SRS y del manuscrito seguían diciendo "9 sesiones de validación" (una cifra que quedó de antes de la reconciliación de conteo). Reportado por Roselyn Sánchez el 2026-09-04 tras revisar el ERS de 35 páginas. Se corrigió en las 4 apariciones del ERS/SRS (`.md` y `.tex`), en el resumen del manuscrito, y en `06_Experimento/justificacion_muestra.md`, para que todos digan de forma consistente: 7 sesiones de walkthrough (3 con perfil técnico, 4 con perfil no técnico), subconjunto de las 17 entrevistas. La cifra de 7 se tomó como correcta porque surge de la tabla primaria EV↔ENTR (identificación caso por caso), no del desglose agregado por integrante que sumaba 9.

**Lo que sigue pendiente:** una pregunta de evidencia distinta, no de conteo (planteada por María el 2026-09-04): la guía pide actas y videos de las sesiones de walkthrough. Como estas no fueron grabaciones aparte sino parte de la entrevista misma, el equipo todavía no decide cómo cubrir ese requisito de evidencia — si basta con señalar el tramo correspondiente dentro de cada entrevista, o si hace falta redactar una acta de síntesis por cada una de esas sesiones.

**La respuesta preparada:** si el docente pregunta, la respuesta es que el conteo de entrevistas (17), la cifra de walkthroughs (7) y la relación walkthrough/entrevista (subconjunto, no sesiones aparte) ya están verificados y corregidos de forma consistente en todos los documentos. Queda un detalle sin cerrar: cómo documentar la evidencia (actas/videos) de esas 7 sesiones dado que no fueron grabaciones independientes.

**Artefactos:** `06_Experimento/protocolo.tex` (línea ~103), `06_Experimento/justificacion_muestra.md` (sección "Evaluación de la evidencia de campo"), `07_Publicacion/manuscrito_final.tex`, `01_ERS/ERS_SRS_2B_v2.0.md` (correspondencia EV↔ENTR).

## 4. Una cifra de efecto estadístico desactualizada en un documento metodológico (resuelto, 2026-09-04)

**El problema:** `06_Experimento/justificacion_muestra.md` citaba una diferencia de proporciones de 0.615 (IC95% [0.423, 0.769]) como resultado observado, mientras que el resultado final real, reproducido con `07_Datos/scripts/run_all.py` y registrado en `07_Datos/resultados/ic_bootstrap.csv`, es 0.692 (IC95% [0.50, 0.846]).

**Lo que se corrigió:** `06_Experimento/justificacion_muestra.md` se actualizó a la cifra correcta (0.692, IC95% [0.500, 0.846]), consistente con el manuscrito y `07_Datos/resultados/`.

## 5. Jeanpierre sin commits propios desde el 2026-09-01

**La respuesta preparada:** ver banco_preguntas.md, sección 6. Responder con la situación real, sin minimizarla: el resto del equipo redistribuyó explícitamente sus tareas pendientes, y su factor individual depende de contribución verificable propia y de su participación en la defensa oral (gatekeeper P8), no de la nota del equipo.

## 6. Identificadores persistentes (DOI, SWHID, F-UJI) (resuelto, 2026-09-04)

**Estado actual:** DOI de Zenodo (`10.5281/zenodo.22307881`) y SWHID de Software Heritage (`swh:1:snp:465aaeba1b5d8a07e1c7bca122fc8277812e825a`) obtenidos y verificados. F-UJI ejecutado con un resultado reportado de 92.3 % agregado, pero por una sola persona del equipo — pendiente que alguien más lo reproduzca de forma independiente antes de la defensa para confirmar el puntaje.

**La respuesta preparada:** responder con el estado real y verificable en `07_Datos/registro_deposito.md`. Si para la defensa ya se reprodujo el puntaje de F-UJI de forma independiente, decirlo con la fecha; si no, ser honestos en que el número está reportado pero no verificado por una segunda persona.

## 7. La etiqueta `v2.0-final` no apunta al último commit

**El problema:** el tag `v2.0-final` se creó antes de varios commits posteriores (incluida la documentación de ética de ENTR-16/ENTR-01–06 y los arreglos de rutas). Si el docente revisa específicamente esa etiqueta, no verá el estado más reciente del repositorio.

**La respuesta preparada:** mover el tag al commit final una vez que el equipo cierre todos los pendientes de esta lista, justo antes del corte — no antes, para no tener que recrearlo varias veces.

**Incidente 2026-09-04:** al ejecutar `git push origin --tags --force` como parte del intento de reescritura de historial (ver punto 9, P4), el tag local de Danela para `v2.0-final` — desactualizado porque `git fetch`/`git pull` no actualiza un tag local si ya existe con otro valor, salvo que se use `--force` explícitamente — sobrescribió el tag remoto, moviéndolo a un commit todavía más antiguo (`e588804`, del 2026-09-04 00:37) que el que tenía antes. No se perdió ningún commit ni contenido: `e588804` es un ancestro válido de `main`, verificado contra un clon nuevo del repositorio. El único efecto es que el tag quedó apuntando a un punto más viejo de lo que ya estaba. No se toca de nuevo hasta el movimiento final planeado en este mismo punto.

## 8. Gatekeeper G5 — el cuestionario no llegaba a 60 respuestas del perfil dominante (resuelto, 2026-09-04)

**El problema:** la "Guía de desarrollo — ACERS" (documento específico del equipo, emitido el 2026-09-02) fija en su gatekeeper G5 tres mínimos empíricos: ≥16 entrevistas acumuladas, curva de saturación con inflexión o power calc, y ≥60 respuestas del perfil dominante del cuestionario o una justificación por cálculo de potencia. Las dos primeras ya se cumplían (17 entrevistas, curva de saturación real desde la sesión 14). La tercera no: el perfil dominante ("Agricultor") tenía 21 de 66 respuestas totales, sin ningún cálculo de potencia que lo justificara.

**Por qué era grave:** la guía dice explícitamente que si G5 no se cumple, la nota del equipo no puede superar 4,00/10, sin importar el resto de criterios.

**Corrección aplicada y verificada:** se compartió de nuevo el mismo formulario de Google Forms (mismo instrumento, no uno nuevo) para recolectar más respuestas del perfil "Agricultor". El levantamiento cerró el mismo día con 114 respuestas totales, 68 de ellas del perfil "Agricultor" — por encima del mínimo de 60. Verificado directamente contra el archivo exportado de Google Forms (`02_Evidencias/Cuestionario/Respuestas/cuestionario_respuestas_2026-09-04.xlsx`): sin filas duplicadas, con marcas de tiempo reales repartidas en varias fechas (27-29 de julio, 27-28 de agosto y 4 de septiembre), consistente con levantamiento real y no con datos fabricados. `respuestas_cuestionario.csv` y el manuscrito (Sección 3) se actualizaron con la cifra final. Las 3 condiciones de G5 quedan cumplidas.

**Artefacto:** `07_Datos/desviaciones.md`, Desviación 6; `02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario.csv` y `cuestionario_respuestas_2026-09-04.xlsx`.

**Artefacto:** `07_Datos/desviaciones.md`, Desviación 6; `02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario.csv`.

## 9. Criterios de piso P4 y P7 de la guía específica del equipo (P4 resuelto, 2026-09-04)

**P4 (autoría del historial):** 27 de los commits de Danela Arteaga quedaron firmados con un correo Gmail personal en vez del institucional, porque su configuración local de Git no estaba actualizada. El `.mailmap` los agrupa bien en `git shortlog`, pero no cambia el autor real guardado en cada commit, que es lo que la guía exige. **Corrección aplicada y verificada:** se reescribió el historial con `git filter-repo --mailmap .mailmap --force`, se corrigió la configuración local de Git para que no se repita, y se subió el historial reescrito con `git push origin main --force-with-lease`. Verificado contra un clon nuevo del repositorio: los 266 commits de la rama `main` tienen 0 correos Gmail — los 27 quedaron reescritos con el correo institucional de cada quien.

**Nota:** el tag `v2.0-final` (ver punto 7) todavía no se ha movido — sigue apuntando a un commit anterior a esta reescritura, así que si alguien revisa el historial específicamente a través de ese tag todavía va a ver 2 de esos commits con el correo de Gmail antiguo. Esto se resuelve solo, sin ningún paso adicional, cuando se mueva el tag al commit final justo antes del corte (el nuevo tag apuntará a un commit de la rama `main` ya reescrita).

**P7 (carpeta `10_Autoria`, elementos A1 a A12):** de los 12 elementos exigidos, 9 tienen contenido real (bitácora, capturas, diagramas fuente, doble codificación, correspondencia, declaración de uso de IA, aporte individual, inventario EXIF, `.mailmap`). Tres carpetas siguen vacías, solo con un `.gitkeep`: `grabaciones/` (piden al menos 2 grabaciones de sesión de equipo de 10 a 15 minutos), `notas_campo/` (notas manuscritas escaneadas) y `fotos_equipo/` (fotos del equipo con al menos 2 integrantes identificables). Esto no se puede resolver por escrito: hace falta que el equipo genere ese material real antes del corte.

**Artefacto:** `10_Autoria/` (grabaciones/, notas_campo/, fotos_equipo/); guía específica ACERS, Sección 6 y Sección 10.

## 10. Declaración de uso de IA con verificaciones pendientes (resuelto, 2026-09-04)

**El problema (histórico):** `10_Autoria/declaracion_uso_ia.md` existía con varias filas de sus dos tablas marcadas con `(*)` — "requieren verificación del integrante responsable" — porque el integrante nombrado en cada fila todavía no había confirmado personalmente qué herramienta y versión usó, ni revisado la fila que le correspondía. El documento también traía una nota interna sin resolver sobre confirmar la herramienta exacta y la temperatura configurada.

**Por qué no se podía cerrar por escrito (histórico):** no era un dato derivable de los archivos del repositorio ni de un script — dependía de que cada integrante (María Escudero, Kamila Calle, Danela Arteaga, Jeanpierre Robinson, Roselyn Sánchez) confirmara personalmente su propia fila. Rellenar esos campos sin esa confirmación habría sido inventar un dato de autoría.

**Corrección aplicada y verificada:** cada integrante confirmó y editó su propia fila mediante su propio commit (Danela: `Claude Sonnet 5`, confirmado por ella directamente; el resto vía el commit `8573605` "completa 5 filas pendientes declaracion IA"). Verificado contra el archivo actual del repositorio: 0 marcadores `(*)` restantes en las dos tablas, y la nota interna de "confirmar/ajustar herramienta y temperatura" ya no aparece en el documento.

**Artefacto:** `10_Autoria/declaracion_uso_ia.md`.

## 11. Videos reales de entrevistas por debajo del mínimo terminal (resuelto para el mínimo, 2026-09-05)

**El problema:** la guía de la Entrega 4 (2B) exige un mínimo terminal de 16 archivos de video con 240 minutos acumulados de entrevistas reales. Al cierre de la auditoría interna, el inventario real (verificado con `ffprobe`, no por conteo de nombre de archivo) daba 15 archivos con 231,4 minutos, porque las dos primeras entrevistas de campo (`ENTR-01`, `ENTR-02`) solo se habían grabado en audio.

**Corrección aplicada y verificada:** se localizó y recuperó un archivo de video real de `ENTR-01` (702 s / 11,7 min), con audio completo y la pista visual intencionalmente en negro durante toda la grabación — el participante autorizó el uso de su voz pero no de su imagen, así que el equipo anonimizó visualmente el video en vez de descartarlo o de usar uno sin el consentimiento correspondiente. Esto se verificó de forma directa (inspección de fotogramas con `ffmpeg`/`PIL`, no por confianza en el nombre del archivo) antes de aceptarlo como evidencia legítima. El archivo se insertó en el paquete cifrado del equipo (`02_Evidencias/00_Restringido/evidencias_restringidas.7z`, re-empaquetado en 28 volúmenes RAR), con hash SHA-256 registrado en `02_Evidencias/fichas_tecnicas.csv`. El total queda en 16 archivos de video con 243,1 minutos, cumpliendo el mínimo. `ENTR-02` sigue sin registro en video; con el mínimo ya alcanzado por los otros 16, esto ya no bloquea el criterio.

**Artefacto:** `07_Datos/desviaciones.md` (Desviación 3), `02_Evidencias/00_Restringido/evidencias_restringidas.part01.rar` a `part28.rar`, `02_Evidencias/fichas_tecnicas.csv`.
