# Retrospectiva del equipo ACERS — Examen suspenso

**Fecha:** 15 de septiembre de 2026
**Integrantes:** Roselyn Sánchez, Danela Arteaga, Kamila Calle, María Escudero, Jeanpierre Robinson

## Qué hicimos entre el 13 y el 15 de septiembre de 2026

### Kamila Calle (analista de requerimientos)
- Agregó flujos alternativos y excepciones a los 14 casos de uso del ERS (CU-01 a CU-14), documentando 45 flujos con 52 menciones, 51 precondiciones y 46 poscondiciones.
- Actualizó la matriz de trazabilidad con columna ID-Flujo para trazar cada flujo alternativo.
- Redactó los 6 RNF del componente inteligente (RNF-12 a RNF-17) con referencia a caso de uso y flujo.
- Corrigió todas las menciones de "registro previo" en ERS, protocolo, OSF, CHANGELOG y manuscrito.
- Recompiló el PDF del ERS (pasó de 37 a 44 páginas).

### María Escudero (investigación experimental)
- Corrigió la afirmación "orden correcto" en `osf_registration.md`.
- Agregó la declaración de registro retrospectivo en amenazas a la validez del manuscrito (`manuscrito_final.tex` L187).
- Regeneró `checksums.sha256` tras los cambios del ERS.
- Generó las notas de campo de las sesiones de member checking (ENTR-11, ENTR-12, ENTR-14).
- Convirtió el diccionario de datos a CSV real con separador coma.

### Roselyn Sánchez (gestión del repositorio)
- Actualizó `CITATION.cff` y `CHANGELOG.md` con la entrada v2.3-final.
- Regeneró checksums tras los cambios del ERS.
- Creó la etiqueta anotada `v2.3-final`.

### Danela Arteaga (diseño y modelado UML)
- Sin cambios asignados en esta ronda (modelado UML cerrado en 100%).

### Jeanpierre Robinson (líder)
- Sin cambios asignados en esta ronda (liderazgo y entrevistas cerrados).

## Qué aprendimos

1. **El preregistro OSF no cubre la totalidad del campo.** Las 6 primeras entrevistas (junio 2026) se hicieron antes de registrar en OSF (agosto 2026). Documentamos esta limitación en las desviaciones sin intentar disimularla.
2. **Los flujos alternativos son esenciales en un ERS.** Un caso de uso sin flujos alternativos está enunciado, no especificado. Esta corrección fue la de mayor peso en el examen.
3. **Los manifiestos de checksums deben regenerarse en orden:** primero el de la subcarpeta, luego el raíz. Regenerarlos al revés crea inconsistencias.
4. **El CHANGELOG es un archivo vivo.** Cada versión etiquetada y cada ronda de correcciones debe registrarse con fecha, quién hizo qué y la etiqueta correspondiente.
