# Unidades 3 y 4 - Planificación, estimación y calendario

## Roadmap y dependencias

| Sprint | Duración | Sprint Goal | Alcance planificado | Incremento demostrable |
| --- | --- | --- | --- | --- |
| 1 | Semanas 1 y 2 | Permitir acceso y reporte con evidencia y consulta propia. | HU-01 a HU-05, 16 SP. | Registro, autenticación, reporte, adjunto y consulta. |
| 2 | Semanas 3 y 4 | Permitir que mantenimiento gestione el incidente y el usuario consulte su avance. | HU-06 a HU-10 y HU-16, 15 SP. | Visualización, asignación, prioridad, estado e historial. |
| 3 | Semanas 5 y 6 | Entregar comunicación y privacidad sin superar la capacidad observada. | HU-11, HU-12, HU-17 y HU-18, 16 SP. | Notificación, valoración, anonimato y geolocalización consentida. |

Dependencias principales: HU-01 -> HU-02 -> HU-03 -> HU-05 -> HU-06; HU-03 -> HU-04; HU-03 -> HU-07 -> HU-08 -> HU-16; HU-03 -> HU-17 y HU-18.

## Planificación de Sprint

| Sprint | Capacidad explícita | Criterio de selección | Riesgo/control | Resultado de Planning |
| --- | --- | --- | --- | --- |
| 1 | 16 SP como pronóstico inicial. | Historias Must, sin dependencias externas y alineadas al flujo mínimo. | Validar carga de archivos y acceso antes de Review. | HU-01, HU-02, HU-03, HU-04 y HU-05. |
| 2 | 15 SP; se revisa contra velocidad S1 antes de iniciar. | Gestión esencial y trazabilidad; todas cumplen DoR. | Spike o tarea de investigación si rendimiento/roles bloquean. | HU-06, HU-07, HU-08, HU-09, HU-10 y HU-16. |
| 3 | 16 SP tras observar S1 y reordenar el cambio. | Privacidad y mantenimiento tienen prioridad sobre estadísticas y administración. | Consentimiento, minimización de datos y prueba de anonimato. | HU-11, HU-12, HU-17 y HU-18. |

### Política de cambios urgentes

1. El Product Owner registra el pedido como historia o Issue, con origen y urgencia.
2. El equipo analiza valor, riesgo, dependencia, esfuerzo, privacidad y efecto sobre el Sprint Goal.
3. Si no puede hacerse sin alterar objetivo o capacidad, queda priorizado en el Product Backlog futuro.
4. Si afecta una obligación de seguridad, el Product Owner y el equipo negocian alcance; no se acepta trabajo directo de un stakeholder al equipo.
5. La decisión queda enlazada desde Issue, backlog, Sprint Review y PR.

Después de Sprint 1, seguridad solicita HU-17 y mantenimiento HU-18. Se protege el Goal de Sprint 1: ambas historias se estiman, analizan por privacidad y se programan para Sprint 3. No se modifica retrospectivamente el alcance comprometido.

## Técnica de estimación

Se usa **Planning Poker** con la escala Fibonacci modificada `1, 2, 3, 5, 8, 13, 21` Story Points (SP). HU-02, inicio de sesión, es la historia de referencia de 2 SP: alcance pequeño, tecnología conocida y bajo riesgo.

En refinamiento, el Product Owner explica valor y criterios; cada integrante estima simultáneamente complejidad, esfuerzo, riesgo y pruebas. Los valores extremos explican su criterio y se vota de nuevo hasta obtener consenso. Los SP no se convierten en horas ni se utilizan para evaluar personas.

| Entrada reproducible | Decisión |
| --- | --- |
| Tamaño | SP del Product Backlog de Unidad 2. |
| Duración | Tres Sprints de dos semanas, seis semanas de calendario. |
| Capacidad académica simulada | Cinco roles de entrega x 4 horas efectivas por Sprint = 20 horas-equipo por Sprint; 60 horas para el caso simulado. |
| Esfuerzo/costo de referencia | Para transparentar el supuesto: 60 horas x USD 10/hora = USD 600. Es una referencia académica, no un presupuesto real. |
| Rango de incertidumbre | +/- 20%: 48 a 72 horas y USD 480 a 720, por cambios de prioridad, disponibilidad del PO y riesgo de privacidad/archivos. |
| Responsable de validación | Equipo de desarrollo estima; Product Owner valida prioridad; Scrum Master registra supuestos. |

## Forecast y revisión

| Momento | Velocidad usada | Alcance restante | Decisión |
| --- | ---: | ---: | --- |
| Inicio | 17-18 SP proyectados | 51 SP iniciales | Planificar S1 en 16 SP y no convertir SP en horas. |
| Cierre S1 | 16 SP observados en la simulación académica | 35 SP iniciales; se agregan 8 SP de HU-17/HU-18 | Mantener S2 en 15 SP y reordenar el cambio para S3. |
| Cierre S2 | 15 SP observados en la simulación académica | 28 SP antes del ajuste | Priorizar 16 SP de S3; mover HU-13, HU-14 y HU-15 a Release 2. |
| Cierre S3 | 16 SP observados en la simulación académica | 0 SP del Release Goal revisado | Release 1 entrega flujo principal y cambio de privacidad. |

Los resultados indicados como simulación se reemplazarán por evidencia de GitHub Projects, Issues, PR y Actions si se ejecutan los tres Sprints reales. El forecast se revisa en cada Sprint Review, no se usa para presionar al equipo ni para prometer alcance fijo.
