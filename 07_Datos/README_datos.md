# 07_Datos — Paquete de datos ACERS

## Qué contiene
Paquete de datos crudos y procesados del componente empírico del proyecto ACERS
(enfoque legal-first: cobertura de obligaciones legales de la Ley Orgánica de
Protección de Datos y de trazabilidad agroindustrial por los RF elicitados).

- `datos_crudos/`: exportación exacta de los instrumentos (matriz de correspondencia
  legal-requisito sin editar, hojas de evaluación independiente, respuestas de
  cuestionario), tal como salieron del instrumento, sin ninguna edición manual.
- `datos_procesados/`: resultado de ejecutar `scripts/run_all.py` sobre `datos_crudos/`.
  Nunca se edita a mano.
- `scripts/`: orquestador único (`run_all.py`) que lee `datos_crudos/`, produce
  `datos_procesados/` y genera todas las tablas y figuras citadas en el ERS y el manuscrito.
- `resultados/`: tablas y figuras generadas exclusivamente por los scripts.
- `diccionario_datos.csv`: descripción columna por columna de cada archivo de datos.
- `checksums_datos.sha256`: hash de cada archivo depositado.
- `desviaciones.md`: registro de toda diferencia respecto del protocolo pre-registrado.
- `registro_deposito.md`: identificador persistente del depósito (Zenodo/OSF) y su fecha.

## Cómo se reproduce
```
cd 07_Datos
pip install -r scripts/requirements.txt
python scripts/run_all.py
```
Esta orden única debe reproducir, sin intervención manual, exactamente las mismas
tablas y figuras que aparecen en el ERS y en cualquier reporte del equipo. Si no lo
hace, el paquete de datos no está terminado (criterio de piso P6).

## Estado (actualizar según se vaya llenando)
- [ ] datos_crudos/ contiene la exportación real de cada instrumento
- [ ] datos_procesados/ se genera únicamente por script
- [ ] scripts/run_all.py ejecuta sin error desde un clon limpio
- [ ] diccionario_datos.csv completo
- [ ] checksums_datos.sha256 verificado con `sha256sum -c`
