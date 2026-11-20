# Unidad 5 - Personas y comunicación

> **Caso: incidentes del campus** · TP 5 Enfoque Ágil · Issue #20 · Responsable: Diana Duarte · Revisor: Samuel Fernandez
>
> El caso describe un equipo de desarrollo de cinco integrantes; la entrega la producen dos personas. Los roles del
> caso, la retrospectiva y el conflicto son **simulación académica** coherente con la planificación de
> [Unidades 3 y 4](03-planificacion-y-estimacion.md).

## 5.1. Roles y responsabilidades

Cada desarrollador tiene una especialidad principal para que los responsables de riesgos ([Unidad 6](06-riesgos.md))
y de métricas ([Unidad 9](../09-seguimiento-mejora.md)) sean roles concretos. La responsabilidad sobre el
incremento es compartida.

| Rol del caso | Responsabilidades | Decide sobre | Rinde cuentas en |
| --- | --- | --- | --- |
| Product Owner | Visión, orden del Product Backlog, criterios de aceptación, aceptación del incremento, relación con seguridad y mantenimiento. Disponible dos veces por semana (martes y jueves). | Qué se construye y en qué orden. | Planning, Refinamiento, Review |
| Scrum Master | Facilita eventos, remueve impedimentos, protege el Sprint Goal y el ritmo sostenible, cuida los acuerdos de trabajo. | Cómo se aplica el proceso. | Retrospectiva |
| Dev 1 - Líder técnico | Arquitectura, revisión de PR, base de datos y rendimiento. | Decisiones técnicas junto con el equipo. | Daily, PR |
| Dev 2 - Backend | Endpoints FastAPI, autenticación y autorización, integración de mapas. | — | Daily, PR |
| Dev 3 - Interfaz | Plantillas, diseño responsivo, accesibilidad. | — | Daily, PR |
| Dev 4 - QA y seguridad | Estrategia de pruebas, regresión, revisión de seguridad, registro de defectos. | Puede bloquear el pase a **Hecha** si no se cumple la DoD. | Review, Retrospectiva |
| Dev 5 - DevOps | Workflow `CI-CD TP5`, ambientes, tablero de métricas. | — | Review |

**Responsabilidades compartidas del equipo de desarrollo:** estimar con Planning Poker, armar el plan del Sprint,
mantener el tablero al día, cumplir la DoD y revisar el trabajo de otros: nadie aprueba su propio PR.

**Liderazgo de servicio:** el Scrum Master no asigna tareas, facilita que el equipo se organice. El Product Owner
no agrega alcance dentro del Sprint; negocia el orden del backlog.

### Correspondencia con el equipo real

| Integrante | Rol en el TP (README) | Aporte TP 5 |
| --- | --- | --- |
| Samuel Fernandez | Product Owner y desarrollo | Unidades 2, 3, 4 y 8; integración final |
| Diana Duarte | Facilitadora Scrum/Kanban, relatora y desarrollo | Unidades 5, 6, 7 y 9; validación de calidad, riesgos y métricas |

## 5.2. Canales de comunicación

| Canal | Uso | Regla | Respuesta esperada |
| --- | --- | --- | --- |
| Eventos Scrum | Planning, Daily, Refinamiento, Review, Retrospectiva | Con timebox y salida registrada | — |
| GitHub Issues y [Project](https://github.com/users/SamuelF90/projects/1) | Historias, tareas, defectos (etiqueta `bug`) y riesgos que requieren trabajo técnico (etiqueta `risk`) | **Fuente única** del estado del trabajo | Se actualiza al cambiar de columna |
| Pull Requests | Revisión de código y documentación | Las observaciones quedan escritas en el PR | 1 día hábil |
| Mensajería del equipo | Coordinación diaria y consultas rápidas | Lo que se decide ahí se copia a la Issue correspondiente | Mismo día |
| Registro de supuestos funcionales | Dudas cuando el PO no está disponible | El equipo avanza con un supuesto explícito; el PO lo confirma o corrige en su próxima sesión | Máximo 2 días hábiles |
| Carril **Urgente** del Kanban | Incidente crítico del campus (ver 5.5) | WIP = 1, atiende el Dev de guardia | Inicio en el día |

## 5.3. Ceremonias y cadencias

| Evento | Momento | Timebox | Participantes | Salida verificable |
| --- | --- | --- | --- | --- |
| Sprint Planning | Día 1 (día con PO) | 2 h | PO, SM, Devs | Sprint Goal, Sprint Backlog y capacidad registrados |
| Daily Scrum | Diaria | 15 min | Devs (facilita SM) | Impedimentos marcados en el tablero |
| Refinamiento | Mitad del Sprint (día con PO) | 1 h | PO, SM, Devs | Historias que cumplen la DoR para el próximo Sprint |
| Sprint Review | Último día | 1 h | PO, SM, Devs, interesados | Incremento demostrado y backlog actualizado |
| Retrospectiva | Después de la Review | 1 h | SM, Devs (PO invitado) | 1 o 2 acciones con responsable y métrica |
| Revisión del flujo de soporte | Semanal | 15 min | SM y Dev de guardia | WIP y tiempos del carril de soporte revisados |

**Acuerdos de trabajo:** no se toma trabajo nuevo si una columna alcanzó su límite WIP; no se usan horas extra
para absorber alcance nuevo; toda decisión que afecte al equipo queda en una Issue o en la documentación.

## 5.4. Retrospectiva del Sprint 1 (simulación)

Formato: *Qué funcionó / Qué no funcionó / Qué probamos*. Las retrospectivas de los Sprints 2 y 3 y la
comprobación de cada acción están en la [Unidad 9](../09-seguimiento-mejora.md#92-retrospectivas-de-los-tres-sprints).

- **Funcionó:** colaboración para cerrar el flujo de autenticación (HU-01, HU-02); la columna *En pruebas* hizo
  visibles los defectos antes de la Review.
- **No funcionó:** dos historias llegaron a *En pruebas* el último día (cuello de botella en HU-04); la duda sobre
  qué formatos de evidencia aceptar quedó esperando al PO.
- **Acciones para el Sprint 2:**
  1. Bajar el WIP de *En pruebas* de 2 a 1 y aplicar "terminar antes de empezar". Responsable: SM. Métrica: cycle time.
  2. Crear el Registro de supuestos funcionales. Responsables: PO y Dev 4. Métrica: historias bloqueadas más de 1 día.

## 5.5. Conflicto urgente: urgencia del interesado vs. sostenibilidad del equipo

**Situación (Sprint 2, día 6).** El jefe de Mantenimiento contacta directamente a dos desarrolladores. Para el
viernes quiere una exportación de incidentes a PDF con gráficos, para una presentación ante las autoridades, y
sugiere "quedarse el fin de semana si hace falta". El Sprint Goal 2 (gestión del incidente por mantenimiento)
está al 60 %.

| Parte | Posición | Interés real |
| --- | --- | --- |
| Jefe de Mantenimiento | "Lo necesito ya" | Mostrar datos el viernes |
| Equipo de desarrollo | "No llegamos sin horas extra" | Cumplir el Sprint Goal sin desgaste ni pérdida de calidad |
| Product Owner | — | Mantener el orden de valor y la confianza del interesado |

**Resolución**

1. **Canalizar.** Los desarrolladores no aceptan pedidos directos: registran la solicitud como Issue y avisan al
   SM. Esto aplica la política de cambios urgentes de la [Unidad 3](03-planificacion-y-estimacion.md#política-de-cambios-urgentes).
2. **Proteger el Sprint y el ritmo sostenible.** El SM recuerda el acuerdo de no usar horas extra para absorber
   alcance nuevo: oculta la capacidad real y genera defectos y deuda técnica.
3. **Negociar con el PO el mismo día.** El PO separa la necesidad (tener datos para el viernes) de la solución
   pedida (un módulo de exportación con gráficos).
4. **Acuerdo en dos niveles:**
   - **Inmediato, sin cambiar el Sprint:** el Dev 5 dedica como máximo 1 hora a extraer un CSV de los
     incidentes del período desde la base de prueba. El interesado arma sus gráficos en una hoja de cálculo.
   - **Planificado:** se crea *HU-19 - Exportar reporte en PDF con gráficos*, estimada en 5 SP en el
     Refinamiento. El PO la ubica después de HU-17 y HU-18, por lo que pasa a la Release 2.
5. **Registrar y aprender.** El caso entra en la Retrospectiva del Sprint 2 y se publica para los interesados
   cómo solicitar funcionalidades nuevas.

**Resultado.** Sprint Goal 2 cumplido (15 SP) sin horas extra; el interesado tuvo sus datos el viernes; la
necesidad quedó trazable como HU-19. El riesgo R-09 (capacidad reducida) no se materializó.

**Diferencia con una urgencia real del campus.** Si lo urgente es un incidente de infraestructura crítico, por
ejemplo una pérdida de agua en un laboratorio que la aplicación no permite cambiar de estado, entra por el carril
**Urgente** del Kanban (WIP = 1). El Dev de guardia lo atiende sin renegociar el Sprint, y el tiempo usado se
descuenta de la reserva de capacidad del Sprint.
