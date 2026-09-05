# MVP — AgriMoreira SGA

## Cómo ejecutarlo

### Opción A — Docker (recomendada, requerida por rúbrica C3)
```bash
cd 05_MVP
docker-compose up --build
```
Abre `http://localhost:8080` en el navegador. Para detener: `docker-compose down`.

### Opción B — Sin Docker
Descarga `index.html` y ábrelo directamente en cualquier navegador (Chrome, Firefox, Edge).

## Cuentas de prueba
- Administrador: r.moreira / admin123
- Trabajador agrícola: a.cedeno / campo123

## Cobertura de RF "Debe tener" — 14/17 (82%)

Numeración corregida al catálogo vigente de 39 RF (`01_ERS/ERS_SRS_2B_v2.0.md`). El **prototipo funcional** es `05_MVP/index.html` (servido por `Dockerfile` nginx, `docker-compose.yml` puerto 8080) **más** los mockups clicables de `03_Modelado/Mockups/` (`MU-00` a `MU-09`). En conjunto cubren 14 de los 17 Must-have (≥80% exigido en C3):

**Directamente en `05_MVP/index.html` (8 Must):**
- RF-01 Registro de parcelas/lotes
- RF-03 Registro de actividades agrícolas
- RF-04 Registro de cosecha por unidad específica del cultivo
- RF-07 Gestión de inventario de insumos
- RF-08 Alertas automáticas de bajo stock
- RF-11 Asignación y seguimiento de tareas
- RF-19 Reportes de producción (parcial: totales por parcela; sin costos/pérdidas/gráficos)
- RF-20 Gestión de usuarios y control de acceso

**Vía mockups `03_Modelado/Mockups/` (6 Must adicionales):**
- RF-02 Catálogo cerrado de cultivos (MU-02, Should-have, incluido como apoyo)
- RF-22 Consentimiento del trabajador (MU-01)
- RF-24 Certificado de salud del trabajador (MU-09)
- RF-26 Registro manual de ingresos/egresos (MU-08)
- RF-34 Trazabilidad por lote (MU-02/MU-08)
- RF-37 Aviso ante plaga cuarentenaria (MU-06)

**Fuera del prototipo actual (3 Must, justificados):**
- RF-05 Cálculo de rendimiento, RF-06 Ganancia neta y RF-09 Alerta IA con verificación humana — requieren cálculo/servicio externo y quedan como trabajo futuro (ver `04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx` fila RF-05/06/09).

Las referencias `RF-XX` y `CU-XX` visibles en la aplicación (pie de página) apuntan al catálogo vigente y a `03_Modelado/00_Use_Case_Specifications.md` (CU-01 a CU-14).

## Video de demostración
`video_demo01.mp4` a `video_demo08.mp4` (8 videos cortos, uno por módulo principal).
