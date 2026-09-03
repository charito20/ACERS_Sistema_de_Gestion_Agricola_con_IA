# 10_Autoria — Carpeta de autores

Esta carpeta contiene la evidencia de aporte individual de cada integrante del
proyecto ACERS (SGA), exigida por la Guía de desarrollo y consolidación del PFC
(Entrega 4 / 2B).

## Contenido

| Archivo/Carpeta | Código | Descripción |
|---|---|---|
| `bitacora_sesiones.csv` | A1 | Registro de cada sesión de trabajo (fecha, hora, participantes, decisiones, commits) |
| `capturas/` | A4 | Capturas de pantalla de ediciones (nombre: `AAAA-MM-DD_usuario_epsilon.png`) |
| `notas_campo/` | A5 | Escaneos/fotos de notas manuscritas, con fecha visible |
| `fotos_equipo/` | A6 | Fotos del equipo en la finca/organización, EXIF intacto (USB/cable/Drive, **NO WhatsApp**) |
| `doble_codificacion/` | A7 | Dos hojas de codificación + script `calcular_kappa.py` para kappa de Cohen con IC95% |
| `correspondencia/` | A8 | Capturas de mensajes/correos con Agrícola Moreira, fecha visible |
| `declaracion_uso_ia.md` | A9 | Tabla de uso de IA por sección del ERS y del manuscrito |
| `aporte_individual.md` | A10 | Aporte de cada integrante con rutas y commits acreditados |
| `generar_exif_inventario.py` | A11 | Script que genera `exif_inventario.csv` con fecha EXIF, dispositivo y hash SHA256 |
| `diagramas_fuente/` | A3 | Fuentes editables de diagramas (copiados de `03_Modelado/Diagrams/`) |

## Inventario EXIF

Para generar el inventario de metadatos de fotografías (A11):

```bash
python3 10_Autoria/generar_exif_inventario.py \
    10_Autoria/capturas \
    10_Autoria/fotos_equipo \
    02_Evidencias/Fotos_Entorno \
    -o 10_Autoria/exif_inventario.csv
```

## Doble codificación

Para calcular kappa de Cohen (A7):

```bash
python3 10_Autoria/doble_codificacion/calcular_kappa.py \
    codificador_a.csv codificador_b.csv \
    --output 10_Autoria/doble_codificacion
```

## Pendiente por completar (solo Roselyn)

Las carpetas `capturas/`, `grabaciones/`, `notas_campo/`, `fotos_equipo/`,
`correspondencia/` están vacías porque contienen evidencia **personal** de Roselyn
que solo ella puede proveer (capturas de pantalla suyas, fotos con su cámara,
grabaciones de entrevistas donde participó, notas manuscritas, correos con la
finca). No deben rellenarse con datos sintéticos.
