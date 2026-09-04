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

## Cobertura de RF "Debe tener"

Numeración corregida para que coincida con el catálogo actual de 39 RF de `01_ERS/ERS_SRS_2B_v2.0.md` (la versión anterior de esta lista usaba una numeración antigua de una fase previa del proyecto, ~RF-01 a RF-16, que ya no corresponde al catálogo vigente):

- RF-01 Registro de parcelas/lotes
- RF-02 Catálogo cerrado de cultivos y variedades
- RF-03 Registro de actividades agrícolas
- RF-04 Registro de cosecha por unidad específica del cultivo
- RF-07 Gestión de inventario de insumos
- RF-08 Alertas automáticas de bajo stock
- RF-11 Asignación y seguimiento de tareas
- RF-19 Reportes de producción (parcial en este MVP: totales por parcela; sin costos, pérdidas ni gráficos todavía)
- RF-20 Gestión de usuarios y control de acceso

Las referencias `RF-XX` y `CU-XX` visibles dentro de la aplicación (pie de página de cada módulo) también se corrigieron para apuntar a este mismo catálogo vigente y a `03_Modelado/00_Use_Case_Specifications.md` (CU-01 a CU-14).

## Video de demostración
`video_demo01.mp4` a `video_demo08.mp4` (8 videos cortos, uno por módulo principal).
