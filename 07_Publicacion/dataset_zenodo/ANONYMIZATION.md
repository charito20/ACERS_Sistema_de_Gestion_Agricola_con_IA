# Anonimización, AgroMoreira

Cómo se trató cada tipo de dato antes de incluirlo en este paquete público. Basado en `08_Etica/C3_Protocolo_Anonimizacion_Agricola_Moreira.pdf`, Protocolo de anonimización de datos empresariales sensibles, documento adicional C3 de la categoría ética C.

| Elemento | Tratamiento aplicado |
|---|---|
| Nombre de la organización | Se maneja según el documento C3 y el aval de unidad productiva (documento C1), que rigen cómo se nombra a la organización en los artefactos públicos del proyecto |
| Nombres de participantes | Reemplazados por códigos de participante (ENTR-01, ENTR-02, ...) en todas las transcripciones y respuestas |
| Ubicación geográfica exacta | Generalizada a nivel de cantón o provincia; ninguna fotografía conserva coordenadas GPS (eliminadas con `exiftool -gps:all=`) |
| Volúmenes de producción | Presentados en rangos o normalizados a porcentajes, nunca en cifras absolutas |
| Precios y márgenes | No se reportan en ningún artefacto público |
| Cédulas y firmas | Nunca aparecen en la zona pública; solo en el contenedor cifrado `02_Evidencias/00_Restringido/` |
| Fotografías del entorno | Sin rostros identificables, sin metadatos GPS |
| Respuestas del cuestionario | Sin columnas de nombre, correo, teléfono ni dirección IP |
| Documentos de la organización | Precios, márgenes, volúmenes de producción e información tributaria tachados de forma irreversible antes de subir |

## Verificación

Cada archivo de este paquete fue revisado contra esta lista antes de subirlo, confirmando que ninguna columna ni ningún campo contiene nombre, cédula, correo, teléfono, dirección o IP.

## Tabla de correspondencia entre código y persona real

No existe en este paquete ni en ningún lugar del repositorio público. Se mantiene bajo custodia exclusiva del docente responsable (Ing. Gleiston Guerrero Ulloa), conforme al Plan de Gestión de Datos (documento A.4).
