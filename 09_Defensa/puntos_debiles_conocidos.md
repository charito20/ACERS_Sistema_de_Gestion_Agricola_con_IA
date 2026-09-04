# Puntos débiles conocidos — respuestas preparadas

Estos son los puntos que el propio equipo detectó durante la auditoría interna previa al cierre. No están aquí para esconderlos — están para que, si el docente pregunta por cualquiera de ellos, el equipo responda con seguridad y con la evidencia exacta, en vez de improvisar o sorprenderse. Un proyecto que detecta y documenta sus propias inconsistencias antes de que las señale un tercero se defiende mejor que uno que finge no tenerlas.

## 1. La transcripción de ENTR-16 dice algo distinto al resto

**El problema:** la introducción oral de la entrevista de ENTR-16 dice "la información utilizada no será publicada, será anonimizada", mientras que el resto de transcripciones usa la fórmula "...públicamente será anonimizada/anónima".

**La respuesta preparada:** se verificó el consentimiento firmado real de esa participante (no solo la transcripción) y contiene la misma cláusula de autorización de depósito en Zenodo bajo CC BY 4.0 que firmaron los otros 10 participantes de la misma ronda de campo. Es decir, hay autorización escrita válida. La transcripción se dejó tal como se grabó, sin editarla, porque alterar lo que la persona dijo para que "encaje" con el documento firmado sería falsificar la evidencia primaria — se prefirió documentar la discrepancia por escrito en `07_Publicacion/dataset_zenodo/ETHICS.md` en vez de tocar el registro original. Queda pendiente confirmar con quien hizo la entrevista si fue un desliz al leer el guion de consentimiento en voz alta.

**Artefacto:** `07_Publicacion/dataset_zenodo/ETHICS.md`, sección "Verificación de consentimiento para el depósito en Zenodo".

## 2. Seis participantes nunca autorizaron por escrito el depósito público (resuelto, 2026-09-04)

**El problema (señal incorrecta):** una revisión previa había asumido que ENTR-01 a ENTR-06 firmaron una plantilla de consentimiento más antigua (primera ronda de campo) que solo autorizaba uso académico interno, sin mencionar depósito en Zenodo ni licencia CC BY 4.0.

**Lo que se corrigió:** se verificaron directamente los 6 consentimientos firmados originales (fotografías de los documentos, no la plantilla asumida) y los 6 sí contienen la cláusula estándar de autorización de depósito en Zenodo bajo CC BY 4.0, firmada y fechada por cada participante (ENTR-01 a ENTR-06, entre el 20 y el 29 de junio de 2026). La señal original era incorrecta; no hubo que excluir ninguna entrevista ni recabar autorización adicional.

**La respuesta preparada:** si el docente pregunta, la respuesta es que las 17 entrevistas cuentan con autorización escrita verificada para el depósito público en Zenodo — el equipo detectó una posible inconsistencia en la auditoría interna, verificó los documentos firmados originales uno por uno, y confirmó que la autorización sí existía para las 6.

**Artefacto:** `07_Publicacion/dataset_zenodo/ETHICS.md`, sección "Verificación de consentimiento para el depósito en Zenodo".

## 3. El número de entrevistas no es consistente entre documentos (parcialmente resuelto, 2026-09-04)

**El problema original:** el manuscrito y el ERS/SRS hablan de 17 entrevistas + 9 sesiones de validación con walkthrough, y el ERS/SRS asigna 7 de esos 17 códigos ENTR como sesiones de walkthrough (es decir, los walkthroughs son un subconjunto de las 17). Pero `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` hablaban de 16 entrevistas + 9 walkthroughs = 25 sesiones, tratándolos como categorías separadas y no solapadas.

**Lo que se corrigió:** María Escudero confirmó que el conteo real es 17 entrevistas (17 audios y 17 consentimientos firmados: 16 del paquete que envió Robinson más 1 adicional de firma digital). `06_Experimento/protocolo.tex` y `06_Experimento/justificacion_muestra.md` se corrigieron de 16 a 17 entrevistas.

**Lo que sigue pendiente:** si los 9 walkthroughs son un subconjunto de esas 17 entrevistas (como sugiere el manuscrito/ERS) o sesiones separadas además de ellas (como sigue tratándolo `justificacion_muestra.md`, dando 26 sesiones de campo en total tras la corrección). El desglose por integrante de la entrevista número 17 tampoco está confirmado todavía.

**La respuesta preparada:** si el docente pregunta, la respuesta honesta es que el conteo de entrevistas (17) ya está verificado y corregido en todos los documentos, pero la relación exacta entre walkthroughs y entrevistas — si se solapan o no — sigue en proceso de confirmación con quienes coordinaron el trabajo de campo. No inventar una respuesta improvisada sobre ese solapamiento; es preferible reconocer que ese punto específico sigue en verificación.

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
