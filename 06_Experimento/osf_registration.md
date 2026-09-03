# Comprobante de registro previo en OSF — Enfoque 2 legal-first

**Proyecto:** ACERS - Sistema de Gestion Agricola con IA para verde y cacao (Finca Agricola Moreira)
**Integrante responsable:** Escudero Plaza Maria del Rosario
**URL persistente del registro:** https://osf.io/7cvhy
**Fecha de registro:** 2 de agosto de 2026
**Estado:** Registro publico verificado contra la API publica de OSF. Anterior a la tercera ronda de campo (orden correcto).

---

## Datos del registro en OSF

| Campo | Valor |
|---|---|
| Plataforma | Open Science Framework (OSF) |
| URL | https://osf.io/7cvhy |
| Titulo registrado | Protocolo de validacion de explicabilidad |
| Fecha de creacion | 2 de agosto de 2026 |
| Visibilidad | Publico |
| Licencia | CC BY 4.0 |

## Verificacion

El registro fue verificado contra la API publica de OSF (`https://api.osf.io/v2/registrations/7cvhy/`) el 1 de septiembre de 2026. La respuesta confirmo titulo, fecha y estado publico.

## Contenido del preregistro

### Pregunta de investigacion
Que requisitos legales de la Ley Organica de Proteccion de Datos y de trazabilidad agroindustrial no quedan cubiertos por los RF elicitados con metodos convencionales, y como el enfoque legal-first de Amaral et al. extiende esa cobertura.

### Hipotesis
- H0: La proporcion de criterios cubiertos (C1-C26) no difiere antes vs despues de aplicar legal-first.
- H1: La proporcion difiere, mayor despues de legal-first. Alfa 0.05. Prueba McNemar pareada.

### Variables
- Independiente: momento evaluacion (antes convencional vs despues legal-first)
- Dependiente: cobertura binaria por criterio (0=no cubierto, 1=cubierto) para C1-C26
- Control: mismo set 26 criterios, comparacion pareada

### Diseno
Comparacion de proporciones pareadas sobre 26 criterios. Fuente: 01_ERS/Modelo_Legal_LOPDP.md (3 bloques: LOPDP C1-C13, BPA cacao C14-C20 Res.183, Bioseguridad C21-C26 Res.0072) vs 01_ERS/ERS_SRS_2B_v2.0 (39 RF +15 RNF) y 04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx

### Plan de analisis
1. Tabla pareada C1-C26: cubierto_convencional (0/1) y cubierto_legalfirst (0/1)
2. Descriptivos: proporcion global y por bloque (LOPDP, BPA, Bioseguridad)
3. McNemar mcnemar.test en R sobre tabla 2x2
4. IC 95% diferencia proporciones por bootstrap 10k replicas
5. Alfa 0.05

### Materiales
- 01_ERS/Modelo_Legal_LOPDP.md (26 criterios verificados)
- 01_ERS/ERS_SRS_2B_v2.0.pdf
- 04_Trazabilidad/Matriz_Trazabilidad_v2.xlsx
- 06_Experimento/protocolo.tex (legal-first v2B)
- 07_Datos/scripts/analisis_legalfirst.py

### Datos y licencia
Dataset anonimizado en Zenodo CC BY 4.0, FAIR. Zona [R] cifrada AES-256.
