# Casos de prueba — AgroMoreira

Un caso de prueba formal por cada requisito funcional testeable (38 de los 39 RF; RF-32 queda fuera de alcance por ser Won't have de esta version) y por cada requisito no funcional (21 RNF). Cada caso de prueba formaliza, en pasos y resultado esperado, el **mismo** criterio de verificacion (RF) o metrica/umbral/metodo de verificacion (RNF) ya documentado en `01_ERS/ERS_SRS_2B_v2.0.md` — no se inventa comportamiento nuevo, se estructura el ya especificado en formato de caso de prueba, tal como pide la guia de desarrollo ACERS. El campo Pasos deriva del Flujo principal ya agregado a cada ficha RF.

Responsable de esta especificacion: Danela Arteaga. Revision independiente pendiente (gatekeeper P11): Kamila Calle.

## Casos de prueba — Requisitos Funcionales

### CP-RF-01 — Registro de parcelas/lotes (verifica RF-01)

- **Objetivo:** confirmar que registro de parcelas/lotes se comporta segun el criterio de verificacion definido para RF-01.
- **Precondicion:** usuario autenticado con permiso de edición.
- **Datos de entrada:** nombre, sector, ubicación, área, cultivo, variedad, N.º plantas.
- **Pasos:**
  1. El usuario (Administrador, Técnico o Jornalero) autenticado con permiso de edición selecciona "Nueva parcela".
  2. Ingresa nombre/número, sector, ubicación, área, cultivo, variedad y cantidad de plantas.
  3. El sistema valida que los 7 campos obligatorios estén completos.
  4. El sistema guarda la parcela y la muestra en el listado general en menos de 2 segundos.
- **Resultado esperado:** al crear una parcela con los 7 campos obligatorios, el sistema la muestra en el listado en menos de 2 segundos, sin campos vacíos.
- **Casos alternos a verificar:**
  - Si falta alguno de los 7 campos obligatorios, el sistema rechaza el guardado y marca los campos vacíos (criterio de verificación de RF-01).
  - Si la parcela se marca como "para exportación", el sistema habilita los campos de trazabilidad de exportación (ver RF-14, CU-03).
- **Prioridad:** Must have.

### CP-RF-02 — Catálogo cerrado de cultivos y variedades (verifica RF-02)

- **Objetivo:** confirmar que catálogo cerrado de cultivos y variedades se comporta segun el criterio de verificacion definido para RF-02.
- **Precondicion:** catálogo previamente configurado.
- **Datos de entrada:** selección de cultivo/variedad desde catálogo.
- **Pasos:**
  1. El usuario, al registrar o editar una parcela (CU-01), abre el selector de cultivo/variedad.
  2. El sistema muestra únicamente las opciones del catálogo previamente configurado por el Administrador.
  3. El usuario selecciona el cultivo/variedad y el sistema lo asocia a la parcela.
- **Resultado esperado:** intentar guardar un cultivo fuera del catálogo es rechazado por el sistema.
- **Casos alternos a verificar:**
  - Si el usuario intenta ingresar un cultivo fuera del catálogo (texto libre tipo "otros"), el sistema rechaza el valor (criterio de verificación de RF-02).
  - El Administrador puede ampliar el catálogo dando de alta un nuevo cultivo/variedad, lo que lo deja disponible de inmediato para el resto de usuarios.
- **Prioridad:** Should have.

### CP-RF-03 — Registro de actividades agrícolas (verifica RF-03)

- **Objetivo:** confirmar que registro de actividades agrícolas se comporta segun el criterio de verificacion definido para RF-03.
- **Precondicion:** lote existente.
- **Datos de entrada:** fecha, lote, tipo de actividad, producto, trabajador.
- **Pasos:**
  1. El Jornalero o Técnico selecciona el lote existente sobre el que va a registrar la actividad.
  2. Ingresa fecha, tipo de actividad (fumigación, fertilización, poda, riego, limpieza), producto/insumo usado y trabajador responsable.
  3. El sistema guarda el registro y lo asocia al historial del lote (CU-02).
- **Resultado esperado:** el sistema no permite guardar una actividad sin fecha, lote y trabajador.
- **Casos alternos a verificar:**
  - Si falta la fecha, el lote o el trabajador responsable, el sistema rechaza el guardado (criterio de verificación de RF-03).
  - Si la actividad usa un insumo del catálogo, el sistema descuenta automáticamente el inventario correspondiente (ver RF-07, CU-05).
- **Prioridad:** Must have.

### CP-RF-04 — Registro de cosecha por unidad específica del cultivo (verifica RF-04)

- **Objetivo:** confirmar que registro de cosecha por unidad específica del cultivo se comporta segun el criterio de verificacion definido para RF-04.
- **Precondicion:** lote y cultivo existentes.
- **Datos de entrada:** lote, fecha, cultivo, cantidad, unidad.
- **Pasos:**
  1. El Jornalero selecciona el lote y el cultivo sobre el que va a registrar la cosecha.
  2. El sistema determina la unidad esperada según el cultivo (tacho/quintal para cacao, racimo/caja para plátano).
  3. El usuario ingresa la cantidad cosechada en esa unidad.
  4. El sistema valida la unidad, guarda la cosecha y actualiza el acumulado del lote/periodo.
- **Resultado esperado:** al registrar cosecha de cacao el sistema exige unidad "tacho" o "quintal". De plátano, "racimo" o "caja".
- **Casos alternos a verificar:**
  - Si la unidad ingresada no corresponde al cultivo del lote, el sistema rechaza el registro (criterio de verificación de RF-04).
  - Si corresponde, el usuario puede consultar de inmediato el precio de mercado vigente y ver el ingreso proyectado (RF-15).
- **Prioridad:** Must have.

### CP-RF-05 — Cálculo automático de rendimiento por lote y periodo (verifica RF-05)

- **Objetivo:** confirmar que cálculo automático de rendimiento por lote y periodo se comporta segun el criterio de verificacion definido para RF-05.
- **Precondicion:** existen 2 o más registros de cosecha del lote.
- **Datos de entrada:** histórico de cosechas del lote.
- **Pasos:**
  1. El sistema consulta el histórico de cosechas del lote seleccionado.
  2. Calcula el promedio de producción del periodo (suma dividida entre N registros).
  3. Muestra el promedio y permite comparar contra otros periodos en el reporte del lote.
- **Resultado esperado:** el promedio calculado coincide con el cálculo manual (suma dividida entre N) sobre un set de prueba.
- **Casos alternos a verificar:**
  - Si el lote tiene menos de 2 registros de cosecha, el sistema muestra "datos insuficientes" en vez de un promedio (precondición de RF-05).
- **Prioridad:** Must have.

### CP-RF-06 — Cálculo automático de ganancia neta (verifica RF-06)

- **Objetivo:** confirmar que cálculo automático de ganancia neta se comporta segun el criterio de verificacion definido para RF-06.
- **Precondicion:** existen registros de ingreso y egreso en el periodo.
- **Datos de entrada:** registros de ingresos y egresos.
- **Pasos:**
  1. El sistema consulta los registros de ingreso (automáticos por cosecha/precio y manuales por RF-26) y egreso (insumos, mano de obra) del periodo.
  2. Calcula la ganancia neta como la suma de ingresos menos la suma de egresos.
  3. Muestra el valor en el módulo financiero.
- **Resultado esperado:** ganancia es igual a la suma de ingresos menos la suma de egresos, verificado contra un caso de prueba manual.
- **Casos alternos a verificar:**
  - Si no existen registros de ingreso o egreso en el periodo consultado, el sistema muestra el módulo financiero en cero, sin error.
  - El usuario puede registrar manualmente un ingreso o egreso adicional (RF-26), que se refleja de inmediato en el siguiente cálculo.
- **Prioridad:** Must have.

### CP-RF-07 — Gestión de inventario de insumos (verifica RF-07)

- **Objetivo:** confirmar que gestión de inventario de insumos se comporta segun el criterio de verificacion definido para RF-07.
- **Precondicion:** ninguna.
- **Datos de entrada:** nombre del insumo, cantidad, unidad.
- **Pasos:**
  1. El usuario da de alta un insumo con nombre, cantidad disponible y unidad, o registra el uso de una cantidad de un insumo existente.
  2. El sistema actualiza el stock disponible restando la cantidad usada.
  3. El sistema muestra el stock actualizado.
- **Resultado esperado:** tras registrar el uso de 26 unidades de un stock de 30, el sistema muestra 4 disponibles.
- **Casos alternos a verificar:**
  - Si el uso registrado dejaría el stock en un valor negativo, el sistema advierte antes de permitir guardar (regla de negocio de CU-05).
  - Tras actualizar el stock, el sistema verifica si quedó por debajo del umbral configurado y dispara la alerta de bajo stock (RF-08, RF-30).
- **Prioridad:** Must have.

### CP-RF-08 — Alertas automáticas de bajo stock (verifica RF-08)

- **Objetivo:** confirmar que alertas automáticas de bajo stock se comporta segun el criterio de verificacion definido para RF-08.
- **Precondicion:** umbral definido para el insumo.
- **Datos de entrada:** umbral configurado, stock actual.
- **Pasos:**
  1. Tras cada actualización de stock de un insumo (RF-07), el sistema compara el nuevo stock contra el umbral mínimo configurado (RF-30).
  2. Si el stock quedó por debajo del umbral, el sistema genera una notificación al responsable del insumo.
  3. El sistema registra el envío de la notificación.
- **Resultado esperado:** al bajar del umbral, la notificación se envía en menos de 5 minutos.
- **Casos alternos a verificar:**
  - Si el insumo no tiene un umbral configurado todavía, el sistema no dispara la alerta hasta que el Técnico lo defina (RF-30).
  - Si la notificación no puede entregarse por falta de conectividad, el sistema reintenta hasta la reconexión del dispositivo (ver RNF-15).
- **Prioridad:** Must have.

### CP-RF-09 — Alerta de plagas/enfermedades asistida por IA con verificación humana obligatoria (verifica RF-09)

- **Objetivo:** confirmar que alerta de plagas/enfermedades asistida por ia con verificación humana obligatoria se comporta segun el criterio de verificacion definido para RF-09.
- **Precondicion:** modelo de IA entrenado disponible.
- **Datos de entrada:** datos del lote, histórico de tratamientos.
- **Pasos:**
  1. El sistema de IA analiza los datos del lote (histórico de tratamientos y, opcionalmente, una foto) y genera una sugerencia de posible plaga/enfermedad con su justificación.
  2. El sistema notifica al usuario responsable, marcando explícitamente la sugerencia como "a confirmar en campo", nunca como diagnóstico automático.
  3. El usuario revisa la justificación y elige "confirmar" o "descartar".
  4. El sistema registra la decisión del usuario junto con la alerta.
- **Resultado esperado:** ninguna alerta se aplica automáticamente a un lote sin que el usuario responsable la confirme.
- **Casos alternos a verificar:**
  - El usuario descarta la sugerencia; el sistema la deja registrada como descartada, sin aplicar ninguna acción sobre el lote.
  - El usuario, en desacuerdo con la recomendación, la registra formalmente en la bandeja de sugerencias en vez de solo confirmar/descartar (RF-33).
  - En ningún caso la alerta se aplica automáticamente al lote sin la confirmación explícita del usuario responsable (regla de negocio central de RF-09).
- **Prioridad:** Must have.

### CP-RF-10 — Diagnóstico de plagas por imagen (IA) (verifica RF-10)

- **Objetivo:** confirmar que diagnóstico de plagas por imagen (ia) se comporta segun el criterio de verificacion definido para RF-10.
- **Precondicion:** conexión a internet.
- **Datos de entrada:** foto (JPG/PNG).
- **Pasos:**
  1. El Jornalero sube una foto (JPG/PNG) de una hoja o fruto desde el módulo de alerta de plagas (CU-06).
  2. El sistema procesa la imagen y genera una sugerencia de plaga/enfermedad probable junto con el tratamiento recomendado.
  3. El sistema responde en menos de 10 segundos y registra el resultado en el historial del lote.
- **Resultado esperado:** el sistema responde con una sugerencia en menos de 10 segundos tras subir la foto.
- **Casos alternos a verificar:**
  - Si no hay conexión a internet, el sistema informa que el diagnóstico por imagen no está disponible en ese momento (precondición de RF-10).
  - El resultado del diagnóstico por imagen sigue el mismo flujo de confirmación humana obligatoria que RF-09: se muestra como sugerencia, nunca como diagnóstico definitivo.
- **Prioridad:** Could have.

### CP-RF-11 — Asignación y seguimiento de tareas (verifica RF-11)

- **Objetivo:** confirmar que asignación y seguimiento de tareas se comporta segun el criterio de verificacion definido para RF-11.
- **Precondicion:** trabajador registrado.
- **Datos de entrada:** lote, trabajador, fecha, tipo de tarea.
- **Pasos:**
  1. El usuario asigna una tarea a un trabajador, indicando lote, fecha y tipo de tarea.
  2. El sistema crea la tarea en estado "pendiente" y la muestra con su estado.
  3. El trabajador actualiza el estado de la tarea (pendiente → en proceso → bloqueado → completado) conforme avanza.
  4. El sistema permite filtrar la lista de tareas por cualquiera de los 4 estados.
- **Resultado esperado:** al filtrar por "pendiente" el sistema solo muestra tareas en ese estado.
- **Casos alternos a verificar:**
  - Si el lote tiene un riesgo laboral registrado (CU-11), el sistema muestra la advertencia de equipo de protección antes de confirmar la asignación.
  - Al filtrar por un estado, el sistema muestra exclusivamente las tareas en ese estado, sin mezclar lotes ni trabajadores (criterio de verificación de RF-11).
- **Prioridad:** Must have.

### CP-RF-12 — Notificación móvil de tareas asignadas (verifica RF-12)

- **Objetivo:** confirmar que notificación móvil de tareas asignadas se comporta segun el criterio de verificacion definido para RF-12.
- **Precondicion:** trabajador con dispositivo registrado.
- **Datos de entrada:** asignación de tarea.
- **Pasos:**
  1. Al asignarse una tarea (RF-11), el sistema identifica el dispositivo registrado del trabajador.
  2. El sistema envía una notificación push/SMS con el lote, la fecha y el tipo de tarea.
  3. El trabajador recibe la notificación en su dispositivo.
- **Resultado esperado:** la notificación incluye lote, fecha y tipo de tarea en el mensaje.
- **Casos alternos a verificar:**
  - Si el trabajador no tiene un dispositivo registrado, el sistema deja la tarea visible en su vista de pendientes (RF-27) aunque no pueda enviar la notificación push.
- **Prioridad:** Should have.

### CP-RF-13 — Registro de motivo de rechazo/pérdida de fruta (verifica RF-13)

- **Objetivo:** confirmar que registro de motivo de rechazo/pérdida de fruta se comporta segun el criterio de verificacion definido para RF-13.
- **Precondicion:** cosecha registrada ese día.
- **Datos de entrada:** lote, fecha, cantidad rechazada, motivo.
- **Pasos:**
  1. El Jornalero, tras registrar la cosecha del día (RF-04), registra la cantidad de fruta rechazada y su motivo (enfermedad, plaga, daño mecánico).
  2. El sistema resta automáticamente la cantidad rechazada del total aprovechable del lote.
- **Resultado esperado:** el total de fruta aprovechable excluye automáticamente lo marcado como rechazado.
- **Casos alternos a verificar:**
  - Si no hay una cosecha registrada ese día, el sistema no permite registrar un rechazo asociado (precondición de RF-13).
- **Prioridad:** Should have.

### CP-RF-14 — Trazabilidad de lote de exportación (verifica RF-14)

- **Objetivo:** confirmar que trazabilidad de lote de exportación se comporta segun el criterio de verificacion definido para RF-14.
- **Precondicion:** lote marcado como "exportación".
- **Datos de entrada:** color de cinta, semana de enfunde, calidad de caja.
- **Pasos:**
  1. Para un lote marcado como "exportación" (RF-01), el usuario registra color de cinta, semana de enfunde y calidad de caja al momento de la cosecha (RF-04).
  2. El sistema guarda la ficha de trazabilidad asociada al lote de exportación.
  3. Dado un número de caja, el sistema recupera el lote, la fecha de enfunde y el color de cinta correspondiente (criterio de verificación de RF-14).
- **Resultado esperado:** dado un número de caja, el sistema recupera el lote, la fecha de enfunde y el color de cinta correspondiente.
- **Casos alternos a verificar:**
  - Si el lote no está marcado como "exportación", el sistema no solicita estos campos adicionales.
- **Prioridad:** Should have.

### CP-RF-15 — Consulta de precio de mercado y estimación de ingreso (verifica RF-15)

- **Objetivo:** confirmar que consulta de precio de mercado y estimación de ingreso se comporta segun el criterio de verificacion definido para RF-15.
- **Precondicion:** cantidad de cosecha registrada.
- **Datos de entrada:** cantidad cosechada, precio de mercado (manual o de fuente externa).
- **Pasos:**
  1. Tras registrar una cosecha (RF-04), el usuario consulta el precio de mercado vigente del cultivo.
  2. El sistema calcula el ingreso estimado como la cantidad cosechada multiplicada por el precio ingresado.
  3. El sistema muestra la estimación al usuario.
- **Resultado esperado:** ingreso estimado es igual a cantidad multiplicada por precio ingresado, validado con un caso de prueba.
- **Casos alternos a verificar:**
  - Si no hay un precio de mercado disponible de fuente externa, el usuario puede ingresarlo manualmente para obtener la estimación.
- **Prioridad:** Could have.

### CP-RF-16 — Registro de condición climática/estado del lote (verifica RF-16)

- **Objetivo:** confirmar que registro de condición climática/estado del lote se comporta segun el criterio de verificacion definido para RF-16.
- **Precondicion:** ninguna.
- **Datos de entrada:** condición climática, observación de acceso.
- **Pasos:**
  1. Al registrar una actividad o visitar un lote (CU-01), el usuario anota la condición climática (lluvia/sol) y una observación de accesibilidad del terreno.
  2. El sistema guarda el dato como campo adicional del registro de actividad/parcela.
- **Resultado esperado:** el campo de clima aparece disponible en el formulario de registro de parcela/actividad.
- **Casos alternos a verificar:**
  - El usuario puede registrar la condición climática en cualquier momento posterior, no solo al crear el registro (flujo alternativo documentado en CU-01).
- **Prioridad:** Could have.

### CP-RF-17 — Canal de reporte rápido tipo chat/voz (verifica RF-17)

- **Objetivo:** confirmar que canal de reporte rápido tipo chat/voz se comporta segun el criterio de verificacion definido para RF-17.
- **Precondicion:** usuario autenticado.
- **Datos de entrada:** nota de voz o texto corto.
- **Pasos:**
  1. El Jornalero abre el canal de reporte rápido desde la pantalla principal.
  2. Registra un mensaje corto (texto o nota de voz) describiendo una novedad de campo.
  3. El sistema envía el reporte al responsable del lote en un máximo de 2 toques desde la pantalla principal (criterio de verificación de RF-17).
- **Resultado esperado:** el reporte se envía en máximo 2 toques desde la pantalla principal.
- **Casos alternos a verificar:**
  - Si el reporte describe una posible plaga cuarentenaria, el sistema sugiere escalarlo como aviso fitosanitario formal (RF-37, CU-14).
- **Prioridad:** Could have.

### CP-RF-18 — Registro de riesgo/seguridad laboral por lote (verifica RF-18)

- **Objetivo:** confirmar que registro de riesgo/seguridad laboral por lote se comporta segun el criterio de verificacion definido para RF-18.
- **Precondicion:** ninguna.
- **Datos de entrada:** tipo de riesgo, lote, equipo de protección recomendado.
- **Pasos:**
  1. El Técnico marca un lote con un riesgo laboral (fauna peligrosa, terreno inestable), indicando el equipo de protección personal sugerido.
  2. Al asignar una tarea en ese lote (RF-11), el sistema muestra la advertencia de riesgo antes de confirmar la asignación.
- **Resultado esperado:** al asignar una tarea en un lote marcado con riesgo, el sistema muestra la advertencia antes de confirmar.
- **Casos alternos a verificar:**
  - Ninguna tarea sobre un lote con riesgo registrado puede confirmarse sin que la advertencia de equipo de protección se haya mostrado primero (regla de negocio de CU-11).
- **Prioridad:** Should have.

### CP-RF-19 — Reportes de producción, costos y pérdidas con gráficos (verifica RF-19)

- **Objetivo:** confirmar que reportes de producción, costos y pérdidas con gráficos se comporta segun el criterio de verificacion definido para RF-19.
- **Precondicion:** existen datos en el rango seleccionado.
- **Datos de entrada:** rango de fechas, lote o lotes.
- **Pasos:**
  1. El Administrador o Técnico selecciona un rango de fechas y uno o más lotes.
  2. El sistema consolida producción, costos, pérdidas por plaga y rendimiento del rango seleccionado.
  3. El sistema genera gráficos de barra y circulares codificados por color, reflejando exactamente la suma de los registros del rango.
- **Resultado esperado:** el reporte generado refleja exactamente la suma de los registros del rango de fechas seleccionado.
- **Casos alternos a verificar:**
  - Si no existen datos en el rango seleccionado, el sistema muestra "no hay datos disponibles" en vez de un reporte vacío (criterio de verificación de RF-19).
- **Prioridad:** Must have.

### CP-RF-20 — Gestión de usuarios y control de acceso (verifica RF-20)

- **Objetivo:** confirmar que gestión de usuarios y control de acceso se comporta segun el criterio de verificacion definido para RF-20.
- **Precondicion:** usuario previamente registrado.
- **Datos de entrada:** usuario, contraseña.
- **Pasos:**
  1. El usuario ingresa su usuario y contraseña.
  2. El sistema valida las credenciales y determina el rol (Administrador, Técnico, Jornalero).
  3. El sistema concede acceso únicamente a las funciones correspondientes a ese rol.
- **Resultado esperado:** un usuario con rol "jornalero" no puede acceder al módulo financiero.
- **Casos alternos a verificar:**
  - Si las credenciales son inválidas, el sistema niega el acceso.
  - Si un usuario con rol "jornalero" intenta acceder al módulo financiero, el sistema le niega el acceso (criterio de verificación de RF-20).
- **Prioridad:** Must have.

### CP-RF-21 — Registro de visitas técnicas periódicas (verifica RF-21)

- **Objetivo:** confirmar que registro de visitas técnicas periódicas se comporta segun el criterio de verificacion definido para RF-21.
- **Precondicion:** ninguna.
- **Datos de entrada:** fecha de visita, informe, próxima fecha estimada.
- **Pasos:**
  1. El Técnico registra una visita técnica: fecha, hallazgos e informe adjunto.
  2. El sistema guarda la visita y la asocia al historial de cumplimiento del lote.
  3. 15 días después, el sistema genera automáticamente un recordatorio de la siguiente visita (criterio de verificación de RF-21).
- **Resultado esperado:** 15 días después de una visita registrada, el sistema genera un recordatorio automático.
- **Casos alternos a verificar:**
  - Si la visita encuentra un incumplimiento, el sistema sugiere registrar la capacitación o el equipo de protección relacionado (CU-11, CU-13).
- **Prioridad:** Should have.

### CP-RF-22 — Registro de consentimiento del trabajador para el tratamiento de sus datos personales dentro del sistema (verifica RF-22)

- **Objetivo:** confirmar que registro de consentimiento del trabajador para el tratamiento de sus datos personales dentro del sistema se comporta segun el criterio de verificacion definido para RF-22.
- **Pasos:**
  1. En el primer inicio de sesión de un trabajador (CU-09), el sistema muestra el aviso de tratamiento de datos personales (LOPDP Art. 8).
  2. El usuario acepta el consentimiento de forma libre, específica, informada e inequívoca.
  3. El sistema registra el consentimiento antes de continuar con cualquier otro módulo.
- **Resultado esperado:** El sistema registra el consentimiento antes de continuar con cualquier otro módulo.
- **Casos alternos a verificar:**
  - Si el usuario no acepta el aviso, el sistema no concede acceso a ningún módulo que trate datos personales (regla de negocio de CU-09).
- **Prioridad:** Must have (regulatorio).

### CP-RF-23 — Módulo de derechos ARCO+ del trabajador (verifica RF-23)

- **Objetivo:** confirmar que módulo de derechos arco+ del trabajador se comporta segun el criterio de verificacion definido para RF-23.
- **Pasos:**
  1. El trabajador, autenticado en el sistema, solicita acceder, rectificar o eliminar sus propios datos personales desde Ajustes → Mis Datos.
  2. El sistema atiende la solicitud sobre los datos del propio usuario.
  3. El sistema deja un registro de la acción realizada (criterio de verificación derivado de C10, LOPDP Art. 13-19).
- **Resultado esperado:** El sistema deja un registro de la acción realizada (criterio de verificación derivado de C10, LOPDP Art. 13-19).
- **Casos alternos a verificar:**
  - Si la solicitud es de eliminación y existen datos que deben conservarse por obligación legal (por ejemplo, trazabilidad BPA), el sistema informa al usuario cuáles datos no pueden eliminarse y por qué.
- **Prioridad:** Must have (regulatorio).

### CP-RF-24 — Registro de certificado de salud del trabajador que aplica agroquímicos (verifica RF-24)

- **Objetivo:** confirmar que registro de certificado de salud del trabajador que aplica agroquímicos se comporta segun el criterio de verificacion definido para RF-24.
- **Pasos:**
  1. Antes de asignar una tarea de aplicación de agroquímicos (CU-11), el Administrador registra el certificado de salud vigente del trabajador.
  2. El sistema adjunta el certificado al perfil del trabajador.
- **Resultado esperado:** El sistema adjunta el certificado al perfil del trabajador.
- **Casos alternos a verificar:**
  - Si el trabajador no tiene certificado de salud vigente registrado, el sistema advierte que el certificado no está registrado al intentar asignarle esa tarea (Res. AGROCALIDAD 183, Art. 33-34).
- **Prioridad:** Must have (regulatorio).

### CP-RF-25 — Registro y seguimiento del proceso de certificación BPA ante AGROCALIDAD (verifica RF-25)

- **Objetivo:** confirmar que registro y seguimiento del proceso de certificación bpa ante agrocalidad se comporta segun el criterio de verificacion definido para RF-25.
- **Pasos:**
  1. El Administrador revisa el panel de cumplimiento (vigencia del certificado BPA, capacitaciones pendientes, bitácora de bioseguridad) (CU-13).
  2. Si el certificado está por vencer o falta evidencia de respaldo, solicita la renovación ante AGROCALIDAD.
  3. El sistema adjunta como evidencia los registros de capacitación y la bitácora de bioseguridad.
- **Resultado esperado:** El sistema adjunta como evidencia los registros de capacitación y la bitácora de bioseguridad.
- **Casos alternos a verificar:**
  - Si falta una capacitación obligatoria, el sistema bloquea la solicitud de renovación hasta que se registre (RF-36, RF-39).
- **Prioridad:** Should have (regulatorio).

### CP-RF-26 — Registro manual de ingresos y egresos (verifica RF-26)

- **Objetivo:** confirmar que registro manual de ingresos y egresos se comporta segun el criterio de verificacion definido para RF-26.
- **Precondicion:** usuario autenticado.
- **Datos de entrada:** concepto, monto, fecha, tipo (ingreso/egreso).
- **Pasos:**
  1. El usuario autenticado abre el módulo de registro manual de ingresos/egresos.
  2. Registra concepto, monto, fecha y tipo (ingreso/egreso), de forma independiente al cálculo automático de RF-06.
  3. El sistema guarda el movimiento en el listado.
- **Resultado esperado:** un ingreso o egreso registrado manualmente aparece reflejado en el reporte financiero del periodo correspondiente.
- **Casos alternos a verificar:**
  - El movimiento registrado manualmente se refleja de inmediato en el reporte financiero del periodo correspondiente (criterio de verificación de RF-26).
- **Prioridad:** Must have.

### CP-RF-27 — Vista de tareas pendientes por trabajador (verifica RF-27)

- **Objetivo:** confirmar que vista de tareas pendientes por trabajador se comporta segun el criterio de verificacion definido para RF-27.
- **Precondicion:** existen tareas asignadas al usuario.
- **Datos de entrada:** usuario autenticado.
- **Pasos:**
  1. El trabajador autenticado abre su vista de tareas pendientes.
  2. El sistema muestra únicamente las tareas asignadas a ese trabajador.
- **Resultado esperado:** un trabajador con 3 tareas pendientes ve exactamente esas 3 al abrir la vista, sin tareas de otros lotes o trabajadores.
- **Casos alternos a verificar:**
  - Un trabajador con 3 tareas pendientes ve exactamente esas 3 al abrir la vista, sin tareas de otros lotes o trabajadores (criterio de verificación de RF-27).
- **Prioridad:** Should have.

### CP-RF-28 — Campo de observaciones en el registro de tareas (verifica RF-28)

- **Objetivo:** confirmar que campo de observaciones en el registro de tareas se comporta segun el criterio de verificacion definido para RF-28.
- **Precondicion:** tarea existente.
- **Datos de entrada:** texto libre.
- **Pasos:**
  1. El trabajador, al marcar una tarea como completada (RF-11), adjunta una nota u observación de texto libre.
  2. El sistema asocia la observación a la tarea.
- **Resultado esperado:** la observación ingresada aparece al consultar el detalle de la tarea.
- **Casos alternos a verificar:**
  - La observación ingresada permanece visible al consultar el detalle de la tarea en cualquier momento posterior (criterio de verificación de RF-28).
- **Prioridad:** Could have.

### CP-RF-29 — Historial completo por parcela (verifica RF-29)

- **Objetivo:** confirmar que historial completo por parcela se comporta segun el criterio de verificacion definido para RF-29.
- **Precondicion:** la parcela tiene al menos un evento registrado.
- **Datos de entrada:** identificador de parcela.
- **Pasos:**
  1. El usuario selecciona una parcela y abre su vista de historial.
  2. El sistema agrega actividades, tratamientos y cosechas de esa parcela a lo largo del tiempo.
  3. El sistema muestra los eventos ordenados cronológicamente.
- **Resultado esperado:** al consultar el historial de una parcela con 5 eventos registrados en distintas fechas, los 5 aparecen ordenados cronológicamente.
- **Casos alternos a verificar:**
  - Si la parcela no tiene ningún evento registrado, el sistema muestra el historial vacío en vez de un error (precondición de RF-29).
- **Prioridad:** Should have.

### CP-RF-30 — Umbral de stock mínimo configurable por insumo (verifica RF-30)

- **Objetivo:** confirmar que umbral de stock mínimo configurable por insumo se comporta segun el criterio de verificacion definido para RF-30.
- **Precondicion:** insumo ya registrado.
- **Datos de entrada:** cantidad mínima por insumo.
- **Pasos:**
  1. El Técnico abre la ficha de un insumo ya registrado.
  2. Define el valor numérico de stock mínimo (stock limit) para ese insumo.
  3. El sistema guarda el umbral y lo deja disponible para el mecanismo de alertas (RF-08).
- **Resultado esperado:** al bajar el stock del insumo por debajo del valor configurado, se dispara la alerta de RF-08.
- **Casos alternos a verificar:**
  - El Técnico puede editar el umbral en cualquier momento; el nuevo valor se aplica desde la siguiente actualización de stock.
- **Prioridad:** Should have.

### CP-RF-31 — Detección de valores atípicos al ingresar datos (verifica RF-31)

- **Objetivo:** confirmar que detección de valores atípicos al ingresar datos se comporta segun el criterio de verificacion definido para RF-31.
- **Precondicion:** existe histórico suficiente del lote (mínimo 3 registros previos).
- **Datos de entrada:** valor ingresado, histórico del lote.
- **Pasos:**
  1. El usuario ingresa un dato numérico (por ejemplo, cantidad cosechada) para un lote con histórico suficiente (mínimo 3 registros previos).
  2. El sistema compara el valor contra el promedio histórico del mismo lote.
  3. Si el valor se desvía más de 2 desviaciones estándar del promedio, el sistema muestra una advertencia antes de guardar.
- **Resultado esperado:** un valor que se desvía más de 2 desviaciones estándar del promedio histórico dispara la advertencia antes de guardar.
- **Casos alternos a verificar:**
  - El usuario confirma el dato pese a la advertencia (si el valor atípico es real), o lo corrige antes de guardar (postcondición de RF-31).
  - Si el lote no tiene histórico suficiente, el sistema guarda el dato sin comparar (precondición de RF-31).
- **Prioridad:** Could have.

### CP-RF-32 — Vía de integración futura con sensores de campo (verifica RF-32)

- **Estado:** no aplica en esta version. RF-32 es Won't have (via de integracion futura con sensores de campo); queda documentado como trabajo futuro, sin caso de prueba ejecutable en esta entrega.

### CP-RF-33 — Bandeja de sugerencias para disputar una recomendación de IA (verifica RF-33)

- **Objetivo:** confirmar que bandeja de sugerencias para disputar una recomendación de ia se comporta segun el criterio de verificacion definido para RF-33.
- **Precondicion:** existe una recomendación de IA previa.
- **Datos de entrada:** recomendación en cuestión, comentario del usuario.
- **Pasos:**
  1. El usuario, en desacuerdo con una recomendación de IA previa (RF-09/RF-10), abre la bandeja de sugerencias.
  2. Registra su comentario asociado a esa recomendación.
  3. El sistema guarda el desacuerdo, visible para revisión posterior del equipo técnico.
- **Resultado esperado:** un desacuerdo registrado aparece en un listado consultable, con la fecha y el comentario del usuario.
- **Casos alternos a verificar:**
  - El desacuerdo registrado aparece en un listado consultable con fecha y comentario del usuario (criterio de verificación de RF-33), sin alterar el estado de la alerta original.
- **Prioridad:** Should have.

### CP-RF-34 — Esquema de atributos configurable por variedad de cultivo (verifica RF-34)

- **Objetivo:** confirmar que esquema de atributos configurable por variedad de cultivo se comporta segun el criterio de verificacion definido para RF-34.
- **Precondicion:** variedad dada de alta en el catálogo con su set de atributos.
- **Datos de entrada:** variedad seleccionada.
- **Pasos:**
  1. El Técnico da de alta una variedad de cultivo en el catálogo (RF-02), definiendo el conjunto de campos y atributos propios de esa variedad.
  2. Al seleccionar esa variedad en un formulario (por ejemplo, CU-01), el sistema muestra el conjunto de campos correspondiente.
- **Resultado esperado:** al seleccionar una variedad de cacao, el formulario muestra un conjunto de campos distinto al que se muestra al seleccionar plátano.
- **Casos alternos a verificar:**
  - Al seleccionar una variedad de cacao, el formulario muestra un conjunto de campos distinto al que se muestra al seleccionar plátano (criterio de verificación de RF-34).
- **Prioridad:** Must have.

### CP-RF-35 — Registro de análisis de suelo previo a siembra (verifica RF-35)

- **Objetivo:** confirmar que registro de análisis de suelo previo a siembra se comporta segun el criterio de verificacion definido para RF-35.
- **Precondicion:** parcela registrada.
- **Datos de entrada:** tipo de suelo, resultado de aptitud, fecha del análisis.
- **Pasos:**
  1. El Técnico registra, para una parcela ya existente, el resultado de un análisis de suelo (calicata) previo a la siembra: tipo de suelo, aptitud y fecha.
  2. El sistema guarda la ficha de análisis de suelo asociada a la parcela.
- **Resultado esperado:** una parcela con análisis de suelo registrado muestra el resultado de aptitud al consultar su ficha.
- **Casos alternos a verificar:**
  - Una parcela con análisis de suelo registrado muestra el resultado de aptitud al consultar su ficha, antes de aprobar la siembra (criterio de verificación de RF-35).
- **Prioridad:** Could have.

### CP-RF-36 — Registro de capacitación en manejo de plaguicidas y primeros auxilios (verifica RF-36)

- **Objetivo:** confirmar que registro de capacitación en manejo de plaguicidas y primeros auxilios se comporta segun el criterio de verificacion definido para RF-36.
- **Pasos:**
  1. El Administrador registra una capacitación en manejo de plaguicidas o primeros auxilios recibida por un trabajador.
  2. El sistema guarda el registro como evidencia de respaldo para la certificación BPA (RF-25, CU-13).
- **Resultado esperado:** El sistema guarda el registro como evidencia de respaldo para la certificación BPA (RF-25, CU-13).
- **Casos alternos a verificar:**
  - Si la capacitación registrada está vencida o incompleta, el sistema la marca como pendiente en el panel de cumplimiento (CU-13).
- **Prioridad:** Should have (regulatorio).

### CP-RF-37 — Aviso/alerta ante síntomas sospechosos de plaga cuarentenaria (ej. Moko) (verifica RF-37)

- **Objetivo:** confirmar que aviso/alerta ante síntomas sospechosos de plaga cuarentenaria (ej. moko) se comporta segun el criterio de verificacion definido para RF-37.
- **Pasos:**
  1. Un usuario de campo detecta síntomas sospechosos de plaga cuarentenaria (ej. Moko) en un lote.
  2. Registra el síntoma y el lote afectado en el sistema.
  3. El sistema genera el aviso fitosanitario y lo marca con prioridad alta, visible de inmediato para el Administrador.
  4. Un Técnico confirma el síntoma tras la inspección.
- **Resultado esperado:** Un Técnico confirma el síntoma tras la inspección.
- **Casos alternos a verificar:**
  - El Técnico descarta el síntoma tras la inspección; el aviso no se envía a AGROCALIDAD, pero queda registrado como descartado para trazabilidad (CU-14).
- **Prioridad:** Must have (regulatorio). Nota: EV-17 mencionó el problema del Moko y las medidas de desinfección, pero ningún entrevistado describió el mecanismo formal de aviso a AGROCALIDAD, por eso sigue siendo un vacío..

### CP-RF-38 — Bitácora de bioseguridad de ingreso/salida del predio (verifica RF-38)

- **Objetivo:** confirmar que bitácora de bioseguridad de ingreso/salida del predio se comporta segun el criterio de verificacion definido para RF-38.
- **Pasos:**
  1. Al confirmarse una visita al predio (técnica o por síntoma sospechoso, CU-10/CU-14), el usuario registra el evento de ingreso/salida en la bitácora de bioseguridad.
  2. El sistema guarda el registro con fecha y motivo de la visita.
- **Resultado esperado:** El sistema guarda el registro con fecha y motivo de la visita.
- **Casos alternos a verificar:**
  - La bitácora queda disponible como evidencia de respaldo para la certificación BPA y para la auditoría de AGROCALIDAD (RF-25, CU-13).
- **Prioridad:** Should have (regulatorio).

### CP-RF-39 — Registro de capacitaciones del personal sobre control fitosanitario específico (verifica RF-39)

- **Objetivo:** confirmar que registro de capacitaciones del personal sobre control fitosanitario específico se comporta segun el criterio de verificacion definido para RF-39.
- **Pasos:**
  1. El Administrador registra una capacitación fitosanitaria específica recibida por un trabajador (control de plagas cuarentenarias, bioseguridad).
  2. El sistema guarda el registro y lo deja disponible como evidencia de auditoría (RF-25, CU-13).
- **Resultado esperado:** El sistema guarda el registro y lo deja disponible como evidencia de auditoría (RF-25, CU-13).
- **Casos alternos a verificar:**
  - Si falta una capacitación fitosanitaria obligatoria, el sistema bloquea la solicitud de renovación BPA hasta que se registre (regla de negocio de CU-13).
- **Prioridad:** Should have (regulatorio).

## Casos de prueba — Requisitos No Funcionales

### CP-RNF-01 — Acceso móvil prioritario (Interacción con el usuario) (verifica RNF-01)

- **Objetivo:** las funciones de consulta y registro más usadas en campo (tareas, cosecha, inventario) deben estar disponibles desde un teléfono móvil, no solo desde escritorio.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el 100% de las pantallas de RF-01, RF-03, RF-04, RF-11 y RF-19 deben renderizar correctamente en una pantalla de 360x800 px sin scroll horizontal.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-02 — Interfaz simple y sin tecnicismos (Interacción con el usuario) (verifica RNF-02)

- **Objetivo:** las etiquetas de campos y menús deben usar vocabulario cotidiano del agricultor, evitando abreviaturas o nombres de columna técnicos.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** en una prueba de usabilidad con 5 jornaleros sin experiencia previa en el sistema, al menos el 90% de los términos de la interfaz deben ser comprendidos sin ayuda externa.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-03 — Usabilidad para usuarios con baja alfabetización digital (Interacción con el usuario) (verifica RNF-03)

- **Objetivo:** un usuario sin experiencia previa en aplicaciones móviles debe poder completar el registro de una cosecha sin asistencia después de una capacitación breve.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** tiempo máximo de 5 minutos de capacitación para que un jornalero sin experiencia previa registre una cosecha sin errores.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-04 — Robustez de campo ante condiciones adversas (Fiabilidad) (verifica RNF-04)

- **Objetivo:** el registro de actividades y cosecha debe seguir siendo posible sin conexión a internet, sincronizando los datos cuando la conexión se restablezca.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el sistema debe permitir guardar localmente hasta 7 días de registros sin conexión, sin pérdida de datos al reconectarse.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-05 — Explicabilidad verificable de las recomendaciones de IA (Adecuación funcional) (verifica RNF-05)

- **Objetivo:** toda recomendación de IA debe mostrar la razón de la sugerencia antes de que el usuario pueda aplicarla.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el 100% de las alertas de IA (RF-09, RF-10) deben incluir un texto de justificación de máximo 60 palabras, visible antes del botón de confirmación.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-06 — Transparencia del origen de los datos de la recomendación (Adecuación funcional) (verifica RNF-06)

- **Objetivo:** además de explicar el motivo, la recomendación debe indicar en qué datos del propio lote se basó.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el 100% de las recomendaciones deben listar al menos 1 dato de origen (por ejemplo, "basado en el registro de fumigación del 12 de agosto").
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-07 — Preservación del histórico de datos sin pérdida (Fiabilidad) (verifica RNF-07)

- **Objetivo:** ningún dato de cosecha, actividad o inventario registrado debe poder eliminarse de forma permanente sin confirmación explícita y registro de auditoría.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el sistema debe mantener un registro de auditoría de cambios/eliminaciones por al menos 24 meses.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-08 — Consentimiento explícito registrado en el primer inicio de sesión (Seguridad) (verifica RNF-08)

- **Objetivo:** todo trabajador debe aceptar un aviso de tratamiento de datos personales antes de poder usar el sistema por primera vez.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** el 100% de las cuentas activas deben tener un registro de aceptación con fecha y hora.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-09 — Seguridad de los datos personales almacenados (Seguridad, derivado legal) (verifica RNF-09)

- **Objetivo:** los datos personales de los trabajadores deben cifrarse en reposo y en tránsito.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** cifrado AES-256 en base de datos y TLS 1.2 o superior en toda comunicación cliente-servidor.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-10 — Posibilidad de disentir de una recomendación sin bloquear el flujo de trabajo (Interacción con el usuario) (verifica RNF-10)

- **Objetivo:** el usuario debe poder continuar su trabajo normalmente aunque decida no seguir una recomendación de IA, sin que el sistema se lo impida ni lo penalice.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** 0 casos en los que el sistema bloquee una acción del usuario por no aceptar una recomendación de IA.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-11 — Reducción del esfuerzo de captura manual de datos (Eficiencia de desempeño) (verifica RNF-11)

- **Objetivo:** las pantallas de registro frecuente (cosecha, actividad) deben minimizar el número de campos obligatorios y usar selección en vez de texto libre donde sea posible.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** registrar una cosecha completa debe tomar un máximo de 30 segundos en condiciones normales de campo.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-12 — Conservación mínima de registros de trazabilidad (Fiabilidad, derivado legal) (verifica RNF-12)

- **Objetivo:** los registros de actividad, cosecha y aplicación de insumos deben conservarse un mínimo de 2 años, conforme a la normativa de trazabilidad agroindustrial.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** ningún registro de los tipos mencionados puede eliminarse antes de cumplir 24 meses desde su creación.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-13 — Compatibilidad con dispositivos de gama baja (Compatibilidad) (verifica RNF-13)

- **Objetivo:** la aplicación móvil debe funcionar en equipos Android de gama baja, dado el perfil económico de los usuarios de campo.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** funcionamiento fluido (sin caídas) en un dispositivo con 2 GB de RAM y Android 9 o superior.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-14 — Extensibilidad del catálogo de cultivos y variedades (Mantenibilidad) (verifica RNF-14)

- **Objetivo:** agregar un nuevo cultivo o variedad al catálogo (RF-02, RF-34) no debe requerir cambios en el código de la aplicación, solo configuración.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** un administrador debe poder agregar una variedad nueva con su set de atributos en menos de 10 minutos, sin intervención del equipo de desarrollo.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-15 — Disponibilidad del servicio de notificaciones (Fiabilidad) (verifica RNF-15)

- **Objetivo:** las notificaciones de bajo stock y asignación de tareas deben entregarse de forma confiable incluso con conectividad intermitente.
- **Metodo de verificacion:** revision funcional dirigida durante las pruebas de aceptacion, confirmando el criterio descrito en la ficha del requisito.
- **Metrica:** 95% de las notificaciones deben entregarse dentro de los 5 minutos posteriores a la reconexión del dispositivo.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-16 — Desempeño de detección/predicción del modelo de IA (Fiabilidad del componente de IA) (verifica RNF-16)

- **Objetivo:** el modelo que sustenta RF-09 y RF-10 debe alcanzar un nivel mínimo de acierto en la detección de plagas/enfermedades antes de habilitarse en producción.
- **Metodo de verificacion:** evaluación del modelo sobre un conjunto de prueba etiquetado, ejecutada por script versionado, con matriz de confusión documentada en el repositorio.
- **Metrica:** exactitud (accuracy) y sensibilidad (recall) del modelo sobre el conjunto de validación. (porcentaje (%).)
- **Umbral de aceptacion:** ≥80% de exactitud y ≥75% de sensibilidad en el conjunto de validación, antes de habilitar el modelo en campo.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-17 — Explicabilidad de las recomendaciones de IA (Transparencia) (verifica RNF-17)

- **Objetivo:** toda alerta o recomendación generada por el componente de IA (RF-09, RF-10) debe mostrar al usuario al menos un factor que motivó la sugerencia, no solo el resultado, para que el usuario decida con criterio si confirmarla (RF-09) o disputarla (RF-33).
- **Metodo de verificacion:** revisión de una muestra de alertas generadas en pruebas de aceptación, confirmando la presencia del campo de explicación.
- **Metrica:** proporción de alertas emitidas que muestran al menos un factor explicativo (por ejemplo, "temperatura y humedad elevadas en los últimos 5 días"). (porcentaje (%) de alertas con explicación.)
- **Umbral de aceptacion:** 100% de las alertas deben mostrar al menos un factor explicativo.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-18 — Equidad de desempeño entre cultivos (Equidad) (verifica RNF-18)

- **Objetivo:** el componente de IA no debe generar sistemáticamente peor desempeño (más falsos negativos) para un cultivo respecto del otro, dado que cacao y plátano están igualmente en alcance del estudio de caso.
- **Metodo de verificacion:** evaluación separada del modelo por subconjunto (cacao, plátano) sobre el conjunto de validación, con reporte comparativo versionado.
- **Metrica:** diferencia en la tasa de falsos negativos entre cacao y plátano. (puntos porcentuales de diferencia.)
- **Umbral de aceptacion:** diferencia ≤10 puntos porcentuales en la tasa de falsos negativos entre ambos cultivos.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-19 — Supervisión humana obligatoria antes de cualquier acción automática (Supervisión humana) (verifica RNF-19)

- **Objetivo:** formaliza como requisito transversal lo que RF-09 ya exige en su flujo: ninguna alerta o recomendación de IA puede ejecutar una acción sobre los datos del sistema sin confirmación explícita de una persona.
- **Metodo de verificacion:** revisión de logs de auditoría y prueba funcional dirigida a intentar forzar una aplicación automática.
- **Metrica:** número de acciones aplicadas automáticamente sobre datos del sistema sin confirmación humana. (conteo de incidentes.)
- **Umbral de aceptacion:** 0 acciones automáticas sin confirmación humana.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-20 — Monitoreo continuo del desempeño del modelo en producción (Monitoreo) (verifica RNF-20)

- **Objetivo:** el sistema debe registrar, para cada alerta de IA, si el usuario la confirmó, la descartó (RF-09) o la disputó (RF-33), para poder calcular el desempeño real del modelo en campo y no solo en el conjunto de prueba.
- **Metodo de verificacion:** consulta sobre el registro de alertas y su estado, generada por script versionado.
- **Metrica:** proporción de alertas emitidas con retroalimentación registrada (confirmada, descartada o disputada). (porcentaje (%).)
- **Umbral de aceptacion:** ≥90% de las alertas deben tener retroalimentación registrada dentro de los 7 días de emitidas.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.

### CP-RNF-21 — Clasificación de riesgo de las recomendaciones de IA (Gestión de riesgo) (verifica RNF-21)

- **Objetivo:** cada tipo de alerta o recomendación del componente de IA debe clasificarse por nivel de riesgo (bajo, medio, alto) según el impacto potencial de seguirla sin verificación —por ejemplo, aplicar un agroquímico implica mayor riesgo que una sugerencia de riego— y ese nivel debe ser visible al usuario junto a la alerta.
- **Metodo de verificacion:** revisión de la tabla de configuración de tipos de alerta, confirmando el campo de nivel de riesgo.
- **Metrica:** proporción de tipos de alerta definidos en RF-09/RF-10 con nivel de riesgo asignado y visible en la interfaz. (porcentaje (%) de tipos de alerta clasificados.)
- **Umbral de aceptacion:** 100% de los tipos de alerta deben tener un nivel de riesgo asignado antes de habilitarse.
- **Resultado esperado:** el valor medido cumple el umbral de aceptacion definido arriba; en caso contrario, el caso de prueba se marca como no superado y bloquea el cierre del requisito.
