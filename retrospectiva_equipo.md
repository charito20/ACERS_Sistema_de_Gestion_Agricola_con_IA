# Retrospectiva del equipo ACERS

Proyecto Fin de Curso. Ingenieria de Requerimientos ISR-401, Universidad Tecnica Estatal de Quevedo, 2026-2027 PPA.
Equipo ACERS, Paralelo 4to A.

Este documento responde a la observacion de la evaluacion de la Entrega 4, que pidio una retrospectiva del equipo con acciones y responsables. Recoge lo que funciono, lo que no funciono y las acciones concretas que el equipo asume para la entrega final y para futuros proyectos.

## 1. Que funciono bien

- La matriz de trazabilidad extremo a extremo permitio conectar cada obligacion legal con su requisito, caso de uso y caso de prueba.
- La doble codificacion de la cobertura legal, con calculo de kappa y su intervalo de confianza, dio respaldo estadistico al componente empirico.
- El paquete de datos y el deposito FAIR (Zenodo, OSF, Software Heritage) quedaron completos y verificables por un tercero.
- El paquete etico base (anexos A1 a A13, adenda de segunda ronda, documentos de Categoria C) estuvo completo y a tiempo.
- Las 17 entrevistas de campo, con audios, consentimientos firmados y transcripciones anonimizadas, se realizaron y documentaron.

## 2. Que no funciono, y acciones

| Que paso | Por que paso | Accion | Responsable |
|---|---|---|---|
| El trabajo se concentro en pocos dias y no quedo distribuido en el tiempo | Falta de un ritmo de trabajo acordado desde el inicio; 63 de 64 commits de la primera entrega cayeron en un solo dia, segun verifico el propio docente | Cada integrante registra su trabajo el mismo dia en que lo hace, con commits que digan que cambio y por que. El lider revisa el ritmo del historial cada semana | Todo el equipo, verificacion semanal del lider (Espinoza) |
| El prototipo del MVP vivia en un repositorio separado del declarado en la caratula, y no se habia actualizado desde el 2 de agosto | El MVP se desarrollo en una etapa anterior en otro repositorio y no se integro al repositorio principal a tiempo, hecho que el docente verifico directamente | Se integro 05_MVP al repositorio oficial y se actualizo con los flujos de la version final del ERS | Sanchez (repositorio e infraestructura), con apoyo del equipo en los flujos nuevos |
| Existian dos repositorios activos y la caratula apuntaba a uno distinto del que instruia clonar el README | El equipo migro de repositorio sin dejar por escrito cual era el oficial | Se creo el documento REPOSITORIO_OFICIAL.md que declara el repositorio oficial y explica la migracion. Se unifico la nomenclatura del sistema en README y ERS | Calle (documentacion), confirmacion de todo el equipo |
| Se declaro por error que no existian notas de campo manuscritas de las 17 sesiones de elicitacion | Confusion en la comunicacion interna durante la auditoria de cierre, las notas si se tomaron el mismo dia de cada entrevista pero no se habian cargado todavia al repositorio | Se subieron las 17 notas de campo manuscritas a 10_Autoria/notas_campo/ y se retiro la desviacion correspondiente en 07_Datos/desviaciones.md | Arteaga y Escudero (elicitacion y evidencia) |
| No se tenian fotografias del momento de aplicacion del cuestionario | No se contemplo como evidencia obligatoria al momento de aplicar el instrumento | Se recuperaron y subieron 5 fotografias de la aplicacion del cuestionario | Todo el equipo |
| Veintisiete commits de Danela Arteaga quedaron firmados con un correo Gmail personal en vez del institucional, lo que incumplia el criterio de autoria del historial | Configuracion local de Git desactualizada | Se reescribio el historial con git filter-repo y mailmap, verificado contra un clon nuevo: los commits de main quedaron con el correo institucional correcto. Durante ese proceso un push de etiquetas con --force movio por accidente la etiqueta de linea base a un commit mas viejo, lo cual se corrigio despues creando una etiqueta anotada nueva sobre el commit final | Sanchez (repositorio), regla de no volver a reescribir el historial de aqui en adelante |
| Solo 13 de 47 referencias del ERS tenian DOI resoluble | La bibliografia se armo sin verificar cada DOI contra la publicacion real | Las 47 referencias se verificaron contra Crossref, con DOI completo en todas | Calle (cierre tecnico del manuscrito) |
| El registro OSF original tenia el titulo de otro estudio (Protocolo de validacion de explicabilidad) | El protocolo se registro con el enfoque metodologico previo, antes de fijar el enfoque legal-first como enfoque oficial de la Entrega 4 | Se enmendo el registro OSF documentando el cambio de enfoque | Escudero (protocolo y registros OSF) |
| El manuscrito llego a la evaluacion de la Entrega 4 como un borrador de 4 paginas de una entrega anterior, escrito en futuro, sin el analisis ejecutado y con citas sin resolver | La seccion de resultados dependia del analisis, que se completo despues de esa evaluacion | Se compilo con bibtex hasta resolver las citas, se uso la plantilla Springer ya disponible en el repositorio y se escribieron resultados sobre los datos ya ejecutados | Espinoza y Calle (manuscrito) |
| checksums.sha256 y fichas_tecnicas.csv llegaron a la evaluacion de la Entrega 4 con una sola linea, la de encabezado | No se habia generado el contenido real todavia en ese momento | Ambos archivos se completaron con las fichas y los hashes reales, y checksums.sha256 se regenera antes de cada corte | Sanchez (integridad del repositorio) |

## 3. Acuerdos para la entrega final

1. Commits el mismo dia en que se hace el trabajo.
2. Ninguna reescritura del historial de la rama por defecto.
3. Regenerar y verificar checksums.sha256 antes del corte.
4. Congelar el manuscrito con antelacion al corte.
5. Cada integrante confirma por commit propio los documentos de equipo que le corresponden.
