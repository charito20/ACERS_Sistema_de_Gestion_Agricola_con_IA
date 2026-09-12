# Retrospectiva del equipo ACERS
Proyecto Fin de Curso. Ingeniería de Requerimientos ISR-401, Universidad Técnica Estatal de Quevedo, 2026-2027 PPA.
Equipo ACERS, Paralelo 4to A.

Este documento responde a la observación de la evaluación de la entrega 4, que pidió una retrospectiva del equipo con acciones y responsables. Recoge lo que funcionó, lo que no funcionó y las acciones concretas que el equipo asume para la entrega final y para futuros proyectos.
## 1. Qué funcionó bien
- La matriz de trazabilidad extremo a extremo permitió conectar cada obligación legal con su requisito, caso de uso y caso de prueba.
- La doble codificación de la cobertura legal, con cálculo de kappa y su intervalo de confianza, dio respaldo estadístico al componente empírico.
- El paquete de datos y el depósito FAIR (ZENODO, OSF, Software Heritage) quedaron completos y verificables por un tercero.
- El paquete ético base (anexos A1 a A13, adenda de segunda ronda, documentos de categoría C) estuvo completo y a tiempo.
- Las 17 entrevistas de campo, con audios, consentimientos firmados y transcripciones anonimizadas, se realizaron y documentaron.

## 2. Qué no funcionó y acciones
| Qué pasó | Por qué pasó | Acción | Responsable |
| --- | --- | --- | --- |
| El trabajo se concentró en pocos días y no quedó distribuido en el tiempo | Falta de un ritmo de trabajo acordado desde el inicio; 63/64 commits de la 1ra Entrega cayeron en un sólo día, según verificó el propio docente | Cada integrante registra su trabajo el mismo día en que lo hace, con commits que digan qué cambió y por qué. El líder revisa el ritmo del historial cada semana | 
Todo el equipo, verificación semanal de líder (Robinson) |
| El prototipo del MVP vivía en un repositorio separado del declarado en la carátula, y no se había actualizado desde el 2 de agosto | El MVP se desarrolló en una etapa anterior en otro repositorio y no se integró al repositorio principal a tiempo, hecho que el docente verificó directamente |
Se integró 05_MVP al repositorio oficial y se actualizó con los flujos de la versión final del ERS | Sánchez (repositorio e infraestructura), con apoyo del equipo en los flujos nuevos | 
| Las notas de campo no se registraron de forma manuscrita y sistemática en cada sesión de elicitación | No se asignó a nadie la responsabilidad de tomar notas durante la entrevista | Documentar la situación como desviación en 07_Datos/Desviaciones.md. En futuras rondas, el entrevistador redacta una nota de campo breve inmediatamente después de cada sesión |
Arteaga y Escudero (elicitación y evidencia) | 
| No se tenía fotografías del momento de aplicación en el cuestionario | No se contempló como evidencia obligatoria al momento de aplicar el instrumento | Se recuperaron y subieron 5 fotografías de la aplicación del cuestionario | 
Todo el equipo | 
| 27 commits de Danela Arteaga quedaron firmados por un correo gmail personal en vez del institucional lo que incumplía el criterio de autoría del historial | Configuración local del Git desactualizada
| Se reescribió el historial con Git y mailmap, verificado contra un clon nuevo
