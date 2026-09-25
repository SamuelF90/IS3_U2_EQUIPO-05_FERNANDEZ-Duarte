# Sistema de solicitudes ciudadanas

Práctica de la Unidad 2 de Ingeniería de Software III: historias de usuario, Product Backlog, Kanban y Sprint Planning.

## Equipo

| Integrante | Usuario de GitHub | Rol académico |
| --- | --- | --- |
| Samuel Fernandez | [@SamuelF90](https://github.com/SamuelF90) | Product Owner y desarrollo |
| Diana Duarte | [@dianaduartev99](https://github.com/dianaduartev99) | Facilitadora Scrum/Kanban, relatora y desarrollo |

## Caso y visión

Una institución necesita un sistema web para gestionar solicitudes ciudadanas, respetar plazos formales y adaptarse a la retroalimentación del piloto. La visión es que ciudadanos y personal institucional puedan registrar, seguir y gestionar solicitudes de forma trazable, oportuna y auditable, sin usar datos personales reales.

## Enlaces de trabajo

- Repositorio: <https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte>
- Project: <https://github.com/users/SamuelF90/projects/1>

## Sprint 1

- Duración: dos semanas.
- Sprint Goal: permitir que un ciudadano registre una solicitud básica y consulte su estado inicial mediante un código de seguimiento.
- Capacidad acordada: 16 puntos de historia, considerando 8 puntos por integrante.
- Historias seleccionadas: registrar solicitud básica, generar código de seguimiento, validar datos obligatorios, consultar estado mediante código y mostrar información inicial del estado.
- Total comprometido: 16 puntos.
- Riesgo principal: definir estados obligatorios y plazos formales sin información normativa detallada durante el piloto.
- Criterio de éxito: un ciudadano puede registrar una solicitud ficticia, recibe un código y visualiza un estado inicial sin exponer información sensible.

## Políticas Kanban

- **Backlog:** historia identificada, pero todavía no lista para trabajar.
- **Preparada:** cumple Definition of Ready: narrativa, criterios verificables, dependencias conocidas y estimación acordada.
- **En curso:** tiene responsable y comenzó una tarea verificable.
- **En revisión:** el autor terminó la historia y otra persona valida los criterios de aceptación.
- **Hecha:** cumple criterios de aceptación, revisión cruzada, evidencia enlazada y Definition of Done.
- Límites WIP: **En curso <= 3** y **En revisión <= 2**. Si se alcanza un límite, se finaliza o revisa trabajo antes de iniciar otro.

## Simulación Kanban

Durante la simulación se detectó un posible cuello de botella cuando dos historias alcanzan el límite de **En revisión** y una tercera no puede ingresar a esa columna. La acción acordada es que la facilitadora priorice la revisión cruzada y que el equipo no inicie trabajo nuevo hasta liberar capacidad de revisión.

## Decisiones de priorización

1. El registro y el código de seguimiento se ubican primero porque habilitan cualquier consulta o gestión posterior y entregan valor inmediato al ciudadano.
2. La consulta de estado se prioriza antes de adjuntos y derivaciones porque completa el objetivo mínimo del Sprint 1 y reduce consultas presenciales.
3. El control de plazos y la derivación son Must, pero se planifican después del flujo básico: dependen de contar con una solicitud identificada y con estados definidos.

## Definition of Done

- Los criterios de aceptación fueron revisados por un integrante distinto del responsable.
- La evidencia o prototipo está enlazado en el Issue cuando corresponde.
- No hay tareas abiertas ni bloqueos sin registrar.
- Los campos del Project están actualizados.
- Las decisiones que afecten al equipo se reflejan en este README o en la documentación.
