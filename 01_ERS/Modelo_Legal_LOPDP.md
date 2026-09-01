# Modelo conceptual y criterios de cumplimiento legal

## Adaptación del método de Amaral, Abualhaija, Sabetzadeh y Briand (2021) para AgroMoreira

**Estado:** versión 1.0, cerrada. Cubre tres bloques normativos, la Ley Orgánica de
Protección de Datos Personales del Ecuador y su Reglamento General, la Resolución
Técnica 183 de AGROCALIDAD sobre buenas prácticas y trazabilidad del cacao, y la
Resolución 0072 de AGROCALIDAD sobre bioseguridad y manejo fitosanitario, con 26
criterios de cumplimiento, C1 a C26.

**Método.** Se adapta la conceptualización de Amaral et al. (2021). A diferencia
del trabajo original, que aplica los criterios a un contrato de tratamiento de
datos, aquí cada criterio se evalúa contra el conjunto de requisitos funcionales
y no funcionales de la Sección 3 del ERS. Un criterio se marca como cubierto si al
menos un requisito verificable declara esa información, y como no cubierto si
ningún requisito la cubre. Los criterios sin cobertura son los vacíos legales que
responden a la pregunta de investigación, y los requisitos derivados del texto
legal para cerrarlos son la extensión de cobertura que aporta el método
legal-first.

---

# Bloque 1. Protección de datos personales

**Fuente legal verificada.** Ley Orgánica de Protección de Datos Personales del
Ecuador, Registro Oficial Quinto Suplemento N.º 459, del 26 de mayo de 2021.
Texto oficial en https://www.telecomunicaciones.gob.ec/wp-content/uploads/2021/06/Ley-Organica-de-Datos-Personales.pdf.
Se complementa con el Reglamento General a la Ley, Decreto Ejecutivo 904,
Registro Oficial Tercer Suplemento N.º 435, del 13 de noviembre de 2023.

**Artículo núcleo,** equivalente al Art. 28 del RGPD en el trabajo original. Art.
47, obligaciones del responsable y del encargado del tratamiento de datos
personales. Desde ahí se leyeron los artículos 4, 7, 8, 10, 12 a 24, 25 a 32, 33
a 36, 37 a 46, 48 a 51 y 55 a 60.

## Paso 1. Modelo conceptual jerárquico, adaptado de la Figura 2 del trabajo original

| Nivel 1, tipo de información | Nivel 2, especialización | Artículo LOPDP |
|---|---|---|
| Identidad y contacto del responsable | Nombre o razón social, domicilio legal, correo | Art. 4, Art. 12(8) |
| Identidad y contacto del encargado, por ejemplo un proveedor de nube o un centro de acopio | Nombre, domicilio, correo | Art. 4, Art. 34 y 35 |
| Finalidad del tratamiento | Determinada, explícita, legítima y comunicada al titular | Art. 10(d) |
| Base de legitimación | Consentimiento, obligación legal o interés legítimo | Art. 7, Art. 8 |
| Categorías de datos personales tratados | Datos comunes frente a datos sensibles, biométricos o de salud | Art. 12(5), Art. 25 |
| Tipos de titulares de datos | Trabajador de campo, jornalero, administrador, técnico externo | Implícito, análogo a la categoría de titulares del trabajo original |
| Seguridad de datos personales | Medidas técnicas y organizativas, análisis de riesgo | Art. 37, Art. 40, Art. 41 |
| Plazo de conservación | Tiempo máximo y criterio de eliminación | Art. 10(i) |
| Transferencia o comunicación a terceros | Consentimiento informado del titular y excepciones | Art. 33, Art. 36 |
| Transferencia internacional, relevante si la finca exporta a la Unión Europea | País con nivel adecuado o garantías adecuadas | Art. 55 a 60 |
| Notificación de vulneración de seguridad | A la autoridad en un máximo de 5 días y al titular en un máximo de 3 días | Art. 43, Art. 46 |
| Derechos del titular, ARCO+ | Acceso, rectificación, eliminación, oposición, portabilidad, suspensión y no ser objeto de una decisión automatizada | Art. 13 a 20 |
| Contrato con el encargado | Instrucciones documentadas, prohibición de subcontratar sin autorización, devolución o eliminación al finalizar el servicio | Art. 34, Art. 35 |
| Delegado de protección de datos | Obligatorio si hay tratamiento a gran escala o de datos sensibles | Art. 48 a 50 |
| Responsabilidad proactiva y demostrable | Políticas documentadas, auditorías, registro actualizado | Art. 47(2)(3)(14), Art. 51 |

## Paso 2. Criterios de cumplimiento, adaptados de la Tabla II del trabajo original

| ID | Criterio | Artículo LOPDP |
|---|---|---|
| C1 | Al menos un requisito debe declarar la identidad y el contacto del responsable del tratamiento, Agrícola Moreira | Art. 4, 12(8) |
| C2 | Al menos un requisito debe declarar la identidad y el contacto de cualquier encargado del tratamiento, por ejemplo el proveedor de alojamiento o el centro de acopio si procesa datos personales de productores | Art. 4, 34 y 35 |
| C3 | Debe existir un requisito por cada finalidad de tratamiento de datos personales del sistema | Art. 10(d) |
| C4 | Debe existir un requisito que implemente el mecanismo de consentimiento libre, específico, informado e inequívoco | Art. 8 |
| C5 | Debe existir un requisito que enumere las categorías de datos personales tratadas, por ejemplo datos del personal de campo y datos de administración | Art. 12(5) |
| C6 | Debe existir un requisito no funcional de seguridad de datos con medidas técnicas y organizativas concretas, por ejemplo cifrado y control de acceso | Art. 37, 41 |
| C7 | Debe existir un requisito de plazo de conservación y eliminación de datos personales | Art. 10(i) |
| C8 | Debe existir un requisito que regule la transferencia de datos a terceros, AGROCALIDAD, centro de acopio o exportador, con garantías para el titular | Art. 33, 36 |
| C9 | Debe existir un procedimiento de notificación de vulneración de seguridad a la autoridad y al titular | Art. 43, 46 |
| C10 | Debe existir un requisito que implemente cada uno de los derechos ARCO+, acceso, rectificación, eliminación, oposición, portabilidad y suspensión | Art. 13 a 19 |
| C11 | Si el tratamiento es a gran escala o de datos sensibles, debe existir un requisito de designación de un delegado de protección de datos | Art. 48 |
| C12 | Debe existir un requisito que regule el contrato con el encargado, instrucciones documentadas, prohibición de subcontratar sin autorización y devolución o eliminación de datos al finalizar el servicio | Art. 34 y 35 |
| C13 | Debe existir un requisito de responsabilidad proactiva con evidencia de políticas documentadas y mecanismos de auditoría interna | Art. 47(2)(3)(14) |

## Aplicación del método legal-first al Bloque 1

Los 13 criterios se evaluaron contra el conjunto de 39 requisitos funcionales y 15
no funcionales de la Sección 3 del ERS. Ninguno de los 13 tenía cobertura por la
elicitación convencional, ya que ninguna de las 16 entrevistas trató el
tratamiento de datos personales del sistema. Los vacíos se cerraron con los
requisitos derivados RF-22, consentimiento del trabajador, RF-23, derechos
ARCO+, RNF-08, consentimiento explícito en el primer inicio de sesión, y RNF-09,
seguridad de los datos personales almacenados.

## Notas de alcance del modelo

- El criterio C11, sobre la figura del delegado de protección de datos, se marca
  como obligatorio o no según el volumen real de trabajadores y productores que
  gestione el sistema. El equipo fija ese valor con el administrador de la finca
  antes de evaluar la cobertura.
- El modelo no incorpora el Sistema Único de Registro de Operadores para
  exportación de cacao libre de deforestación a la Unión Europea, normativa de
  AGROCALIDAD de 2026, porque Agrícola Moreira no exporta de forma directa. Si eso
  cambia, añadiría un cuarto bloque de criterios sobre geolocalización de parcelas
  y debida diligencia de deforestación.

---

# Bloque 2. Trazabilidad agroindustrial

**Fuente verificada.** Guía de Buenas Prácticas Agrícolas para Cacao, anexo a la
Resolución Técnica AGROCALIDAD N.º 183, del 20 de septiembre de 2012, en
https://www.agrocalidad.gob.ec/wp-content/uploads/2022/08/Gu%C3%ADa-de-BPA-para-cacao-jul.pdf.

**Artículo núcleo.** Art. 36, del sistema de trazabilidad, y Art. 38, de la
documentación y el registro, leídos junto con los artículos que regulan el
registro de la finca, Art. 3, la seguridad de los trabajadores, Art. 31 a 34, el
empacado y el transporte, Art. 27 y 29, y la certificación, Art. 39 a 43.

## Paso 1. Modelo conceptual

| Nivel 1, tipo de información | Detalle | Artículo, Resolución 183 |
|---|---|---|
| Registro del predio o finca | Identificación del predio, dirección según clave catastral, mapa o croquis de distribución de la finca | Art. 3 |
| Sistema de trazabilidad de extremo a extremo | Identidad del producto desde el campo hasta la comercialización, origen, historia del procesamiento, proveedores, forma de producción, cantidad y clientes | Art. 36 |
| Documentación y registros obligatorios, 14 tipos | Acuerdo, ficha del productor, mapa o croquis, información del terreno, plan de manejo del cultivo, calidad y uso del agua de riego, mantenimiento de equipos de aplicación, limpieza de instalaciones sanitarias, limpieza de maquinaria y equipos, análisis de residuos de plaguicidas, capacitación del personal, aplicación de plaguicidas, aplicación de fertilizantes y tratamientos poscosecha, con conservación mínima de 2 años | Art. 38 |
| Seguridad y salud de los trabajadores | Plan de seguridad de riesgos laborales, funciones y responsabilidades registradas, certificado de salud del personal que manipula el producto, equipo de protección en aplicación de agroquímicos y registro de accidentes de trabajo | Art. 31 a 34 |
| Empacado y etiquetado | Registro de procedencia por lote y etiquetado con nombre del producto, identificación del lote, razón social, contenido neto y bruto y país de origen | Art. 27 |
| Transporte | Registro por embarque con empresa de transporte, transportista, productor o centro de acopio, fecha de embarque, número de lote, variedad y cantidad | Art. 29 |
| Certificación BPA | Solicitud ante AGROCALIDAD, inspección con acta, certificado con vigencia de 3 años y registro en la base de datos de centros de producción agrícola que cumplen con BPA | Art. 39 a 43 |

## Paso 2. Criterios de cumplimiento, C14 a C20

| ID | Criterio | Artículo |
|---|---|---|
| C14 | Debe existir un requisito que implemente el registro digital del predio, identificación, croquis o georreferenciación y dirección según clave catastral | Art. 3 |
| C15 | Debe existir un requisito que implemente la trazabilidad de extremo a extremo del lote, origen, proveedores, forma de producción, cantidad y cliente o destino | Art. 36 |
| C16 | Debe existir un requisito que registre y conserve, por un mínimo de 2 años, cada uno de los 14 tipos documentales obligatorios del Art. 38 | Art. 38 |
| C17 | Debe existir un requisito de gestión de seguridad y salud del personal de campo, plan de riesgos, certificados de salud, protección en aplicación de agroquímicos y registro de accidentes | Art. 31 a 34 |
| C18 | Debe existir un requisito que module el etiquetado y el registro de procedencia de cada lote empacado | Art. 27 |
| C19 | Debe existir un requisito de registro de transporte por embarque | Art. 29 |
| C20 | Debe existir un requisito que soporte el proceso de certificación BPA ante AGROCALIDAD, solicitud, inspección, vigencia y renovación | Art. 39 a 43 |

## Aplicación del método legal-first al Bloque 2

Al evaluar los 7 criterios contra el conjunto de requisitos elicitados, la
mayoría ya tenía cobertura indirecta por RF-01, RF-03, RF-04, RF-14, RF-18 y
RF-19, el registro de la finca, las actividades, la cosecha, la trazabilidad del
lote de exportación y los reportes. Quedaron sin cubrir el certificado de salud
del trabajador, parte del C17, y la certificación BPA formal, C20, que se
cerraron con los requisitos derivados RF-24 y RF-25.

---

# Bloque 3. Bioseguridad y manejo fitosanitario

**Origen.** Este bloque surgió de la entrevista EV-17, con un técnico que
mencionó la bioseguridad contra el Moko, el análisis de suelo previo a la siembra
y el equipo de protección personal, temas que el Bloque 2 no cubría. Se buscó y
verificó la normativa correspondiente.

**Fuentes verificadas.**

- Guía de Buenas Prácticas Agrícolas para Cacao, anexo a la Resolución Técnica
  AGROCALIDAD N.º 183, artículos 8, 17, 18, 19 y 20.
- Plan de Acción para el Control de Ralstonia solanacearum Raza 2, Moko,
  Resolución AGROCALIDAD N.º 0072, del 29 de abril de 2022, en
  https://www.agrocalidad.gob.ec/wp-content/uploads/2022/06/DAJ-20221AD-0201.0072.pdf.

## Paso 1. Modelo conceptual

| Nivel 1, tipo de información | Detalle | Artículo |
|---|---|---|
| Análisis de suelo previo a la siembra | Diagnóstico general al establecer un cultivo en un área nueva, análisis de suelo por fertilidad, residuos de plaguicidas y metales pesados, fuentes de agua y riesgos circundantes | Art. 8 Res. 183 |
| Uso responsable de plaguicidas | Capacitación del personal, manejo de equipos de protección, calibración de equipos, conocimiento de la toxicidad y primeros auxilios | Art. 18(e) Res. 183 |
| Equipo de protección personal en la aplicación | Uso obligatorio del equipo de protección desde el transporte del plaguicida hasta el lavado de los equipos | Art. 18(g) Res. 183 |
| Plan de seguridad laboral y botiquín | Plan escrito de emergencias por intoxicación, números de contacto y botiquín visible y accesible | Art. 18(n)(o) Res. 183 |
| Almacenamiento seguro de plaguicidas | Lugar separado, ventilado y señalizado, con registro de ingreso y salida de productos | Art. 19 Res. 183 |
| Periodo de carencia y residuos | Respetar el periodo de carencia según el agroquímico antes de cosechar | Art. 20 Res. 183 |
| Aviso fitosanitario ante sospecha de plaga cuarentenaria | Reporte a AGROCALIDAD ante síntomas sospechosos de Moko u otra plaga cuarentenaria | Art. 3.6.1(a) Res. 0072 |
| Medidas de bioseguridad de ingreso y salida | Desinfección de calzado, herramientas y vehículos al entrar y salir del predio | Art. 3.6.1(d) Res. 0072, con referencia a la Resolución 110 |
| Capacitación específica en control fitosanitario | Capacitación de todo el personal de la plantación sobre la plaga y su manejo | Art. 3.6.1(f)(g) Res. 0072 |

## Paso 2. Criterios de cumplimiento, C21 a C26

| ID | Criterio | Artículo |
|---|---|---|
| C21 | Debe existir un requisito que registre el análisis de suelo previo a establecer un cultivo en una parcela | Art. 8 Res. 183 |
| C22 | Debe existir un requisito que registre el equipo de protección personal usado en cada aplicación de plaguicidas, con fecha | Art. 18(g) Res. 183 |
| C23 | Debe existir un requisito que registre la capacitación del personal en manejo de plaguicidas, calibración de equipos y primeros auxilios | Art. 18(e) Res. 183 |
| C24 | Debe existir un requisito de aviso o alerta ante síntomas sospechosos de una plaga cuarentenaria, por ejemplo el Moko | Art. 3.6.1(a) Res. 0072 |
| C25 | Debe existir un requisito que documente las medidas de bioseguridad de ingreso y salida del predio | Art. 3.6.1(d) Res. 0072 |
| C26 | Debe existir un requisito de registro de capacitaciones del personal sobre control fitosanitario específico de la plaga | Art. 3.6.1(f)(g) Res. 0072 |

## Aplicación del método legal-first al Bloque 3

Al evaluar los 6 criterios contra el conjunto de requisitos elicitados, dos ya
tenían cobertura por evidencia de entrevista, el análisis de suelo, C21, cubierto
por RF-35 con evidencia EV-17, y el equipo de protección personal, C22, cubierto
por RF-18 con evidencia EV-17 y EV-11. Los otros cuatro, C23 a C26, eran vacíos
legales sin ninguna mención en las 16 entrevistas y se cerraron con los
requisitos derivados RF-36 a RF-39 de la Sección 3 del ERS.
