# Especificación de Requisitos de Software (ERS/SRS)
## AgroMoreira, Sistema de Gestión Agrícola con Inteligencia Artificial

**Versión:** 2.0
**Estándar base:** ISO/IEC/IEEE 29148:2018 y ISO/IEC 25010:2023
**PFC:** #11, Categoría C, riesgo mínimo operativo. Paralelo 4to Software A
**Fecha:** 1 de septiembre de 2026

**Equipo:** Jeanpierre Robinson Espinoza, líder. Danela Dayana Arteaga Álava, diseño y modelado UML. Kamila Annabella Calle Delgado, analista de requerimientos. María del Rosario Escudero Plaza, investigación experimental y análisis estadístico. Roselyn Andreina Sánchez Centeno, gestión del repositorio.
**Docente supervisor:** Ing. Gleiston Cicerón Guerrero Ulloa, PhD

### Historial de versiones

| Versión | Fecha | Cambios | Autor |
|---|---|---|---|
| 1.0 | 30 de agosto de 2026 | Esqueleto inicial del documento, sin trabajo de campo todavía | Equipo AgroMoreira |
| 1.1 | 31 de agosto de 2026 | Corrección del equipo y del enfoque metodológico a partir del expediente ético real | Equipo AgroMoreira |
| 1.2 | 1 de septiembre de 2026 | Corrección del liderazgo del equipo | Equipo AgroMoreira |
| 1.3 | 1 de septiembre de 2026 | Definición del enfoque legal-first como enfoque oficial del proyecto | Equipo AgroMoreira |
| 2.0 | 1 de septiembre de 2026 | Cierre de la Sección 3 con los 39 requisitos funcionales y los 21 requisitos no funcionales obtenidos en las 17 entrevistas y las 7 sesiones de validación, y de las historias de usuario con criterios de aceptación para los 17 requisitos Must have. Cierre del modelado del sistema en la Sección 4, con los 14 casos de uso, los dos diagramas de clases, los diagramas de comportamiento, la arquitectura de componentes y los 9 mockups de `03_Modelado/`. Matriz de trazabilidad cerrada en 60 filas y Sección 6 con el producto mínimo viable funcional | Equipo AgroMoreira |

---

## 1. Introducción

### 1.1 Propósito

Este documento especifica los requisitos funcionales y no funcionales del Sistema de Gestión Agrícola con Inteligencia Artificial para Agrícola Moreira, finca de policultivo dedicada al cacao y al plátano verde. El componente empírico del proyecto sigue el enfoque legal-first de Amaral, Abualhaija, Sabetzadeh y Briand (2021). A partir de un modelo conceptual de cumplimiento legal organizado en tres bloques normativos, la Ley Orgánica de Protección de Datos Personales del Ecuador, la Resolución 183 de AGROCALIDAD sobre buenas prácticas y trazabilidad del cacao, y la Resolución 0072 sobre bioseguridad y manejo fitosanitario, se definieron 26 criterios de cumplimiento documentados en `Modelo_Legal_LOPDP.md`. El trabajo de campo permitió evaluar cuáles de esos criterios quedaban cubiertos por los requisitos obtenidos mediante entrevistas convencionales y cuáles solo se cubren cuando se derivan requisitos directamente del texto legal.

### 1.2 Alcance

El sistema cubre la centralización del registro de parcelas, cultivos y variedades, el registro de actividades agrícolas y cosechas, la gestión del inventario de insumos, la asignación y el seguimiento de tareas, la generación de reportes de producción y costos, y un módulo de alertas de plagas asistido por inteligencia artificial que siempre requiere confirmación humana antes de aplicarse a un lote. También cubre los requisitos de cumplimiento legal derivados del modelo de protección de datos y de la normativa agroindustrial ecuatoriana. El alcance definitivo se fijó tras las 17 entrevistas y las 9 sesiones de validación descritas en la Sección 3, y ya fue confirmado con el administrador Raúl Moreira Alay.

### 1.3 Glosario de términos

| Término | Definición |
|---|---|
| RF | Requisito Funcional |
| RNF | Requisito No Funcional |
| RD | Requisito derivado directamente del texto legal, sin evidencia de entrevista |
| Sugerencia explicable | Recomendación generada por el componente de inteligencia artificial, acompañada de una justificación comprensible para el usuario y de los datos en los que se basa, sin que el sistema ejecute la acción de forma autónoma |
| AGROCALIDAD | Agencia de Regulación y Control Fito y Zoosanitario del Ecuador |
| LOPDP | Ley Orgánica de Protección de Datos Personales del Ecuador |
| Perfil técnico | Usuario con familiaridad previa en el manejo de sistemas informáticos, como el personal de administración o los técnicos agrónomos |
| Perfil no técnico | Usuario sin familiaridad previa en sistemas informáticos, como buena parte del personal de campo |

### 1.4 Referencias

Ver `referencias.bib`. La bibliografía se amplía a medida que avanza el manuscrito y no sustituye a la del protocolo de investigación.

### 1.5 Visión general del documento

La Sección 2 describe el producto y sus interesados. La Sección 3 presenta los 39 requisitos funcionales, los 21 requisitos no funcionales y las historias de usuario con sus criterios de aceptación, todos obtenidos del trabajo de campo real. La Sección 4 recoge el modelado del sistema, con los casos de uso, los diagramas de clases, de comportamiento y de componentes, y los mockups. Las Secciones 5 y 6 describen la priorización, la trazabilidad cerrada y el producto mínimo viable.

---

## 2. Descripción general

### 2.1 Perspectiva del producto

AgroMoreira es un sistema nuevo e independiente, desarrollado específicamente para Agrícola Moreira. No reemplaza un sistema legado formal, ya que la finca lleva sus registros actuales en papel y en hojas de cálculo, según se confirmó durante las entrevistas.

### 2.2 Diagrama de contexto

```
                    +---------------------------------------+
                    |                                         |
   Propietario /    |                                         |      Técnicos de
   Administrador ---+                                         +--- AGROCALIDAD
   de la finca      |                                         |    (externo)
                    |                                         |
   Ingeniero        |                                         |
   agronomo   ------+          SISTEMA AGROMOREIRA            +---- Centro de acopio /
   residente        |   (gestion agricola + sugerencias       |     Asociacion de
                    |    de IA explicables)                   |     productores
   Capataces  ------+                                         |     (externo)
                    |                                         |
   Personal de      |                                         |
   campo      ------+                                         |
                    |                                         |
   Personal de      |                                         |
   acopio     ------+                                         |
                    +---------------------------------------+
```

La versión trazada de este diagrama es `03_Modelado/Diagrams/CTX01_Context_Diagram.drawio`, y la matriz de poder e interés es `CTX02_Power_Interest_Matrix.drawio`.

### 2.3 Mapa de stakeholders (matriz poder e interés)

| Stakeholder | Poder | Interés | Cuadrante | Rol en el proyecto |
|---|---|---|---|---|
| Propietario o administrador de la finca | Alto | Alto | Gestionar de cerca | Decide la adopción del sistema y firmó el aval institucional |
| Ingeniero agrónomo residente | Medio | Alto | Mantener informado e involucrar | Informante clave técnico y usuario del módulo de IA |
| Capataces | Medio | Medio | Mantener satisfecho | Coordina al personal de campo y usa el sistema como usuario intermedio |
| Personal de campo | Bajo | Alto | Mantener informado | Usuario final principal de las sugerencias explicables |
| Personal de acopio | Bajo | Medio | Monitorear | Usuario del módulo de trazabilidad y cosecha |
| Técnicos de AGROCALIDAD, externo | Medio | Bajo | Monitorear | Informante externo sobre requisitos normativos |
| Centro de acopio o asociación, externo | Bajo | Bajo | Monitorear | Informante externo sobre trazabilidad posterior a la cosecha |

### 2.4 Modelado organizacional i estrella

**Diagrama de dependencia estratégica, objetivos por actor**

El propietario o administrador depende del personal de campo para la ejecución correcta de las labores culturales. El personal de campo depende del sistema AgroMoreira para recibir sugerencias comprensibles y accionables sobre el manejo del cultivo. El propio sistema depende del ingeniero agrónomo para validar la calidad de esas sugerencias de inteligencia artificial. El propietario o administrador depende también del sistema para la trazabilidad y los reportes que debe presentar ante AGROCALIDAD. El personal de acopio depende del sistema para registrar la cosecha y la calidad posterior a esta.

Los diagramas de dependencia estratégica y de razón estratégica están en `03_Modelado/Diagrams/ISTAR01_Strategic_Dependency_SD.drawio` y `ISTAR02_Strategic_Rationale_SR.drawio`.

### 2.5 Entorno operativo

El personal de campo trabaja principalmente con teléfonos Android de gama baja y con poca experiencia previa en aplicaciones móviles, según se confirmó en las entrevistas a los jornaleros. La conectividad dentro de las parcelas es intermitente, lo que llevó a definir el requisito no funcional de robustez de campo de la Sección 3.3. El personal técnico y administrativo cuenta con acceso a computadores para las tareas de configuración, reporte y análisis.

### 2.6 Restricciones de diseño

El sistema debe operar con conectividad intermitente o nula en el campo, tal como confirmó el personal de campo entrevistado. Las sugerencias de inteligencia artificial deben ser explicables y en ningún caso pueden ejecutar acciones de forma autónoma sobre un lote sin confirmación humana. El sistema debe cumplir con la Ley Orgánica de Protección de Datos Personales del Ecuador, según se detalla a continuación.

### 2.7 Mapeo a la Ley Orgánica de Protección de Datos Personales del Ecuador

Fuente legal verificada. Registro Oficial, Quinto Suplemento N.º 459, del 26 de mayo de 2021.

| Artículo | Tema | Relevancia para AgroMoreira |
|---|---|---|
| Art. 7 y 8 | Tratamiento legítimo y consentimiento | El consentimiento debe ser libre, específico, informado e inequívoco, y revocable en cualquier momento. Es la base del proceso de entrevistas y del formulario de consentimiento informado |
| Art. 10, literal e | Pertinencia y minimización de datos | El sistema y el estudio solo recolectan los datos estrictamente necesarios para la gestión agrícola |
| Art. 10, literal g | Confidencialidad | El tratamiento no puede comunicarse para un fin distinto al recogido. Respalda el compromiso de confidencialidad firmado por el equipo |
| Art. 10, literal j | Seguridad de datos personales | Respalda el cifrado AES-256 de la zona restringida de evidencias |
| Art. 13 a 19 | Derechos de acceso, rectificación, eliminación, oposición y portabilidad | El sistema en su versión productiva debe soportar estos cinco derechos, recogidos en el RF-23 |
| Art. 20 | Derecho a no ser objeto de una decisión basada única o parcialmente en valoraciones automatizadas | Es el artículo más relevante para AgroMoreira. El titular puede exigir una explicación motivada sobre cualquier sugerencia del sistema, conocer los datos usados e impugnarla. Le da base legal directa a los requisitos de explicabilidad del RF-09 y de la Sección 3.3 |

### 2.8 Supuestos y dependencias

Se confirmó que Agrícola Moreira cuenta con dispositivos móviles y computadores disponibles para el personal técnico y administrativo. La colaboración del personal de campo, inicialmente asumida como voluntaria, quedó confirmada con la realización de las 17 entrevistas y las 9 sesiones de validación descritas en la Sección 3.

---
## 3. Requisitos específicos

Esta sección reúne los 39 requisitos funcionales y los 21 requisitos no funcionales del sistema, obtenidos de las 17 entrevistas semiestructuradas y de las 9 sesiones de validación con walkthrough, 4 con perfiles técnicos y 5 con perfiles no técnicos. De los 39 requisitos funcionales, 31 cuentan con evidencia directa de entrevista y 8 se derivaron directamente de los 26 criterios de cumplimiento legal descritos en `Modelo_Legal_LOPDP.md`, en sus tres bloques normativos, la Ley Orgánica de Protección de Datos Personales, la Resolución 183 de AGROCALIDAD sobre buenas prácticas y trazabilidad del cacao, y la Resolución 0072 sobre bioseguridad y manejo fitosanitario.

Cada entrevista tiene asignado un código de evidencia. EV-01 corresponde a ENTR-01, administrador. EV-02 a ENTR-02, jornalero. EV-03 a ENTR-03, jornalera. EV-04 a ENTR-04, trabajador. EV-05 y EV-06 a ENTR-05 y ENTR-06, técnicos. EV-07 a ENTR-07, técnico, en sesión de walkthrough. EV-08 a ENTR-08, jornalera, en sesión de walkthrough. EV-09 a ENTR-09, jornalero. EV-10 a ENTR-10, técnico, en sesión de walkthrough. EV-11 y EV-12 a ENTR-11 y ENTR-12, jornaleros, en sesión de walkthrough. EV-13 y EV-14 a ENTR-13 y ENTR-14, jornaleros. EV-15 a ENTR-15, jornalero, en sesión de walkthrough. EV-16 a ENTR-16, técnica, en sesión de walkthrough. EV-17 a ENTR-17, técnico. Las 17 personas entrevistadas son distintas entre sí, aunque algunas comparten nombre de pila.

### 3.1 Requisitos funcionales con evidencia de entrevista

## Requisitos Funcionales

### RF-01. Registro de parcelas/lotes
- **Descripción:** el sistema debe permitir registrar y editar una parcela/lote con: nombre/número, sector, ubicación, área, tipo de cultivo, variedad, cantidad de plantas, estado (activo/inactivo).
- **Actor/origen:** Administrador, Técnico, Jornalero. EV-01, EV-07, EV-09, EV-10, EV-11, EV-14, EV-15, EV-16
- **Entradas:** nombre, sector, ubicación, área, cultivo, variedad, N.º plantas
- **Salidas:** ficha de parcela registrada
- **Precondición:** usuario autenticado con permiso de edición
- **Postcondición:** parcela visible en el listado general
- **Flujo principal:**
  1. El usuario (Administrador, Técnico o Jornalero) autenticado con permiso de edición selecciona "Nueva parcela".
  2. Ingresa nombre/número, sector, ubicación, área, cultivo, variedad y cantidad de plantas.
  3. El sistema valida que los 7 campos obligatorios estén completos.
  4. El sistema guarda la parcela y la muestra en el listado general en menos de 2 segundos.
- **Flujos alternativos / excepciones:**
  - Si falta alguno de los 7 campos obligatorios, el sistema rechaza el guardado y marca los campos vacíos (criterio de verificación de RF-01).
  - Si la parcela se marca como "para exportación", el sistema habilita los campos de trazabilidad de exportación (ver RF-14, CU-03).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** al crear una parcela con los 7 campos obligatorios, el sistema la muestra en el listado en menos de 2 segundos, sin campos vacíos.
- **Evidencia textual:** *"Saber exactamente el lote por su nombre y número, qué cultivo tiene y cuántas plantas han sido o están en tratamiento"* (EV-15). *"Los datos deberían ser el código, el tamaño, el cultivo y la ubicación"* (EV-16).

### RF-02. Catálogo cerrado de cultivos y variedades
- **Descripción:** el sistema debe ofrecer una lista predefinida y editable por el administrador de cultivos (cacao, plátano, palma, y ampliable) y sus variedades, sin permitir texto libre tipo "otros".
- **Actor/origen:** Jornalero, Técnico. EV-10, EV-11, EV-12
- **Entradas:** selección de cultivo/variedad desde catálogo
- **Salidas:** cultivo/variedad asociado a la parcela
- **Precondición:** catálogo previamente configurado
- **Postcondición:** ningún registro de cultivo queda con valor "otros" sin especificar
- **Flujo principal:**
  1. El usuario, al registrar o editar una parcela (CU-01), abre el selector de cultivo/variedad.
  2. El sistema muestra únicamente las opciones del catálogo previamente configurado por el Administrador.
  3. El usuario selecciona el cultivo/variedad y el sistema lo asocia a la parcela.
- **Flujos alternativos / excepciones:**
  - Si el usuario intenta ingresar un cultivo fuera del catálogo (texto libre tipo "otros"), el sistema rechaza el valor (criterio de verificación de RF-02).
  - El Administrador puede ampliar el catálogo dando de alta un nuevo cultivo/variedad, lo que lo deja disponible de inmediato para el resto de usuarios.
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** intentar guardar un cultivo fuera del catálogo es rechazado por el sistema.
- **Evidencia textual:** *"no que esté plátano, cacao ahí... Simplemente que permite escribir... No debería estar así"* (EV-11). *"agrupadas por secciones, cacao, plátano, etcétera"* (EV-12).
- **Nota de relación:** este RF se amplía en RF-34, que exige que el catálogo soporte además un conjunto de atributos distinto por variedad, no solo por cultivo.

### RF-03. Registro de actividades agrícolas
- **Descripción:** el sistema debe permitir registrar una actividad (fumigación, fertilización, poda, limpieza, riego) indicando fecha, lote, producto/insumo usado y trabajador responsable.
- **Actor/origen:** Jornalero, Técnico. EV-03, EV-07, EV-08, EV-10, EV-14, EV-15, EV-16
- **Entradas:** fecha, lote, tipo de actividad, producto, trabajador
- **Salidas:** registro de actividad
- **Precondición:** lote existente
- **Postcondición:** actividad queda asociada al historial del lote
- **Flujo principal:**
  1. El Jornalero o Técnico selecciona el lote existente sobre el que va a registrar la actividad.
  2. Ingresa fecha, tipo de actividad (fumigación, fertilización, poda, riego, limpieza), producto/insumo usado y trabajador responsable.
  3. El sistema guarda el registro y lo asocia al historial del lote (CU-02).
- **Flujos alternativos / excepciones:**
  - Si falta la fecha, el lote o el trabajador responsable, el sistema rechaza el guardado (criterio de verificación de RF-03).
  - Si la actividad usa un insumo del catálogo, el sistema descuenta automáticamente el inventario correspondiente (ver RF-07, CU-05).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** el sistema no permite guardar una actividad sin fecha, lote y trabajador.
- **Evidencia textual:** *"que se registre lo que es la fecha, la parcela, la actividad, producto y el trabajador"* (EV-10). *"La información dispensable sería la actividad, la parcela, la fecha y también el responsable"* (EV-16).

### RF-04. Registro de cosecha por unidad específica del cultivo
- **Descripción:** el sistema debe registrar la cosecha usando la unidad propia de cada cultivo (racimo/caja para plátano, tacho/quintal para cacao), con conversión configurable a kg/lb.
- **Actor/origen:** Jornalero. EV-02, EV-08, EV-11, EV-12, EV-13, EV-14, EV-15
- **Entradas:** lote, fecha, cultivo, cantidad, unidad
- **Salidas:** registro de cosecha
- **Precondición:** lote y cultivo existentes
- **Postcondición:** cosecha sumada al acumulado del lote/periodo
- **Flujo principal:**
  1. El Jornalero selecciona el lote y el cultivo sobre el que va a registrar la cosecha.
  2. El sistema determina la unidad esperada según el cultivo (tacho/quintal para cacao, racimo/caja para plátano).
  3. El usuario ingresa la cantidad cosechada en esa unidad.
  4. El sistema valida la unidad, guarda la cosecha y actualiza el acumulado del lote/periodo.
- **Flujos alternativos / excepciones:**
  - Si la unidad ingresada no corresponde al cultivo del lote, el sistema rechaza el registro (criterio de verificación de RF-04).
  - Si corresponde, el usuario puede consultar de inmediato el precio de mercado vigente y ver el ingreso proyectado (RF-15).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** al registrar cosecha de cacao el sistema exige unidad "tacho" o "quintal". De plátano, "racimo" o "caja".
- **Evidencia textual:** *"cuando es la cosecha de plátano, es por racimo. Y cuando es el cacao, por tacho"* (EV-02). *"Me gustaría el total de la producción y también lo que es del peso"* (EV-08).

### RF-05. Cálculo automático de rendimiento por lote y periodo
- **Descripción:** el sistema debe calcular automáticamente el promedio de producción por lote y periodo (semanal/mensual) y permitir comparar entre periodos.
- **Actor/origen:** Administrador, Jornalero, Técnica. EV-01, EV-07, EV-11, EV-15, EV-16
- **Entradas:** histórico de cosechas del lote
- **Salidas:** promedio, comparación entre periodos
- **Precondición:** existen 2 o más registros de cosecha del lote
- **Postcondición:** valor mostrado en el reporte del lote
- **Flujo principal:**
  1. El sistema consulta el histórico de cosechas del lote seleccionado.
  2. Calcula el promedio de producción del periodo (suma dividida entre N registros).
  3. Muestra el promedio y permite comparar contra otros periodos en el reporte del lote.
- **Flujos alternativos / excepciones:**
  - Si el lote tiene menos de 2 registros de cosecha, el sistema muestra "datos insuficientes" en vez de un promedio (precondición de RF-05).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** el promedio calculado coincide con el cálculo manual (suma dividida entre N) sobre un set de prueba.
- **Evidencia textual:** *"sacar un promedio de cuánto rinde cada lote"* (EV-15). *"Me gustaría que generara automáticamente lo que es el rendimiento y también los totales"* (EV-16). *"El total de la cosecha y la producción por parcela"* (EV-07).

### RF-06. Cálculo automático de ganancia neta
- **Descripción:** el sistema debe calcular ingresos menos egresos (insumos, mano de obra) y mostrar la ganancia neta por periodo.
- **Actor/origen:** Técnico, Jornalero. EV-10, EV-11
- **Entradas:** registros de ingresos y egresos
- **Salidas:** ganancia neta del periodo
- **Precondición:** existen registros de ingreso y egreso en el periodo
- **Postcondición:** valor visible en el módulo financiero
- **Flujo principal:**
  1. El sistema consulta los registros de ingreso (automáticos por cosecha/precio y manuales por RF-26) y egreso (insumos, mano de obra) del periodo.
  2. Calcula la ganancia neta como la suma de ingresos menos la suma de egresos.
  3. Muestra el valor en el módulo financiero.
- **Flujos alternativos / excepciones:**
  - Si no existen registros de ingreso o egreso en el periodo consultado, el sistema muestra el módulo financiero en cero, sin error.
  - El usuario puede registrar manualmente un ingreso o egreso adicional (RF-26), que se refleja de inmediato en el siguiente cálculo.
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** ganancia es igual a la suma de ingresos menos la suma de egresos, verificado contra un caso de prueba manual.
- **Evidencia textual:** *"de todo lo que se gastó se ingresa también todo lo que se vendió y menorando todo eso, lo que quedó de ganancia"* (EV-10).
- **Nota de relación:** ver también RF-26, que pide un módulo de registro manual de ingresos/egresos independiente de este cálculo automático.

### RF-07. Gestión de inventario de insumos
- **Descripción:** el sistema debe permitir dar de alta insumos, registrar cantidad disponible/usada y visualizar stock restante.
- **Actor/origen:** Administrador, Técnico, Jornalero. EV-01, EV-03, EV-05, EV-06, EV-09, EV-10, EV-11, EV-12, EV-16
- **Entradas:** nombre del insumo, cantidad, unidad
- **Salidas:** stock disponible actualizado
- **Precondición:** ninguna
- **Postcondición:** stock reducido tras cada uso registrado
- **Flujo principal:**
  1. El usuario da de alta un insumo con nombre, cantidad disponible y unidad, o registra el uso de una cantidad de un insumo existente.
  2. El sistema actualiza el stock disponible restando la cantidad usada.
  3. El sistema muestra el stock actualizado.
- **Flujos alternativos / excepciones:**
  - Si el uso registrado dejaría el stock en un valor negativo, el sistema advierte antes de permitir guardar (regla de negocio de CU-05).
  - Tras actualizar el stock, el sistema verifica si quedó por debajo del umbral configurado y dispara la alerta de bajo stock (RF-08, RF-30).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** tras registrar el uso de 26 unidades de un stock de 30, el sistema muestra 4 disponibles.
- **Evidencia textual:** *"dice 4 de 30, es decir, lo que tenía era 30 y ahora le queda 4"* (EV-10). *"Sobre cada insumo, lo que es la cantidad, el nombre y además del stock limit"* (EV-16).

### RF-08. Alertas automáticas de bajo stock
- **Descripción:** el sistema debe enviar una alerta (notificación/SMS/correo) cuando el stock de un insumo baje de un umbral configurable, anticipándose al calendario de fertilización/fumigación.
- **Actor/origen:** Administrador, Jornalero, Técnica. EV-01, EV-03, EV-08, EV-09, EV-10, EV-11, EV-16
- **Entradas:** umbral configurado, stock actual
- **Salidas:** notificación al responsable
- **Precondición:** umbral definido para el insumo
- **Postcondición:** notificación enviada y registrada
- **Flujo principal:**
  1. Tras cada actualización de stock de un insumo (RF-07), el sistema compara el nuevo stock contra el umbral mínimo configurado (RF-30).
  2. Si el stock quedó por debajo del umbral, el sistema genera una notificación al responsable del insumo.
  3. El sistema registra el envío de la notificación.
- **Flujos alternativos / excepciones:**
  - Si el insumo no tiene un umbral configurado todavía, el sistema no dispara la alerta hasta que el Técnico lo defina (RF-30).
  - Si la notificación no puede entregarse por falta de conectividad, el sistema reintenta hasta la reconexión del dispositivo (ver RNF-15).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** al bajar del umbral, la notificación se envía en menos de 5 minutos.
- **Evidencia textual:** *"en siete días está estimado que debes abonar el cacao... Y se necesita comprar"* (EV-11). *"Me gustaría que me avisara por medio de una notificación en el celular"* (EV-08).
- **Nota de relación:** ver RF-30 para el umbral configurable como campo propio del insumo (stock limit).

### RF-09. Alerta de plagas/enfermedades asistida por IA con verificación humana obligatoria
- **Descripción:** el sistema debe generar una alerta de posible plaga/enfermedad por lote (basada en datos ingresados), marcada explícitamente como sugerencia a confirmar en campo, nunca como diagnóstico definitivo automático.
- **Actor/origen:** Administrador, Técnico, Jornalero. EV-01, EV-06, EV-07, EV-08, EV-09, EV-10, EV-15, EV-16, EV-17
- **Entradas:** datos del lote, histórico de tratamientos
- **Salidas:** alerta con opción "confirmar"/"descartar"
- **Precondición:** modelo de IA entrenado disponible
- **Postcondición:** alerta queda registrada con el resultado de la verificación humana
- **Flujo principal:**
  1. El sistema de IA analiza los datos del lote (histórico de tratamientos y, opcionalmente, una foto) y genera una sugerencia de posible plaga/enfermedad con su justificación.
  2. El sistema notifica al usuario responsable, marcando explícitamente la sugerencia como "a confirmar en campo", nunca como diagnóstico automático.
  3. El usuario revisa la justificación y elige "confirmar" o "descartar".
  4. El sistema registra la decisión del usuario junto con la alerta.
- **Flujos alternativos / excepciones:**
  - El usuario descarta la sugerencia; el sistema la deja registrada como descartada, sin aplicar ninguna acción sobre el lote.
  - El usuario, en desacuerdo con la recomendación, la registra formalmente en la bandeja de sugerencias en vez de solo confirmar/descartar (RF-33).
  - En ningún caso la alerta se aplica automáticamente al lote sin la confirmación explícita del usuario responsable (regla de negocio central de RF-09).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** ninguna alerta se aplica automáticamente a un lote sin que el usuario responsable la confirme.
- **Evidencia textual:** *"yo confirmaría yendo a visualizar el terreno"* (EV-10). *"Se debería poder revisar antes de tomar una decisión o aplicación"* (EV-07, EV-08). *"Primeramente que eso venga de una fuente confiable o de ya experiencias realizadas"* (EV-17).

### RF-10. Diagnóstico de plagas por imagen (IA)
- **Descripción:** el sistema debe permitir subir una foto de una hoja/fruto y recibir una sugerencia de plaga/enfermedad probable y tratamiento recomendado.
- **Actor/origen:** Jornalero. EV-15
- **Entradas:** foto (JPG/PNG)
- **Salidas:** plaga probable más recomendación
- **Precondición:** conexión a internet
- **Postcondición:** resultado registrado en el historial del lote
- **Flujo principal:**
  1. El Jornalero sube una foto (JPG/PNG) de una hoja o fruto desde el módulo de alerta de plagas (CU-06).
  2. El sistema procesa la imagen y genera una sugerencia de plaga/enfermedad probable junto con el tratamiento recomendado.
  3. El sistema responde en menos de 10 segundos y registra el resultado en el historial del lote.
- **Flujos alternativos / excepciones:**
  - Si no hay conexión a internet, el sistema informa que el diagnóstico por imagen no está disponible en ese momento (precondición de RF-10).
  - El resultado del diagnóstico por imagen sigue el mismo flujo de confirmación humana obligatoria que RF-09: se muestra como sugerencia, nunca como diagnóstico definitivo.
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** el sistema responde con una sugerencia en menos de 10 segundos tras subir la foto.
- **Evidencia textual:** *"una foto de una hoja o de un fruto enfermo que el sistema le atiene rápido y qué plaga es, qué remedio exacto"* (EV-15).

### RF-11. Asignación y seguimiento de tareas
- **Descripción:** el sistema debe permitir asignar una tarea a un trabajador por lote y fecha, con estados (pendiente, en proceso, bloqueado, completado) y filtro por estado.
- **Actor/origen:** Administrador, Técnico, Jornalero. EV-01, EV-09, EV-10, EV-12, EV-16
- **Entradas:** lote, trabajador, fecha, tipo de tarea
- **Salidas:** tarea visible con su estado
- **Precondición:** trabajador registrado
- **Postcondición:** tarea filtrable por los 4 estados
- **Flujo principal:**
  1. El usuario asigna una tarea a un trabajador, indicando lote, fecha y tipo de tarea.
  2. El sistema crea la tarea en estado "pendiente" y la muestra con su estado.
  3. El trabajador actualiza el estado de la tarea (pendiente → en proceso → bloqueado → completado) conforme avanza.
  4. El sistema permite filtrar la lista de tareas por cualquiera de los 4 estados.
- **Flujos alternativos / excepciones:**
  - Si el lote tiene un riesgo laboral registrado (CU-11), el sistema muestra la advertencia de equipo de protección antes de confirmar la asignación.
  - Al filtrar por un estado, el sistema muestra exclusivamente las tareas en ese estado, sin mezclar lotes ni trabajadores (criterio de verificación de RF-11).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** al filtrar por "pendiente" el sistema solo muestra tareas en ese estado.
- **Evidencia textual:** *"que tengas esa opción de buscar en esas cuatro secciones"* (EV-12).

### RF-12. Notificación móvil de tareas asignadas
- **Descripción:** el sistema debe notificar al trabajador (push/SMS) el lote, fecha y tarea asignada.
- **Actor/origen:** Técnico, Jornalera. EV-07, EV-08, EV-10
- **Entradas:** asignación de tarea
- **Salidas:** notificación push/SMS
- **Precondición:** trabajador con dispositivo registrado
- **Postcondición:** notificación entregada
- **Flujo principal:**
  1. Al asignarse una tarea (RF-11), el sistema identifica el dispositivo registrado del trabajador.
  2. El sistema envía una notificación push/SMS con el lote, la fecha y el tipo de tarea.
  3. El trabajador recibe la notificación en su dispositivo.
- **Flujos alternativos / excepciones:**
  - Si el trabajador no tiene un dispositivo registrado, el sistema deja la tarea visible en su vista de pendientes (RF-27) aunque no pueda enviar la notificación push.
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** la notificación incluye lote, fecha y tipo de tarea en el mensaje.
- **Evidencia textual:** *"que la notificación... Le avise por lote, en tal lote, fecha tal, hay un control"* (EV-10). *"A través de una notificación en el celular"* (EV-07, EV-08).

### RF-13. Registro de motivo de rechazo/pérdida de fruta
- **Descripción:** el sistema debe permitir registrar, por lote y fecha, la cantidad de fruta rechazada y su motivo (enfermedad, plaga, daño mecánico).
- **Actor/origen:** Jornalero. EV-14
- **Entradas:** lote, fecha, cantidad rechazada, motivo
- **Salidas:** registro de rechazo
- **Precondición:** cosecha registrada ese día
- **Postcondición:** rechazo restado del total aprovechable
- **Flujo principal:**
  1. El Jornalero, tras registrar la cosecha del día (RF-04), registra la cantidad de fruta rechazada y su motivo (enfermedad, plaga, daño mecánico).
  2. El sistema resta automáticamente la cantidad rechazada del total aprovechable del lote.
- **Flujos alternativos / excepciones:**
  - Si no hay una cosecha registrada ese día, el sistema no permite registrar un rechazo asociado (precondición de RF-13).
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** el total de fruta aprovechable excluye automáticamente lo marcado como rechazado.
- **Evidencia textual:** *"cuántos salieron rechazados, ya sea por una enfermedad, una plaga o los daños"* (EV-14).

### RF-14. Trazabilidad de lote de exportación
- **Descripción:** el sistema debe permitir registrar, por lote de exportación, el estado de calidad (primera/segunda), variedad sembrada y ciclo de enfunde (fecha/color de cinta) para trazar el producto desde campo hasta empaque.
- **Actor/origen:** Jornalero. EV-13, EV-14
- **Entradas:** color de cinta, semana de enfunde, calidad de caja
- **Salidas:** ficha de trazabilidad del lote de exportación
- **Precondición:** lote marcado como "exportación"
- **Postcondición:** historial completo desde enfunde hasta empaque consultable
- **Flujo principal:**
  1. Para un lote marcado como "exportación" (RF-01), el usuario registra color de cinta, semana de enfunde y calidad de caja al momento de la cosecha (RF-04).
  2. El sistema guarda la ficha de trazabilidad asociada al lote de exportación.
  3. Dado un número de caja, el sistema recupera el lote, la fecha de enfunde y el color de cinta correspondiente (criterio de verificación de RF-14).
- **Flujos alternativos / excepciones:**
  - Si el lote no está marcado como "exportación", el sistema no solicita estos campos adicionales.
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** dado un número de caja, el sistema recupera el lote, la fecha de enfunde y el color de cinta correspondiente.
- **Evidencia textual:** *"con el dato que el enfundador da, con eso se lo maneja para el día de cosecha... Ya se sabe cuántas cajas van a salir"* (EV-13). *"que en las pantallas de la cosecha se debe ver clarito el color de la cinta"* (EV-14).

### RF-15. Consulta de precio de mercado y estimación de ingreso
- **Descripción:** el sistema debe permitir consultar el precio de mercado vigente del cacao/plátano y estimar el ingreso proyectado de una cosecha.
- **Actor/origen:** Jornalero. EV-11
- **Entradas:** cantidad cosechada, precio de mercado (manual o de fuente externa)
- **Salidas:** ingreso estimado
- **Precondición:** cantidad de cosecha registrada
- **Postcondición:** estimación mostrada al usuario
- **Flujo principal:**
  1. Tras registrar una cosecha (RF-04), el usuario consulta el precio de mercado vigente del cultivo.
  2. El sistema calcula el ingreso estimado como la cantidad cosechada multiplicada por el precio ingresado.
  3. El sistema muestra la estimación al usuario.
- **Flujos alternativos / excepciones:**
  - Si no hay un precio de mercado disponible de fuente externa, el usuario puede ingresarlo manualmente para obtener la estimación.
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** ingreso estimado es igual a cantidad multiplicada por precio ingresado, validado con un caso de prueba.
- **Evidencia textual:** *"que consultara el precio de la materia prima... Un cálculo de cuánto más o menos uno va a ganar"* (EV-11).

### RF-16. Registro de condición climática/estado del lote
- **Descripción:** el sistema debe permitir anotar, junto a cada visita/actividad del lote, el estado climático (lluvia/sol) y del terreno (accesibilidad).
- **Actor/origen:** Jornalero. EV-12, EV-15
- **Entradas:** condición climática, observación de acceso
- **Salidas:** campo adicional en el registro de actividad/parcela
- **Precondición:** ninguna
- **Postcondición:** dato consultable en el historial del lote
- **Flujo principal:**
  1. Al registrar una actividad o visitar un lote (CU-01), el usuario anota la condición climática (lluvia/sol) y una observación de accesibilidad del terreno.
  2. El sistema guarda el dato como campo adicional del registro de actividad/parcela.
- **Flujos alternativos / excepciones:**
  - El usuario puede registrar la condición climática en cualquier momento posterior, no solo al crear el registro (flujo alternativo documentado en CU-01).
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** el campo de clima aparece disponible en el formulario de registro de parcela/actividad.
- **Evidencia textual:** *"Puede faltar un espacio para anotar lo que es el estado del clima"* (EV-15).

### RF-17. Canal de reporte rápido tipo chat/voz
- **Descripción:** el sistema debe ofrecer un botón de reporte rápido (texto corto o nota de voz) para que un jornalero reporte una novedad sin llenar formularios extensos.
- **Actor/origen:** Jornalero. EV-15
- **Entradas:** nota de voz o texto corto
- **Salidas:** reporte enviado al responsable del lote
- **Precondición:** usuario autenticado
- **Postcondición:** reporte visible para el administrador/técnico
- **Flujo principal:**
  1. El Jornalero abre el canal de reporte rápido desde la pantalla principal.
  2. Registra un mensaje corto (texto o nota de voz) describiendo una novedad de campo.
  3. El sistema envía el reporte al responsable del lote en un máximo de 2 toques desde la pantalla principal (criterio de verificación de RF-17).
- **Flujos alternativos / excepciones:**
  - Si el reporte describe una posible plaga cuarentenaria, el sistema sugiere escalarlo como aviso fitosanitario formal (RF-37, CU-14).
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** el reporte se envía en máximo 2 toques desde la pantalla principal.
- **Evidencia textual:** *"un chat o un botón rápido de voz para reportar novedades"* (EV-15).

### RF-18. Registro de riesgo/seguridad laboral por lote
- **Descripción:** el sistema debe permitir marcar un lote con una alerta de riesgo (fauna peligrosa, terreno inestable) visible antes de asignar tareas ahí, y sugerir el equipo de protección personal requerido.
- **Actor/origen:** Jornalero, Técnico. EV-11, EV-17
- **Entradas:** tipo de riesgo, lote, equipo de protección recomendado
- **Salidas:** alerta visible al asignar tarea en ese lote
- **Precondición:** ninguna
- **Postcondición:** advertencia mostrada al asignar personal
- **Flujo principal:**
  1. El Técnico marca un lote con un riesgo laboral (fauna peligrosa, terreno inestable), indicando el equipo de protección personal sugerido.
  2. Al asignar una tarea en ese lote (RF-11), el sistema muestra la advertencia de riesgo antes de confirmar la asignación.
- **Flujos alternativos / excepciones:**
  - Ninguna tarea sobre un lote con riesgo registrado puede confirmarse sin que la advertencia de equipo de protección se haya mostrado primero (regla de negocio de CU-11).
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** al asignar una tarea en un lote marcado con riesgo, el sistema muestra la advertencia antes de confirmar.
- **Evidencia textual:** *"hay riesgo de que haya animales... Como serpientes"* (EV-11). *"se dice qué usar, qué trajes usar, incluso botas, hasta más arriba... Ya que al momento de presenciar estos peligros estén bien cuidados"* (EV-17).

### RF-19. Reportes de producción, costos y pérdidas con gráficos
- **Descripción:** el sistema debe generar reportes de producción, costos, pérdidas por plaga y rendimiento por parcela/periodo, con gráficos de barra y circulares codificados por color.
- **Actor/origen:** Administrador, Técnico. EV-01, EV-05, EV-06, EV-07, EV-10, EV-16
- **Entradas:** rango de fechas, lote o lotes
- **Salidas:** reporte visual exportable
- **Precondición:** existen datos en el rango seleccionado
- **Postcondición:** reporte generado y descargable
- **Flujo principal:**
  1. El Administrador o Técnico selecciona un rango de fechas y uno o más lotes.
  2. El sistema consolida producción, costos, pérdidas por plaga y rendimiento del rango seleccionado.
  3. El sistema genera gráficos de barra y circulares codificados por color, reflejando exactamente la suma de los registros del rango.
- **Flujos alternativos / excepciones:**
  - Si no existen datos en el rango seleccionado, el sistema muestra "no hay datos disponibles" en vez de un reporte vacío (criterio de verificación de RF-19).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** el reporte generado refleja exactamente la suma de los registros del rango de fechas seleccionado.
- **Evidencia textual:** *"reporte por parcela, costos, pérdidas por plagas o rendimiento por periodo"* (EV-01). *"Los reportes más importantes, el inventario. Otro también podría ser lo que es la producción y las cosechas"* (EV-16).

### RF-20. Gestión de usuarios y control de acceso
- **Descripción:** el sistema debe requerir usuario/contraseña para ingresar, con roles diferenciados (administrador, técnico, jornalero).
- **Actor/origen:** Técnico. EV-07, EV-08, EV-10
- **Entradas:** usuario, contraseña
- **Salidas:** sesión autenticada con permisos según rol
- **Precondición:** usuario previamente registrado
- **Postcondición:** acceso concedido solo a las funciones de su rol
- **Flujo principal:**
  1. El usuario ingresa su usuario y contraseña.
  2. El sistema valida las credenciales y determina el rol (Administrador, Técnico, Jornalero).
  3. El sistema concede acceso únicamente a las funciones correspondientes a ese rol.
- **Flujos alternativos / excepciones:**
  - Si las credenciales son inválidas, el sistema niega el acceso.
  - Si un usuario con rol "jornalero" intenta acceder al módulo financiero, el sistema le niega el acceso (criterio de verificación de RF-20).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** un usuario con rol "jornalero" no puede acceder al módulo financiero.
- **Evidencia textual:** *"han creado como un tipo formulario, donde le pide lo que es un usuario y una contraseña"* (EV-10). *"El administrador debería tener el control total y los trabajadores sólo lo necesario"* (EV-07, EV-08).

### RF-21. Registro de visitas técnicas periódicas
- **Descripción:** el sistema debe permitir registrar cada visita técnica (fecha, hallazgos, informe adjunto) con recordatorio de la siguiente visita (ciclo de 15 días).
- **Actor/origen:** Técnico. EV-10
- **Entradas:** fecha de visita, informe, próxima fecha estimada
- **Salidas:** historial de visitas técnicas por lote/finca
- **Precondición:** ninguna
- **Postcondición:** recordatorio generado para la siguiente visita
- **Flujo principal:**
  1. El Técnico registra una visita técnica: fecha, hallazgos e informe adjunto.
  2. El sistema guarda la visita y la asocia al historial de cumplimiento del lote.
  3. 15 días después, el sistema genera automáticamente un recordatorio de la siguiente visita (criterio de verificación de RF-21).
- **Flujos alternativos / excepciones:**
  - Si la visita encuentra un incumplimiento, el sistema sugiere registrar la capacitación o el equipo de protección relacionado (CU-11, CU-13).
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** 15 días después de una visita registrada, el sistema genera un recordatorio automático.
- **Evidencia textual:** *"un control de la visita técnica de 15 días y pone el otro control que fue a realizarla después de 15 días"* (EV-10).

### RF-26. Registro manual de ingresos y egresos
- **Descripción:** el sistema debe ofrecer un módulo dedicado para registrar manualmente cada ingreso y egreso (concepto, monto, fecha), independiente del cálculo automático de ganancia neta (RF-06).
- **Actor/origen:** Técnico, Jornalera. EV-07, EV-08
- **Entradas:** concepto, monto, fecha, tipo (ingreso/egreso)
- **Salidas:** listado de movimientos
- **Precondición:** usuario autenticado
- **Postcondición:** movimiento reflejado en el cálculo de ganancia neta
- **Flujo principal:**
  1. El usuario autenticado abre el módulo de registro manual de ingresos/egresos.
  2. Registra concepto, monto, fecha y tipo (ingreso/egreso), de forma independiente al cálculo automático de RF-06.
  3. El sistema guarda el movimiento en el listado.
- **Flujos alternativos / excepciones:**
  - El movimiento registrado manualmente se refleja de inmediato en el reporte financiero del periodo correspondiente (criterio de verificación de RF-26).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** un ingreso o egreso registrado manualmente aparece reflejado en el reporte financiero del periodo correspondiente.
- **Evidencia textual:** *"Que permitiera controlar los ingresos y egresos"* (EV-07). *"Me gustaría que tuviera un registro de gastos y de ganancias también"* (EV-08).

### RF-27. Vista de tareas pendientes por trabajador
- **Descripción:** el sistema debe mostrar a cada trabajador una vista dedicada de sus propias tareas pendientes.
- **Actor/origen:** Jornalero. EV-09
- **Entradas:** usuario autenticado
- **Salidas:** listado de tareas pendientes propias
- **Precondición:** existen tareas asignadas al usuario
- **Postcondición:** ninguna
- **Flujo principal:**
  1. El trabajador autenticado abre su vista de tareas pendientes.
  2. El sistema muestra únicamente las tareas asignadas a ese trabajador.
- **Flujos alternativos / excepciones:**
  - Un trabajador con 3 tareas pendientes ve exactamente esas 3 al abrir la vista, sin tareas de otros lotes o trabajadores (criterio de verificación de RF-27).
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** un trabajador con 3 tareas pendientes ve exactamente esas 3 al abrir la vista, sin tareas de otros lotes o trabajadores.
- **Evidencia textual:** *"¿Existe alguna función que considere indispensable y que todavía no hayamos completado? Ver las tareas pendientes"* (EV-09).

### RF-28. Campo de observaciones en el registro de tareas
- **Descripción:** el sistema debe permitir adjuntar una nota u observación libre a cada tarea registrada como completada.
- **Actor/origen:** Jornalero. EV-09
- **Entradas:** texto libre
- **Salidas:** observación asociada a la tarea
- **Precondición:** tarea existente
- **Postcondición:** observación visible al consultar el historial de la tarea
- **Flujo principal:**
  1. El trabajador, al marcar una tarea como completada (RF-11), adjunta una nota u observación de texto libre.
  2. El sistema asocia la observación a la tarea.
- **Flujos alternativos / excepciones:**
  - La observación ingresada permanece visible al consultar el detalle de la tarea en cualquier momento posterior (criterio de verificación de RF-28).
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** la observación ingresada aparece al consultar el detalle de la tarea.
- **Evidencia textual:** *"Al observar esta propuesta, ¿hay alguna información que considere que falta? Sí, las observaciones de las tareas"* (EV-09).

### RF-29. Historial completo por parcela
- **Descripción:** el sistema debe ofrecer una vista de historial por parcela que agregue actividades, tratamientos y cosechas a lo largo del tiempo, no solo el estado actual.
- **Actor/origen:** Técnica. EV-16
- **Entradas:** identificador de parcela
- **Salidas:** línea de tiempo de eventos de la parcela
- **Precondición:** la parcela tiene al menos un evento registrado
- **Postcondición:** ninguna
- **Flujo principal:**
  1. El usuario selecciona una parcela y abre su vista de historial.
  2. El sistema agrega actividades, tratamientos y cosechas de esa parcela a lo largo del tiempo.
  3. El sistema muestra los eventos ordenados cronológicamente.
- **Flujos alternativos / excepciones:**
  - Si la parcela no tiene ningún evento registrado, el sistema muestra el historial vacío en vez de un error (precondición de RF-29).
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** al consultar el historial de una parcela con 5 eventos registrados en distintas fechas, los 5 aparecen ordenados cronológicamente.
- **Evidencia textual:** *"¿Existe alguna función que considere indispensable y que todavía no hayamos completado? El historial de cada parcela"* (EV-16).

### RF-30. Umbral de stock mínimo configurable por insumo
- **Descripción:** el sistema debe permitir definir, para cada insumo, un valor numérico de stock mínimo (stock limit) que dispare la alerta de bajo stock (RF-08).
- **Actor/origen:** Técnica. EV-16
- **Entradas:** cantidad mínima por insumo
- **Salidas:** umbral guardado en la ficha del insumo
- **Precondición:** insumo ya registrado
- **Postcondición:** el umbral queda disponible para el mecanismo de alertas
- **Flujo principal:**
  1. El Técnico abre la ficha de un insumo ya registrado.
  2. Define el valor numérico de stock mínimo (stock limit) para ese insumo.
  3. El sistema guarda el umbral y lo deja disponible para el mecanismo de alertas (RF-08).
- **Flujos alternativos / excepciones:**
  - El Técnico puede editar el umbral en cualquier momento; el nuevo valor se aplica desde la siguiente actualización de stock.
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** al bajar el stock del insumo por debajo del valor configurado, se dispara la alerta de RF-08.
- **Evidencia textual:** *"Sobre cada insumo, lo que es la cantidad, el nombre y además del stock limit"* (EV-16).

### RF-31. Detección de valores atípicos al ingresar datos
- **Descripción:** el sistema debe comparar cada dato numérico recién ingresado (por ejemplo, cantidad cosechada) contra el promedio histórico del mismo lote y avisar si el valor se aleja de forma significativa, antes de guardarlo.
- **Actor/origen:** Técnico. EV-17
- **Entradas:** valor ingresado, histórico del lote
- **Salidas:** advertencia de valor atípico
- **Precondición:** existe histórico suficiente del lote (mínimo 3 registros previos)
- **Postcondición:** el usuario confirma o corrige el dato antes de guardar
- **Flujo principal:**
  1. El usuario ingresa un dato numérico (por ejemplo, cantidad cosechada) para un lote con histórico suficiente (mínimo 3 registros previos).
  2. El sistema compara el valor contra el promedio histórico del mismo lote.
  3. Si el valor se desvía más de 2 desviaciones estándar del promedio, el sistema muestra una advertencia antes de guardar.
- **Flujos alternativos / excepciones:**
  - El usuario confirma el dato pese a la advertencia (si el valor atípico es real), o lo corrige antes de guardar (postcondición de RF-31).
  - Si el lote no tiene histórico suficiente, el sistema guarda el dato sin comparar (precondición de RF-31).
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** un valor que se desvía más de 2 desviaciones estándar del promedio histórico dispara la advertencia antes de guardar.
- **Evidencia textual:** *"que me generara automáticamente promedios estadísticos realizados mediante gráficos, gráficos automáticos que al momento de meter un dato, una variable, me indique... Que este valor de aquí estuvo mal"* (EV-17).

### RF-32. Vía de integración futura con sensores de campo
- **Descripción:** el sistema debe exponer una interfaz (API) capaz de recibir automáticamente lecturas de sensores de clima, suelo o nutrientes, como alternativa al ingreso manual, para una fase posterior del proyecto.
- **Actor/origen:** Técnico. EV-17
- **Entradas:** lectura de sensor (formato a definir en fase posterior)
- **Salidas:** dato incorporado al historial del lote sin intervención manual
- **Precondición:** sensor compatible configurado
- **Postcondición:** ninguna
- **Prioridad MoSCoW:** Won't have (esta versión). Queda documentado para trabajo futuro
- **Criterio de verificación:** no aplica en esta versión, queda como extensión documentada.
- **Evidencia textual:** *"Que ya la aplicación que están generando tenga sensores... Que tomen esos datos automáticamente... Me generan esas alertas de que la planta tiene falta de nutrientes, de nitrógeno, potasio o de fósforo"* (EV-17).

### RF-33. Bandeja de sugerencias para disputar una recomendación de IA
- **Descripción:** el sistema debe ofrecer un mecanismo para que el usuario registre formalmente su desacuerdo con una recomendación de IA, distinto del simple "confirmar/descartar" de RF-09, quedando disponible como registro de retroalimentación.
- **Actor/origen:** Técnico. EV-17
- **Entradas:** recomendación en cuestión, comentario del usuario
- **Salidas:** registro de desacuerdo asociado a la recomendación
- **Precondición:** existe una recomendación de IA previa
- **Postcondición:** el desacuerdo queda visible para revisión posterior del equipo técnico
- **Flujo principal:**
  1. El usuario, en desacuerdo con una recomendación de IA previa (RF-09/RF-10), abre la bandeja de sugerencias.
  2. Registra su comentario asociado a esa recomendación.
  3. El sistema guarda el desacuerdo, visible para revisión posterior del equipo técnico.
- **Flujos alternativos / excepciones:**
  - El desacuerdo registrado aparece en un listado consultable con fecha y comentario del usuario (criterio de verificación de RF-33), sin alterar el estado de la alerta original.
- **Prioridad MoSCoW:** Should have
- **Criterio de verificación:** un desacuerdo registrado aparece en un listado consultable, con la fecha y el comentario del usuario.
- **Evidencia textual:** *"Si en la aplicación realizada de ustedes, yo verifico que esa información está mal, yo obviamente que daría mi observación en una bandejita de sugerencias"* (EV-17).

### RF-34. Esquema de atributos configurable por variedad de cultivo
- **Descripción:** el catálogo de cultivos (RF-02) debe permitir definir campos y variables distintas por variedad, no solo por tipo de cultivo, dado que plátano y las distintas variedades de cacao (nacional, CN51, montaña, entre otras) manejan datos de manejo agronómico diferentes.
- **Actor/origen:** Técnico. EV-17
- **Entradas:** variedad seleccionada
- **Salidas:** formulario con los campos correspondientes a esa variedad
- **Precondición:** variedad dada de alta en el catálogo con su set de atributos
- **Postcondición:** ninguna
- **Flujo principal:**
  1. El Técnico da de alta una variedad de cultivo en el catálogo (RF-02), definiendo el conjunto de campos y atributos propios de esa variedad.
  2. Al seleccionar esa variedad en un formulario (por ejemplo, CU-01), el sistema muestra el conjunto de campos correspondiente.
- **Flujos alternativos / excepciones:**
  - Al seleccionar una variedad de cacao, el formulario muestra un conjunto de campos distinto al que se muestra al seleccionar plátano (criterio de verificación de RF-34).
- **Prioridad MoSCoW:** Must have
- **Criterio de verificación:** al seleccionar una variedad de cacao, el formulario muestra un conjunto de campos distinto al que se muestra al seleccionar plátano.
- **Evidencia textual:** *"Existen muchas diferencias, en el plátano se registra lo que es... En el cacao se registra desde su mazorca... Hay muchos tipos de cacao, el nacional, el CN51, el cacao de montaña, el cacao Iñak, el cacao Pincai"* (EV-17).

### RF-35. Registro de análisis de suelo previo a siembra
- **Descripción:** el sistema debe permitir registrar, por parcela, el resultado de un análisis de suelo (calicata) previo al establecimiento de un cultivo, indicando tipo de suelo y aptitud.
- **Actor/origen:** Técnico. EV-17
- **Entradas:** tipo de suelo, resultado de aptitud, fecha del análisis
- **Salidas:** ficha de análisis de suelo asociada a la parcela
- **Precondición:** parcela registrada
- **Postcondición:** dato consultable antes de aprobar la siembra
- **Flujo principal:**
  1. El Técnico registra, para una parcela ya existente, el resultado de un análisis de suelo (calicata) previo a la siembra: tipo de suelo, aptitud y fecha.
  2. El sistema guarda la ficha de análisis de suelo asociada a la parcela.
- **Flujos alternativos / excepciones:**
  - Una parcela con análisis de suelo registrado muestra el resultado de aptitud al consultar su ficha, antes de aprobar la siembra (criterio de verificación de RF-35).
- **Prioridad MoSCoW:** Could have
- **Criterio de verificación:** una parcela con análisis de suelo registrado muestra el resultado de aptitud al consultar su ficha.
- **Evidencia textual:** *"Se hace una verificación del terreno... Es decir una calicata, para ver o realizar un análisis de suelo... Donde ese análisis de suelo nos va a decir si es apto o no es apto sembrar en dicho terreno"* (EV-17).

### 3.2 Requisitos legales derivados

> Estos RF se derivan directamente de los 26 criterios (C1 a C26) de `Modelo_Legal_LOPDP.md`, en sus 3 bloques normativos (LOPDP, BPA cacao/trazabilidad, bioseguridad y manejo fitosanitario). Ninguna de las 17 entrevistas mencionó el proceso de certificación BPA, el derecho de acceso/rectificación de datos personales, el aviso fitosanitario formal, ni el registro de capacitaciones, así que siguen siendo vacíos legales puros. La parte de equipo de protección personal de RF-24 y el análisis de suelo sí encontraron respaldo parcial en EV-17 (ver RF-18 y RF-35), pero el certificado de salud del trabajador continúa sin evidencia de entrevista.

### RF-22. Registro de consentimiento del trabajador para el tratamiento de sus datos personales dentro del sistema
- **Actor/origen:** Administrador. Sin evidencia de entrevista (criterio C4, LOPDP Art. 8)
- **Flujo principal:**
  1. En el primer inicio de sesión de un trabajador (CU-09), el sistema muestra el aviso de tratamiento de datos personales (LOPDP Art. 8).
  2. El usuario acepta el consentimiento de forma libre, específica, informada e inequívoca.
  3. El sistema registra el consentimiento antes de continuar con cualquier otro módulo.
- **Flujos alternativos / excepciones:**
  - Si el usuario no acepta el aviso, el sistema no concede acceso a ningún módulo que trate datos personales (regla de negocio de CU-09).
- **Prioridad MoSCoW:** Must have (regulatorio)
- **Evidencia legal:** Art. 8 LOPDP. El consentimiento debe ser libre, específico, informado e inequívoco.

### RF-23. Módulo de derechos ARCO+ del trabajador
- **Descripción:** acceso, rectificación y eliminación de sus propios datos.
- **Actor/origen:** Jornalero/Trabajador. Sin evidencia de entrevista (criterio C10, LOPDP Art. 13-19)
- **Flujo principal:**
  1. El trabajador, autenticado en el sistema, solicita acceder, rectificar o eliminar sus propios datos personales desde Ajustes → Mis Datos.
  2. El sistema atiende la solicitud sobre los datos del propio usuario.
  3. El sistema deja un registro de la acción realizada (criterio de verificación derivado de C10, LOPDP Art. 13-19).
- **Flujos alternativos / excepciones:**
  - Si la solicitud es de eliminación y existen datos que deben conservarse por obligación legal (por ejemplo, trazabilidad BPA), el sistema informa al usuario cuáles datos no pueden eliminarse y por qué.
- **Prioridad MoSCoW:** Must have (regulatorio)

### RF-24. Registro de certificado de salud del trabajador que aplica agroquímicos
- **Actor/origen:** Administrador. Sin evidencia de entrevista para el certificado de salud (criterio C17, Resolución AGROCALIDAD 183, Art. 33-34). El requisito de equipo de protección personal ya cuenta con evidencia real y se documentó en RF-18.
- **Flujo principal:**
  1. Antes de asignar una tarea de aplicación de agroquímicos (CU-11), el Administrador registra el certificado de salud vigente del trabajador.
  2. El sistema adjunta el certificado al perfil del trabajador.
- **Flujos alternativos / excepciones:**
  - Si el trabajador no tiene certificado de salud vigente registrado, el sistema advierte que el certificado no está registrado al intentar asignarle esa tarea (Res. AGROCALIDAD 183, Art. 33-34).
- **Prioridad MoSCoW:** Must have (regulatorio)

### RF-25. Registro y seguimiento del proceso de certificación BPA ante AGROCALIDAD
- **Descripción:** solicitud, inspección, vigencia.
- **Actor/origen:** Administrador. Sin evidencia de entrevista (criterio C20, Resolución AGROCALIDAD 183, Art. 39-43)
- **Flujo principal:**
  1. El Administrador revisa el panel de cumplimiento (vigencia del certificado BPA, capacitaciones pendientes, bitácora de bioseguridad) (CU-13).
  2. Si el certificado está por vencer o falta evidencia de respaldo, solicita la renovación ante AGROCALIDAD.
  3. El sistema adjunta como evidencia los registros de capacitación y la bitácora de bioseguridad.
- **Flujos alternativos / excepciones:**
  - Si falta una capacitación obligatoria, el sistema bloquea la solicitud de renovación hasta que se registre (RF-36, RF-39).
- **Prioridad MoSCoW:** Should have (regulatorio)

### RF-36. Registro de capacitación en manejo de plaguicidas y primeros auxilios
- **Actor/origen:** Administrador. Sin evidencia de entrevista (criterio C23, Resolución AGROCALIDAD 183, Art. 18(e))
- **Flujo principal:**
  1. El Administrador registra una capacitación en manejo de plaguicidas o primeros auxilios recibida por un trabajador.
  2. El sistema guarda el registro como evidencia de respaldo para la certificación BPA (RF-25, CU-13).
- **Flujos alternativos / excepciones:**
  - Si la capacitación registrada está vencida o incompleta, el sistema la marca como pendiente en el panel de cumplimiento (CU-13).
- **Prioridad MoSCoW:** Should have (regulatorio)

### RF-37. Aviso/alerta ante síntomas sospechosos de plaga cuarentenaria (ej. Moko)
- **Actor/origen:** Jornalero, Técnico, Administrador. Sin evidencia de entrevista (criterio C24, Resolución AGROCALIDAD 0072, Art. 3.6.1(a))
- **Flujo principal:**
  1. Un usuario de campo detecta síntomas sospechosos de plaga cuarentenaria (ej. Moko) en un lote.
  2. Registra el síntoma y el lote afectado en el sistema.
  3. El sistema genera el aviso fitosanitario y lo marca con prioridad alta, visible de inmediato para el Administrador.
  4. Un Técnico confirma el síntoma tras la inspección.
- **Flujos alternativos / excepciones:**
  - El Técnico descarta el síntoma tras la inspección; el aviso no se envía a AGROCALIDAD, pero queda registrado como descartado para trazabilidad (CU-14).
- **Prioridad MoSCoW:** Must have (regulatorio). Nota: EV-17 mencionó el problema del Moko y las medidas de desinfección, pero ningún entrevistado describió el mecanismo formal de aviso a AGROCALIDAD, por eso sigue siendo un vacío.

### RF-38. Bitácora de bioseguridad de ingreso/salida del predio
- **Actor/origen:** Administrador. Sin evidencia de entrevista sobre el registro formal, aunque EV-17 sí describió la práctica de desinfección en sí misma (criterio C25, Resolución AGROCALIDAD 0072, Art. 3.6.1(d))
- **Flujo principal:**
  1. Al confirmarse una visita al predio (técnica o por síntoma sospechoso, CU-10/CU-14), el usuario registra el evento de ingreso/salida en la bitácora de bioseguridad.
  2. El sistema guarda el registro con fecha y motivo de la visita.
- **Flujos alternativos / excepciones:**
  - La bitácora queda disponible como evidencia de respaldo para la certificación BPA y para la auditoría de AGROCALIDAD (RF-25, CU-13).
- **Prioridad MoSCoW:** Should have (regulatorio)

### RF-39. Registro de capacitaciones del personal sobre control fitosanitario específico
- **Actor/origen:** Administrador. Sin evidencia de entrevista (criterio C26, Resolución AGROCALIDAD 0072, Art. 3.6.1(f)(g))
- **Flujo principal:**
  1. El Administrador registra una capacitación fitosanitaria específica recibida por un trabajador (control de plagas cuarentenarias, bioseguridad).
  2. El sistema guarda el registro y lo deja disponible como evidencia de auditoría (RF-25, CU-13).
- **Flujos alternativos / excepciones:**
  - Si falta una capacitación fitosanitaria obligatoria, el sistema bloquea la solicitud de renovación BPA hasta que se registre (regla de negocio de CU-13).
- **Prioridad MoSCoW:** Should have (regulatorio)

### 3.3 Requisitos no funcionales

### RNF-01. Acceso móvil prioritario (Interacción con el usuario)
- **Descripción:** las funciones de consulta y registro más usadas en campo (tareas, cosecha, inventario) deben estar disponibles desde un teléfono móvil, no solo desde escritorio.
- **Métrica:** el 100% de las pantallas de RF-01, RF-03, RF-04, RF-11 y RF-19 deben renderizar correctamente en una pantalla de 360x800 px sin scroll horizontal.
- **Evidencia textual:** *"Desde mi teléfono, más rápido"* (EV-01). *"A través de una notificación en el celular"* (EV-07, EV-08).

### RNF-02. Interfaz simple y sin tecnicismos (Interacción con el usuario)
- **Descripción:** las etiquetas de campos y menús deben usar vocabulario cotidiano del agricultor, evitando abreviaturas o nombres de columna técnicos.
- **Métrica:** en una prueba de usabilidad con 5 jornaleros sin experiencia previa en el sistema, al menos el 90% de los términos de la interfaz deben ser comprendidos sin ayuda externa.
- **Evidencia textual:** *"cosas muy técnicas, números de oficina, códigos raros a la vez, solo confundir. Entre más directo y sencillo es mejor"* (EV-15). *"Simplificaría lo que es la navegación"* (EV-16).

### RNF-03. Usabilidad para usuarios con baja alfabetización digital (Interacción con el usuario)
- **Descripción:** un usuario sin experiencia previa en aplicaciones móviles debe poder completar el registro de una cosecha sin asistencia después de una capacitación breve.
- **Métrica:** tiempo máximo de 5 minutos de capacitación para que un jornalero sin experiencia previa registre una cosecha sin errores.
- **Evidencia textual:** *"No tengo estudios"* / uso previo de apps: *"No"* (EV-02). *"En lo que es tecnología, sí, no"* (EV-13).

### RNF-04. Robustez de campo ante condiciones adversas (Fiabilidad)
- **Descripción:** el registro de actividades y cosecha debe seguir siendo posible sin conexión a internet, sincronizando los datos cuando la conexión se restablezca.
- **Métrica:** el sistema debe permitir guardar localmente hasta 7 días de registros sin conexión, sin pérdida de datos al reconectarse.
- **Evidencia textual:** *"el barro y la lluvia... Dañan las hojas de papel donde nosotros anotamos y nos confundimos"* (EV-14).

### RNF-05. Explicabilidad verificable de las recomendaciones de IA (Adecuación funcional)
- **Descripción:** toda recomendación de IA debe mostrar la razón de la sugerencia antes de que el usuario pueda aplicarla.
- **Métrica:** el 100% de las alertas de IA (RF-09, RF-10) deben incluir un texto de justificación de máximo 60 palabras, visible antes del botón de confirmación.
- **Evidencia textual:** *"yo confirmaría yendo a visualizar el terreno"* (EV-10). *"Que explique cuál es el problema y lo que se debe hacer"* (EV-09).

### RNF-06. Transparencia del origen de los datos de la recomendación (Adecuación funcional)
- **Descripción:** además de explicar el motivo, la recomendación debe indicar en qué datos del propio lote se basó.
- **Métrica:** el 100% de las recomendaciones deben listar al menos 1 dato de origen (por ejemplo, "basado en el registro de fumigación del 12 de agosto").
- **Evidencia textual:** *"Los datos en que se basa esta información"* (EV-16). *"Primeramente que eso venga de una fuente confiable"* (EV-17).

### RNF-07. Preservación del histórico de datos sin pérdida (Fiabilidad)
- **Descripción:** ningún dato de cosecha, actividad o inventario registrado debe poder eliminarse de forma permanente sin confirmación explícita y registro de auditoría.
- **Métrica:** el sistema debe mantener un registro de auditoría de cambios/eliminaciones por al menos 24 meses.
- **Evidencia textual:** *"había desvarianza de datos, en lo que no se podía cuadrar un número de cajas"* (EV-01).

### RNF-08. Consentimiento explícito registrado en el primer inicio de sesión (Seguridad)
- **Descripción:** todo trabajador debe aceptar un aviso de tratamiento de datos personales antes de poder usar el sistema por primera vez.
- **Métrica:** el 100% de las cuentas activas deben tener un registro de aceptación con fecha y hora.
- **Evidencia textual:** *"Para confirmar que el participante ha leído y firmado el consentimiento informado antes de comenzar"* (EV-16, aplicado al protocolo de entrevista, extendido aquí como requisito del propio sistema).

### RNF-09. Seguridad de los datos personales almacenados (Seguridad, derivado legal)
- **Descripción:** los datos personales de los trabajadores deben cifrarse en reposo y en tránsito.
- **Métrica:** cifrado AES-256 en base de datos y TLS 1.2 o superior en toda comunicación cliente-servidor.
- **Evidencia legal:** Art. 37 y 41 LOPDP (sin evidencia directa de entrevista, requisito regulatorio).

### RNF-10. Posibilidad de disentir de una recomendación sin bloquear el flujo de trabajo (Interacción con el usuario)
- **Descripción:** el usuario debe poder continuar su trabajo normalmente aunque decida no seguir una recomendación de IA, sin que el sistema se lo impida ni lo penalice.
- **Métrica:** 0 casos en los que el sistema bloquee una acción del usuario por no aceptar una recomendación de IA.
- **Evidencia textual:** *"¿Qué haría si una recomendación del sistema no coincide con su experiencia o conocimiento? Lo primero que en este caso haría es comparar con mi experiencia"* (EV-16).

### RNF-11. Reducción del esfuerzo de captura manual de datos (Eficiencia de desempeño)
- **Descripción:** las pantallas de registro frecuente (cosecha, actividad) deben minimizar el número de campos obligatorios y usar selección en vez de texto libre donde sea posible.
- **Métrica:** registrar una cosecha completa debe tomar un máximo de 30 segundos en condiciones normales de campo.
- **Evidencia textual:** *"los datos de manera manual y como es de manera cualitativa, ya que es número, registrarlo, eso sí se hace un poco tedioso"* (EV-17).

### RNF-12. Conservación mínima de registros de trazabilidad (Fiabilidad, derivado legal)
- **Descripción:** los registros de actividad, cosecha y aplicación de insumos deben conservarse un mínimo de 2 años, conforme a la normativa de trazabilidad agroindustrial.
- **Métrica:** ningún registro de los tipos mencionados puede eliminarse antes de cumplir 24 meses desde su creación.
- **Evidencia legal:** Art. 38 de la Resolución AGROCALIDAD 183 (sin evidencia directa de entrevista, requisito regulatorio).

### RNF-13. Compatibilidad con dispositivos de gama baja (Compatibilidad)
- **Descripción:** la aplicación móvil debe funcionar en equipos Android de gama baja, dado el perfil económico de los usuarios de campo.
- **Métrica:** funcionamiento fluido (sin caídas) en un dispositivo con 2 GB de RAM y Android 9 o superior.
- **Evidencia textual:** inferido de que ningún jornalero entrevistado mencionó tener un teléfono de alta gama. Varios reportaron bajo uso previo de aplicaciones (EV-02, EV-13).

### RNF-14. Extensibilidad del catálogo de cultivos y variedades (Mantenibilidad)
- **Descripción:** agregar un nuevo cultivo o variedad al catálogo (RF-02, RF-34) no debe requerir cambios en el código de la aplicación, solo configuración.
- **Métrica:** un administrador debe poder agregar una variedad nueva con su set de atributos en menos de 10 minutos, sin intervención del equipo de desarrollo.
- **Evidencia textual:** *"sería bueno que lo inserten... Maracuyá, la pimienta y el café"* (EV-10). Ver también RF-34 (EV-17).

### RNF-15. Disponibilidad del servicio de notificaciones (Fiabilidad)
- **Descripción:** las notificaciones de bajo stock y asignación de tareas deben entregarse de forma confiable incluso con conectividad intermitente.
- **Métrica:** 95% de las notificaciones deben entregarse dentro de los 5 minutos posteriores a la reconexión del dispositivo.
- **Evidencia textual:** *"Mediante una notificación como un mensaje de texto, algo que creo que es lo más fácil que hoy en día cualquier persona le llegue al celular"* (EV-10).

### 3.3.1 Requisitos no funcionales del componente de inteligencia artificial

Los RF-09, RF-10, RF-31 y RF-33 introducen un componente de IA (alerta de plagas/enfermedades y diagnóstico por imagen). Las seis RNF siguientes gobiernan ese componente de forma transversal, siguiendo el formato identificador/métrica/unidad/umbral/método de verificación/responsable/frecuencia acordado en el reparto de roles del equipo del 2026-09-02.

#### RNF-16. Desempeño de detección/predicción del modelo de IA (Fiabilidad del componente de IA)
- **Descripción:** el modelo que sustenta RF-09 y RF-10 debe alcanzar un nivel mínimo de acierto en la detección de plagas/enfermedades antes de habilitarse en producción.
- **Métrica:** exactitud (accuracy) y sensibilidad (recall) del modelo sobre el conjunto de validación.
- **Unidad:** porcentaje (%).
- **Umbral:** ≥80% de exactitud y ≥75% de sensibilidad en el conjunto de validación, antes de habilitar el modelo en campo.
- **Método de verificación:** evaluación del modelo sobre un conjunto de prueba etiquetado, ejecutada por script versionado, con matriz de confusión documentada en el repositorio.
- **Responsable:** equipo técnico (especificación: Danela Arteaga; análisis estadístico: María Escudero).
- **Frecuencia:** antes de cada despliegue de una versión nueva del modelo, y revisión trimestral en producción.

#### RNF-17. Explicabilidad de las recomendaciones de IA (Transparencia)
- **Descripción:** toda alerta o recomendación generada por el componente de IA (RF-09, RF-10) debe mostrar al usuario al menos un factor que motivó la sugerencia, no solo el resultado, para que el usuario decida con criterio si confirmarla (RF-09) o disputarla (RF-33).
- **Métrica:** proporción de alertas emitidas que muestran al menos un factor explicativo (por ejemplo, "temperatura y humedad elevadas en los últimos 5 días").
- **Unidad:** porcentaje (%) de alertas con explicación.
- **Umbral:** 100% de las alertas deben mostrar al menos un factor explicativo.
- **Método de verificación:** revisión de una muestra de alertas generadas en pruebas de aceptación, confirmando la presencia del campo de explicación.
- **Responsable:** Danela Arteaga (especificación); equipo técnico (implementación).
- **Frecuencia:** en cada entrega que modifique el motor de alertas.

#### RNF-18. Equidad de desempeño entre cultivos (Equidad)
- **Descripción:** el componente de IA no debe generar sistemáticamente peor desempeño (más falsos negativos) para un cultivo respecto del otro, dado que cacao y plátano están igualmente en alcance del estudio de caso.
- **Métrica:** diferencia en la tasa de falsos negativos entre cacao y plátano.
- **Unidad:** puntos porcentuales de diferencia.
- **Umbral:** diferencia ≤10 puntos porcentuales en la tasa de falsos negativos entre ambos cultivos.
- **Método de verificación:** evaluación separada del modelo por subconjunto (cacao, plátano) sobre el conjunto de validación, con reporte comparativo versionado.
- **Responsable:** equipo técnico; revisión independiente por María Escudero (análisis estadístico).
- **Frecuencia:** en cada reentrenamiento del modelo.

#### RNF-19. Supervisión humana obligatoria antes de cualquier acción automática (Supervisión humana)
- **Descripción:** formaliza como requisito transversal lo que RF-09 ya exige en su flujo: ninguna alerta o recomendación de IA puede ejecutar una acción sobre los datos del sistema sin confirmación explícita de una persona.
- **Métrica:** número de acciones aplicadas automáticamente sobre datos del sistema sin confirmación humana.
- **Unidad:** conteo de incidentes.
- **Umbral:** 0 acciones automáticas sin confirmación humana.
- **Método de verificación:** revisión de logs de auditoría y prueba funcional dirigida a intentar forzar una aplicación automática.
- **Responsable:** equipo técnico; verificación independiente por Kamila Calle (gatekeeper P11).
- **Frecuencia:** en cada entrega, como parte de las pruebas de aceptación.

#### RNF-20. Monitoreo continuo del desempeño del modelo en producción (Monitoreo)
- **Descripción:** el sistema debe registrar, para cada alerta de IA, si el usuario la confirmó, la descartó (RF-09) o la disputó (RF-33), para poder calcular el desempeño real del modelo en campo y no solo en el conjunto de prueba.
- **Métrica:** proporción de alertas emitidas con retroalimentación registrada (confirmada, descartada o disputada).
- **Unidad:** porcentaje (%).
- **Umbral:** ≥90% de las alertas deben tener retroalimentación registrada dentro de los 7 días de emitidas.
- **Método de verificación:** consulta sobre el registro de alertas y su estado, generada por script versionado.
- **Responsable:** Roselyn Sánchez (infraestructura de datos); Danela Arteaga (especificación).
- **Frecuencia:** reporte mensual mientras el sistema esté en operación.

#### RNF-21. Clasificación de riesgo de las recomendaciones de IA (Gestión de riesgo)
- **Descripción:** cada tipo de alerta o recomendación del componente de IA debe clasificarse por nivel de riesgo (bajo, medio, alto) según el impacto potencial de seguirla sin verificación —por ejemplo, aplicar un agroquímico implica mayor riesgo que una sugerencia de riego— y ese nivel debe ser visible al usuario junto a la alerta.
- **Métrica:** proporción de tipos de alerta definidos en RF-09/RF-10 con nivel de riesgo asignado y visible en la interfaz.
- **Unidad:** porcentaje (%) de tipos de alerta clasificados.
- **Umbral:** 100% de los tipos de alerta deben tener un nivel de riesgo asignado antes de habilitarse.
- **Método de verificación:** revisión de la tabla de configuración de tipos de alerta, confirmando el campo de nivel de riesgo.
- **Responsable:** Danela Arteaga (especificación); equipo técnico (implementación).
- **Frecuencia:** al definir cada nuevo tipo de alerta.

### 3.4 Historias de usuario y criterios de aceptación

Los 17 requisitos funcionales de prioridad Must have se tradujeron a historias de usuario en formato Connextra, seguidas de un escenario de aceptación en Gherkin construido a partir del criterio de verificación ya definido para cada requisito. Cada historia cumple los criterios INVEST al describir una necesidad independiente, negociable en su implementación, de valor claro para el usuario, estimable, acotada a un solo requisito y verificable mediante el escenario que la acompaña.

**HU-01, ligada a RF-01.** Como administrador, técnico o jornalero, quiero registrar y editar una parcela con sus datos básicos, para tener siempre a la mano el nombre, el cultivo y la cantidad de plantas de cada lote sin depender de la memoria o de papeles sueltos.
Dado que estoy autenticado con permiso de edición, cuando registro una parcela completando los siete campos obligatorios, entonces el sistema la muestra en el listado general en menos de dos segundos y sin campos vacíos.

**HU-02, ligada a RF-03.** Como jornalero o técnico, quiero registrar cada actividad agrícola con su fecha, lote, producto y responsable, para dejar un historial confiable de lo que se hizo en cada parcela.
Dado que estoy autenticado, cuando intento guardar una actividad sin indicar la fecha, el lote o el trabajador responsable, entonces el sistema rechaza el registro hasta que esos tres datos queden completos.

**HU-03, ligada a RF-04.** Como jornalero, quiero registrar la cosecha en la unidad propia de cada cultivo, para no forzar el dato a una unidad que no corresponde con la forma real de trabajo en campo.
Dado que estoy registrando la cosecha de un lote de cacao, cuando elijo la unidad de medida, entonces el sistema solo acepta tacho o quintal, y si el lote es de plátano solo acepta racimo o caja.

**HU-04, ligada a RF-05.** Como administrador, técnico o jornalero, quiero ver el rendimiento promedio de cada lote por periodo, para comparar el desempeño de mis parcelas sin calcularlo a mano.
Dado un lote con dos o más registros de cosecha, cuando consulto su rendimiento, entonces el sistema muestra un promedio igual al que resulta de dividir la suma de las cosechas entre el número de registros.

**HU-05, ligada a RF-06.** Como técnico o jornalero, quiero que el sistema calcule automáticamente la ganancia neta de un periodo, para conocer el resultado económico real sin hacer la resta manualmente.
Dado que existen registros de ingresos y egresos en un periodo, cuando consulto la ganancia neta, entonces el valor mostrado es igual a la suma de ingresos menos la suma de egresos de ese periodo.

**HU-06, ligada a RF-07.** Como administrador, técnico o jornalero, quiero registrar la cantidad usada de un insumo, para saber en todo momento cuánto stock me queda sin contarlo manualmente.
Dado un insumo con treinta unidades disponibles, cuando registro un uso de veintiséis unidades, entonces el sistema muestra cuatro unidades disponibles.

**HU-07, ligada a RF-08.** Como administrador, jornalero o técnica, quiero recibir una alerta cuando el stock de un insumo baje del umbral configurado, para comprar a tiempo antes de quedarme sin insumo para una labor programada.
Dado un insumo cuyo stock cae por debajo del umbral configurado, cuando se registra ese descenso, entonces el sistema envía la notificación al responsable en menos de cinco minutos.

**HU-08, ligada a RF-09.** Como administrador, técnico o jornalero, quiero recibir una alerta de posible plaga o enfermedad que siempre pida mi confirmación antes de aplicarse, para mantener el control sobre las decisiones de manejo del cultivo.
Dado que el sistema genera una alerta de plaga sobre un lote, cuando la alerta se muestra al usuario responsable, entonces queda registrada como pendiente de confirmar o descartar y en ningún caso se aplica de forma automática al lote.

**HU-09, ligada a RF-11.** Como administrador, técnico o jornalero, quiero asignar tareas a un trabajador por lote y fecha y poder filtrarlas por estado, para saber en cualquier momento qué falta, qué está en curso y qué ya se completó.
Dado que existen tareas en distintos estados, cuando filtro la lista por el estado pendiente, entonces el sistema solo muestra las tareas que están en ese estado.

**HU-10, ligada a RF-19.** Como administrador o técnico, quiero generar reportes de producción, costos y pérdidas con gráficos, para presentar la información de la finca de forma visual y tomar decisiones más rápido.
Dado un rango de fechas y uno o varios lotes seleccionados, cuando genero el reporte, entonces los valores mostrados corresponden exactamente a la suma de los registros de ese rango.

**HU-11, ligada a RF-20.** Como técnico, quiero que el sistema pida usuario y contraseña y respete los permisos de cada rol, para que cada persona solo pueda ver y hacer lo que corresponde a su función.
Dado un usuario con rol de jornalero, cuando intenta acceder al módulo financiero, entonces el sistema le niega el acceso.

**HU-12, ligada a RF-22.** Como administrador, quiero registrar el consentimiento de cada trabajador para el tratamiento de sus datos personales, para cumplir con la Ley Orgánica de Protección de Datos Personales antes de guardar cualquier información suya en el sistema.
Dado un trabajador que va a usar el sistema por primera vez, cuando intenta iniciar sesión sin haber registrado su consentimiento, entonces el sistema le solicita aceptarlo antes de continuar.

**HU-13, ligada a RF-23.** Como trabajador, quiero poder acceder, rectificar o eliminar mis propios datos personales dentro del sistema, para ejercer los derechos que me reconoce la Ley Orgánica de Protección de Datos Personales.
Dado que estoy autenticado en el sistema, cuando solicito ver, corregir o eliminar mis datos personales, entonces el sistema atiende la solicitud y deja un registro de la acción realizada.

**HU-14, ligada a RF-24.** Como administrador, quiero registrar el certificado de salud vigente del trabajador que aplica agroquímicos, para cumplir con lo exigido por la Resolución 183 de AGROCALIDAD antes de asignarle esa labor.
Dado un trabajador sin certificado de salud vigente registrado, cuando intento asignarle una tarea de aplicación de agroquímicos, entonces el sistema advierte que el certificado no está registrado.

**HU-15, ligada a RF-26.** Como técnico o jornalera, quiero registrar manualmente cada ingreso y egreso con su concepto, monto y fecha, para llevar un control independiente además del cálculo automático de ganancia.
Dado que registro un ingreso o un egreso con su concepto, monto y fecha, cuando reviso el reporte financiero del periodo correspondiente, entonces ese movimiento aparece reflejado en él.

**HU-16, ligada a RF-34.** Como técnico, quiero que el catálogo de cultivos muestre un conjunto de campos distinto según la variedad seleccionada, para registrar los datos agronómicos propios de cada variedad de cacao o de plátano.
Dado que selecciono una variedad de cacao en el formulario, cuando el formulario se despliega, entonces muestra un conjunto de campos distinto al que se muestra al seleccionar plátano.

**HU-17, ligada a RF-37.** Como jornalero, técnico o administrador, quiero poder registrar y avisar de inmediato ante síntomas sospechosos de una plaga cuarentenaria como el moko, para activar el protocolo de bioseguridad exigido por AGROCALIDAD sin perder tiempo.
Dado que un usuario reporta síntomas compatibles con una plaga cuarentenaria en un lote, cuando registra el aviso, entonces el sistema lo marca con prioridad alta y lo deja visible para el administrador de forma inmediata.

### 3.5 Trazabilidad legal

La cobertura de los 26 criterios legales frente a los requisitos elicitados por entrevista y frente a los requisitos derivados directamente del texto legal se documenta fila por fila en `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx`. Esa matriz es la que alimenta el diseño de la prueba de McNemar del protocolo experimental, al marcar cada uno de los 26 criterios como cubierto o no cubierto antes y después de aplicar el método legal-first.

---
## 4. Modelado del sistema

El modelado completo está en `03_Modelado/`, con 32 diagramas en formato `.drawio` y su exportación a imagen, más la especificación textual de los casos de uso y las historias de usuario. Toma como base el diagrama de contexto de la Sección 2.2 y el modelado organizacional i estrella de la Sección 2.4, y desarrolla a partir de los 39 requisitos funcionales y 21 no funcionales de la Sección 3.

### 4.1 Actores y casos de uso

El sistema tiene tres actores humanos, administrador, técnico y trabajador agrícola, y dos actores externos, el motor de recomendaciones de inteligencia artificial y AGROCALIDAD como entidad reguladora. El diagrama general de casos de uso reúne 14 casos de uso en alcance, CU-01 a CU-14, con el detalle textual de precondiciones, poscondiciones, flujo básico, flujos alternativos y reglas de negocio en `03_Modelado/00_Use_Case_Specifications.md`. CU-15, la vía de integración con sensores del RF-32, queda documentado como Won't have y no se desarrolla.

| Caso de uso | Requisitos que agrupa |
|---|---|
| CU-01 Gestionar parcelas y lotes | RF-01, RF-02, RF-16, RF-29, RF-34, RF-35 |
| CU-02 Registrar actividades agrícolas | RF-03 |
| CU-03 Registrar cosecha | RF-04, RF-13, RF-14, RF-15 |
| CU-04 Calcular rendimiento y finanzas | RF-05, RF-06, RF-26 |
| CU-05 Gestionar inventario de insumos | RF-07, RF-08, RF-30 |
| CU-06 Alertas de plagas asistidas por IA | RF-09, RF-10, RF-31, RF-33 |
| CU-07 Asignar y dar seguimiento a tareas | RF-11, RF-12, RF-27, RF-28 |
| CU-08 Generar reportes | RF-19 |
| CU-09 Autenticación y control de acceso | RF-20, RF-22, RF-23 |
| CU-10 Visitas técnicas | RF-21 |
| CU-11 Riesgo laboral y equipo de protección | RF-18, RF-24 |
| CU-12 Canal rápido de reporte | RF-17 |
| CU-13 Cumplimiento BPA | RF-25, RF-36, RF-38, RF-39 |
| CU-14 Aviso de plaga cuarentenaria | RF-37, RF-38 |

Las historias de usuario con criterios de aceptación en Gherkin están en `03_Modelado/00_User_Stories_Acceptance_Criteria.md`, una por cada requisito funcional Must have que la lleva, según la regla de la guía de modelado.

### 4.2 Modelo de dominio

El dominio se reparte en dos diagramas de clases. `CD01_Refined_Class_Diagram` cubre el dominio operativo, con la jerarquía de usuario, parcela, cultivo, cosecha, labor, insumo, reporte y las clases de recomendación y alerta de inteligencia artificial. `CD02_Legal_Compliance_Class_Diagram` cubre el dominio de cumplimiento legal derivado del enfoque legal-first, con las clases de consentimiento, solicitud de derechos del titular, visita técnica, riesgo laboral, aviso fitosanitario, bitácora de bioseguridad, certificación BPA, registro de capacitación, lote de exportación y transacción financiera.

### 4.3 Comportamiento

El comportamiento se documenta con 7 diagramas de actividad, con calles por actor, que cubren el flujo operativo principal, la alerta de inventario, las recomendaciones de inteligencia artificial, el consentimiento y los derechos ARCO+ de la LOPDP, la visita técnica y el cumplimiento BPA, el riesgo laboral y el aviso de plaga cuarentenaria. Los 14 diagramas de secuencia siguen la separación en capas de frontera, control y entidad, con fragmentos de alternativa y barras de activación. Dos diagramas de estados modelan el ciclo de vida de una tarea de labor y el de una alerta de inteligencia artificial. Este segundo diagrama fija la regla central del RF-09, ninguna alerta se aplica de forma automática a un lote sin la confirmación del usuario responsable, y el camino del RF-33, en el que un desacuerdo formal mantiene la alerta fuera del conjunto aplicado hasta que la revise el equipo técnico.

### 4.4 Arquitectura de componentes

El diagrama de componentes divide el backend en módulos, `AuthModule` y `UserModule` para autenticación y usuarios, `PlotCropModule` para parcelas y catálogo, `TaskModule` para tareas, `InventoryModule` para insumos, `ReportModule` para cosecha, rendimiento y reportes, `AIIntegrationModule` para la integración con el motor de recomendaciones, y `ComplianceModule` para todo el dominio de cumplimiento LOPDP y AGROCALIDAD. El cliente es una aplicación web que consume una API REST sobre HTTPS. Los actores externos son el motor de recomendaciones, conectado por su propia API sin capacidad de modificar datos de forma autónoma, y la pasarela de reporte a AGROCALIDAD para los avisos de las Resoluciones 183 y 0072.

### 4.5 Mockups

Hay 9 pantallas en `03_Modelado/Mockups/`, MU-01 a MU-09, cada una en un archivo HTML autónomo y exportada a imagen, más `MU-00_Prototype.html` como prototipo navegable que las enlaza. Cubren inicio de sesión y consentimiento, listado de parcelas, registro de actividad, registro de cosecha, alerta de inventario, alerta de inteligencia artificial, tablero de tareas, panel de reportes y la pantalla de cumplimiento y visitas técnicas.

### 4.6 Diagrama de despliegue

Este diagrama no depende de los requisitos funcionales y ya está definido en `05_MVP/docker-compose.yml`.

```
+-----------------------------------------------+
|              Host Docker                        |
|                                                  |
|  +--------------------+   +-------------------+ |
|  | Contenedor:         |   | Contenedor:       | |
|  | agromoreira_backend |-->| agromoreira_db    | |
|  | (Node.js / Express)  |   | (PostgreSQL 16)   | |
|  | puerto 3000          |   | puerto 5432        | |
|  +--------------------+   +-------------------+ |
|           ^                    |                 |
+-----------|--------------------|-----------------+
            |                    |
      HTTP (cliente,        Volumen persistente
      navegador o app movil) agromoreira_db_data
```

El backend expone la lógica de negocio a través de una API REST y la base de datos PostgreSQL cuenta con un chequeo de salud antes de aceptar tráfico del backend. Todo el conjunto se levanta con `docker compose up` desde `05_MVP/`. El diagrama de despliegue completo, con el dispositivo cliente, el servidor de aplicación, el servidor de base de datos y los nodos externos del motor de recomendaciones y de AGROCALIDAD, está en `03_Modelado/Diagrams/DEP01_Deployment_Diagram.drawio`.

## 5. Priorización y trazabilidad

Los 39 requisitos funcionales cuentan con su prioridad MoSCoW asignada dentro de cada ficha de la Sección 3. Sobre esa base, el equipo completo realizó el 1 de septiembre de 2026 una sesión de priorización complementaria con el modelo de Kano y el método WSJF, del marco ágil SAFe. La clasificación Kano de cada requisito, en básico, de desempeño, atractivo o indiferente, se definió por consenso del equipo a partir de la evidencia cualitativa recogida en las 17 entrevistas y no de una encuesta Kano formal aplicada a los participantes, ya que esa encuesta específica no formó parte del instrumento de campo. Para el WSJF, el equipo asignó a cada requisito cuatro valores del 1 al 10, valor de negocio, urgencia, reducción de riesgo u oportunidad, y tamaño del esfuerzo, y el puntaje final se calculó como la suma de los tres primeros valores dividida entre el tamaño del esfuerzo.

El resultado completo, con los 39 requisitos y su ranking final, se documenta en `priorizacion_moscow_kano.csv`. Los diez requisitos de mayor prioridad según este método son los siguientes.

| Ranking | ID-RF | MoSCoW | Kano | WSJF |
|---|---|---|---|---|
| 1 | RF-26, registro manual de ingresos y egresos | Must have | Básico | 6.5 |
| 2 | RF-08, alertas automáticas de bajo stock | Must have | De desempeño | 6.3 |
| 2 | RF-13, registro de motivo de rechazo de fruta | Should have | De desempeño | 6.3 |
| 4 | RF-02, catálogo cerrado de cultivos y variedades | Should have | Básico | 6.0 |
| 4 | RF-22, consentimiento del trabajador para tratamiento de datos | Must have regulatorio | Básico | 6.0 |
| 4 | RF-37, aviso ante plaga cuarentenaria | Must have regulatorio | Básico | 6.0 |
| 7 | RF-18, registro de riesgo laboral y equipo de protección | Should have | Básico | 5.6 |
| 7 | RF-24, certificado de salud del trabajador | Must have regulatorio | Básico | 5.6 |
| 7 | RF-38, bitácora de bioseguridad de ingreso y salida | Should have regulatorio | Básico | 5.6 |
| 10 | RF-30, umbral de stock mínimo configurable | Should have | De desempeño | 5.3 |

El requisito con menor prioridad resultante es el RF-32, la vía de integración futura con sensores de campo, coherente con su prioridad MoSCoW de Won't have para esta versión.

La matriz de trazabilidad está cerrada en `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx`, con 60 filas. Son 54 filas base, una por cada requisito funcional, no funcional o derivado del catálogo actual, y 6 filas secundarias para los seis requisitos que dan servicio a un segundo caso de uso además del principal. Cada fila enlaza la ley o la fuente de elicitación, el artículo, el objetivo, el interesado, el código de evidencia, el requisito, el tipo, el caso de uso, la historia de usuario y su criterio de aceptación cuando corresponde, el componente y el mockup. Todos los identificadores de caso de uso, componente y mockup coinciden con los del paquete de modelado de la Sección 4.

## 6. Producto mínimo viable

El producto mínimo viable está en `05_MVP/`, con la arquitectura de contenedores Docker descrita en la Sección 4.6. El backend en Node.js con Express y PostgreSQL implementa el esquema de base de datos derivado del modelo de dominio y los endpoints que cubren 15 de los 17 requisitos funcionales Must have de la Sección 3, RF-01, RF-03, RF-04, RF-05, RF-06, RF-07, RF-08, RF-09, RF-11, RF-19, RF-20, RF-22, RF-26, RF-34 y RF-37. Levanta con `docker compose up` y trae una prueba de humo de extremo a extremo. Quedan como interfaz de cliente el RF-12, la notificación push de tareas, y el RF-10, el diagnóstico por imagen, ambos dependientes de servicios externos.
