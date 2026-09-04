# Banco de preguntas — Defensa final AgroMoreira (ACERS / SGA)

Preguntas probables organizadas por bloque, con respuesta sugerida y el artefacto exacto que la respalda. El objetivo es que cualquier integrante pueda responder cualquier bloque, no solo el suyo.

---

## 1. Enfoque metodológico (legal-first)

**¿Por qué compararon "antes vs. después" en vez de solo describir el sistema final?**
Porque la pregunta de investigación es si el enfoque legal-first (partir del marco legal aplicable y derivar requisitos desde ahí) cubre más obligaciones legales que la elicitación convencional (entrevistas y walkthroughs sin ese punto de partida). Comparar las mismas 26 unidades en dos momentos permite aislar el efecto del enfoque, no solo describir un resultado final. Ver `06_Experimento/protocolo.tex` y `07_Publicacion/manuscrito_final.tex`, sección de metodología.

**¿Qué son exactamente los 26 criterios legales?**
Obligaciones o derechos verificables derivados del articulado de tres normas aplicables a Agrícola Moreira: LOPDP (13 criterios, C1–C13), Resolución 183 de AGROCALIDAD sobre trazabilidad del cacao (7 criterios, C14–C20) y Resolución 0072 sobre bioseguridad fitosanitaria (6 criterios, C21–C26). Están documentados uno por uno en `01_ERS/Modelo_Legal_LOPDP.md`. Ver también `06_Experimento/justificacion_muestra.md`, sección 1.

**¿No es artificial fijar el número en 26?**
No, es el conjunto completo de obligaciones relevantes derivadas de las tres normas aplicables identificadas, no un número elegido para el análisis — está documentado explícitamente así en `06_Experimento/justificacion_muestra.md`.

---

## 2. Estadística y resultados

**¿Qué prueba estadística usaron y por qué?**
McNemar, porque los datos son binarios (cubierto/no cubierto) y pareados (las mismas 26 unidades medidas dos veces, antes y después). Resultado real: χ² = 16.056, p ≈ 0.0001 (`07_Datos/resultados/tabla_mcnemar.csv`). La discordancia es asimétrica: 18 criterios pasaron de no cubierto a cubierto, 0 criterios perdieron cobertura (tabla 2×2 en el mismo archivo).

**¿Cuál fue la magnitud del efecto?**
Diferencia de proporciones de cobertura: 0.692 (69,2 puntos porcentuales), con IC 95% por bootstrap percentil (10.000 réplicas, semilla 42) de [0.50, 0.846] (`07_Datos/resultados/ic_bootstrap.csv`). La cobertura pasó de 26,9% (7/26) a 96,2% (25/26) — ver `07_Datos/resultados/power_calc_mcnemar.txt`.

**¿Tenían potencia estadística suficiente con solo 26 unidades?**
Sí. El cálculo a priori (asumiendo un efecto conservador del 30%, basado en Amaral et al. 2021) indicaba que 26 unidades bastaban para potencia ≥ 0.80 a α = 0.05. El efecto observado (0.692) superó ampliamente ese supuesto, y el cálculo de potencia post-hoc con n=26 da 1.0000 (`07_Datos/resultados/power_calc_mcnemar.txt`, `06_Experimento/justificacion_muestra.md` sección 3).

**¿Cómo garantizaron que la codificación de "cubierto/no cubierto" no fuera subjetiva?**
Con doble codificación independiente: un evaluador primario (María Escudero) y uno secundario (Kamila Calle) codificaron los 26 criterios por separado, y se calculó el coeficiente kappa de Cohen. Resultado: kappa = 1.000 (acuerdo perfecto) tanto para la cobertura convencional como para la legal-first, 26/26 coincidencias. Script y resultado en `10_Autoria/doble_codificacion/calcular_kappa_legal.py` y `resultado_kappa_legal.txt`. El acuerdo perfecto se explica porque `01_ERS/Modelo_Legal_LOPDP.md` documenta de forma no ambigua qué requisito cubre qué criterio — no es un juicio muy interpretativo.

**¿El análisis es reproducible?**
Sí, con un único comando: `python 07_Datos/scripts/run_all.py` sobre los datos crudos en `07_Datos/datos_crudos/`, sin intervención manual. Reproduce exactamente las tablas y la figura publicadas. Ver `07_Datos/README_datos.md`.

---

## 3. Ética y consentimiento

**¿Cómo garantizan el consentimiento informado de los participantes?**
Los 17 participantes firmaron consentimiento informado antes de cualquier grabación, conforme a la LOPDP Art. 8 (libre, específico, informado, inequívoco, revocable). El paquete ético completo (13 anexos A + 4 C) está en `08_Etica/`. Resumen en `07_Publicacion/dataset_zenodo/ETHICS.md`.

**¿Cómo anonimizan los datos antes de publicarlos?**
Redacción de nombre y cédula/firma en las imágenes de consentimiento (caja opaca sobre coordenadas de píxel verificadas, no difuminado), sustitución de nombres reales por códigos ENTR-01 a ENTR-17 en transcripciones, y separación entre zona restringida (identificable, cifrada AES-256, acceso solo del docente) y zona pública (anonimizada). Protocolo completo en `08_Etica/C3_Protocolo_Anonimizacion_Agricola_Moreira.pdf` y `07_Publicacion/dataset_zenodo/ANONYMIZATION.md`.

**¿Qué pasa si el docente pregunta específicamente por la participante de ENTR-16?**
Ver `puntos_debiles_conocidos.md`, es una de las preguntas que el equipo debe poder responder con seguridad porque ya se auditó a fondo.

---

## 4. Requisitos, trazabilidad y modelado

**¿Cuántos requisitos tienen y de dónde salen?**
39 requisitos funcionales y 21 no funcionales. 31 de los RF tienen evidencia directa de entrevista/walkthrough; 8 se derivaron directamente de los 26 criterios de cumplimiento legal. Ver `01_ERS/ERS_SRS_2B_v2.0.md`, sección de RF/RNF, y `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx` para la cadena completa Ley → Objetivo → Interesado → Evidencia → RF/RNF → CU → HU → CA → Componente → Mockup.

**¿Cómo priorizaron los requisitos?**
MoSCoW + Kano + WSJF combinados. Ver `01_ERS/priorizacion_moscow_kano.csv`.

**¿Qué evidencia respalda cada requisito?**
Cada entrevista tiene un código de evidencia (EV-01 a EV-17, correspondiente a ENTR-01 a ENTR-17) enlazado en la matriz de trazabilidad. Ver la lista completa en `01_ERS/ERS_SRS_2B_v2.0.md`, sección de correspondencia EV↔ENTR.

---

## 5. Datos abiertos, FAIR y depósito

**¿Dónde van a depositar el paquete de datos?**
Zenodo, bajo licencia CC BY 4.0 para datos y documentación, MIT para código. Ver `07_Datos/registro_deposito.md` para el estado exacto de cada identificador persistente al momento de la defensa (DOI, SWHID, evaluación F-UJI).

**¿Ya tienen el DOI?**
Responder con el estado real al día de la defensa, tal como está en `07_Datos/registro_deposito.md` — no adelantar un estado que no esté confirmado en el repositorio.

**¿Qué es F-UJI y ya lo corrieron?**
Es la herramienta automática de evaluación de los principios FAIR (localizable, accesible, interoperable, reutilizable). La autoevaluación manual está en `07_Publicacion/dataset_zenodo/ETHICS.md`/`07_Datos/fair_assessment.md`; la ejecución automática contra la URL de Zenodo es el último paso, posterior al depósito — responder según el estado real al momento de la defensa.

---

## 6. Autoría y contribución individual

**¿Cómo se reparten el trabajo y cómo lo acreditan?**
Cada integrante tiene su aporte documentado con rutas de archivos de los que es responsable e IDs de commits que lo acreditan, en `10_Autoria/aporte_individual.md`, conforme al gatekeeper P8 de la guía (contribución individual verificable).

**¿Qué pasó con Jeanpierre?**
Responder con la situación real y documentada, sin minimizarla ni exagerarla: se alejó del equipo el 2026-09-01 sin continuar contribuyendo varios días; el resto del equipo redistribuyó sus tareas pendientes (cierre del modelo legal-first, del manuscrito, registro OSF); manifestó intención de reincorporarse antes del cierre. Su factor individual depende de la contribución verificable que quede acreditada a su nombre en el repositorio y de su participación en la defensa oral — no de esta nota. Ver `10_Autoria/aporte_individual.md`, nota inicial y su sección específica.

---

## Nota de mantenimiento

Este archivo se escribió el 2026-09-04 sobre el estado del repositorio hasta el commit `12d3037`. Antes de la defensa, revisar que las respuestas de las secciones 5 (depósito) y 3 (ENTR-16 / ENTR-01–06) sigan reflejando el estado real — son las dos partes del proyecto que más probablemente cambien entre esta fecha y el cierre.
