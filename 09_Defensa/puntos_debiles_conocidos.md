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

## 3. El número de entrevistas no es consistente entre documentos (resuelto en conteo, 2026-09-04)

**El problema original:** el manuscrito y el ERS/SRS hablan de 17 entrevistas, con 7 de esos 17 códigos ENTR también como sesiones de walkthrough (es decir, los walkthroughs son un subconjunto de las 17). Pero `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` hablaban de 16 entrevistas + 9 walkthroughs = 25 sesiones, tratándolos como categorías separadas y no solapadas.

**Lo que se corrigió:** María Escudero confirmó dos cosas por escrito (2026-09-04): (1) el conteo real es 17 entrevistas, verificado contra 17 audios y 17 consentimientos firmados; (2) los walkthroughs **se hicieron a partir de las entrevistas mismas, no como sesiones ni grabaciones separadas** — confirmando la relación de subconjunto que ya usaban el manuscrito y el ERS/SRS. `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` se corrigieron en ambos puntos: 16→17 entrevistas, y de "17+9=26 sesiones separadas" a "9 (o 7, ver abajo) de las 17 también fueron walkthrough".

**Lo que sigue pendiente (dos cosas distintas):**
1. **Discrepancia numérica menor:** el ERS/SRS identifica 7 códigos ENTR como walkthrough (ENTR-07, 08, 10, 11, 12, 15, 16); el desglose por integrante que traía `justificacion_muestra.md` sumaba 9. Falta reconciliar cuál cifra es la correcta.
2. **Pregunta de evidencia (nueva, planteada por María el 2026-09-04):** la guía pide actas y videos de las sesiones de walkthrough. Como estas no fueron grabaciones aparte sino parte de la entrevista misma, el equipo todavía no decide cómo cubrir ese requisito de evidencia — si basta con señalar el tramo correspondiente dentro de cada entrevista, o si hace falta redactar una acta de síntesis por cada una de esas sesiones.

**La respuesta preparada:** si el docente pregunta, la respuesta es que el conteo de entrevistas (17) y la relación walkthrough/entrevista (subconjunto, no sesiones aparte) ya están verificados y corregidos en todos los documentos. Quedan dos detalles menores sin cerrar: la cifra exacta de walkthroughs (7 vs 9) y cómo documentar la evidencia (actas/videos) de esas sesiones dado que no fueron grabaciones independientes.

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
