# Unidad 2 - Enfoque, Product Backlog y acuerdos de trabajo

## Contexto y adaptación del enfoque

El producto es una aplicación para que estudiantes y funcionarios reporten incidentes del campus, adjunten evidencia, consulten el estado y valoren la solución. El personal de mantenimiento administra, asigna y actualiza los incidentes. Las prioridades cambian según urgencias del campus y la experiencia de los usuarios.

Se adopta un enfoque ágil porque el Product Owner puede aclarar necesidades dos veces por semana, el alcance detallado puede emerger durante el trabajo y se necesita inspeccionar incrementos cada dos semanas. Scrum organiza los incrementos en tres Sprints y Kanban controla el flujo de solicitudes de soporte.

El caso describe un equipo de desarrollo de cinco integrantes. Esta entrega académica es producida por Samuel Fernandez y Diana Duarte; por ello se reduce el alcance técnico a un prototipo demostrable y se documentan las decisiones de gestión como simulación académica cuando no provienen de un Sprint ejecutado. No se presentan métricas simuladas como datos reales.

## Visión y objetivo de Release

**Visión:** centralizar el reporte y seguimiento de incidentes del campus para que las personas conozcan el avance de una solicitud y mantenimiento pueda priorizar su resolución de forma trazable.

**Release Goal:** entregar una primera versión demostrable que permita registrar un incidente, adjuntar evidencia, consultar su estado y que un responsable autorizado lo actualice hasta su resolución. La valoración de la solución completa el ciclo de retroalimentación.

## Scrum y Kanban

| Elemento | Decisión | Evidencia esperada |
| --- | --- | --- |
| Scrum | Tres Sprints de dos semanas con Planning, Daily, Review y Retrospective. | Sprint Goal, Sprint Backlog, incremento y actas. |
| Kanban | Flujo visual para soporte y tareas durante el Sprint. | Tablero con estados, WIP y bloqueos. |
| Product Owner | Prioriza por valor, riesgo y dependencia; aclara historias dos veces por semana. | Backlog ordenado y decisiones de cambio. |
| Scrum Master | Facilita eventos, protege el Sprint Goal y elimina impedimentos. | Retrospectiva y registro de impedimentos. |
| Equipo de desarrollo | Estima, construye, prueba, actualiza el tablero y entrega el incremento. | Commits, PR, pruebas y demo. |

| Columna Kanban | Límite WIP | Política explícita |
| --- | ---: | --- |
| Backlog | Sin límite | Trabajo identificado, todavía no listo. |
| Preparada | 4 | Cumple DoR y puede seleccionarse en Planning. |
| En desarrollo | 3 | No se inicia una cuarta tarea: primero se ayuda a terminar una activa. |
| En pruebas | 2 en S1; 1 desde S2 | Si se alcanza el límite, se prioriza revisar, corregir y terminar. |
| Hecha | Sin límite | Cumple la DoD y está disponible para Review. |

Scrum no se usa para recibir solicitudes urgentes de manera informal. La solicitud entra primero al Product Backlog; solo se incorpora al Sprint actual si Product Owner y equipo comprueban que no compromete el Sprint Goal ni excede la capacidad. De otro modo se refina y reordena para el siguiente Sprint.

## Definition of Ready

Una historia puede pasar a **Preparada** cuando:

1. Está escrita en formato “Como [rol], quiero [capacidad], para [beneficio]”.
2. Tiene criterios de aceptación verificables y el Product Owner resolvió dudas conocidas.
3. Tiene valor, prioridad, dependencias, riesgos y supuestos identificados.
4. Fue estimada mediante Planning Poker y cabe en un Sprint.
5. No presenta bloqueadores conocidos de diseño, acceso, datos o proveedor.
6. Su evidencia de aceptación y prueba es comprensible para desarrollo y revisión.

## Definition of Done inicial

Una historia pasa a **Hecha** cuando:

1. Implementa todos sus criterios de aceptación.
2. Tiene pruebas automatizadas o pasos manuales reproducibles, ejecutados con resultado registrado.
3. Fue revisada mediante Pull Request por una persona distinta del autor.
4. No tiene defectos críticos abiertos, secretos ni datos reales.
5. Está integrada en `main`, documentada y disponible para demostración en el ambiente de pruebas o como artefacto.

La Unidad 7 amplía esta DoD con controles de seguridad, accesibilidad, cobertura y deuda técnica.

## Product Backlog inicial

La prioridad combina valor para usuarios, riesgo técnico y dependencia. `Must` representa trabajo indispensable para el Release Goal; `Should` aporta valor importante y puede reordenarse si la capacidad observada lo exige.

| Orden | ID | Historia y beneficio | Pri. | SP | Dependencia | Criterios de aceptación resumidos |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | HU-01 | Como usuario, quiero registrarme para acceder a funciones personalizadas. | Must | 3 | Ninguna | Valida obligatorios; evita identificador duplicado; confirma creación. |
| 2 | HU-02 | Como usuario registrado, quiero iniciar sesión para proteger mis reportes. | Must | 2 | HU-01 | Credenciales válidas permiten acceso; inválidas informan error; rutas protegidas lo exigen. |
| 3 | HU-03 | Como usuario, quiero reportar un incidente para comunicar un problema del campus. | Must | 5 | HU-02 | Captura categoría y descripción; valida requeridos; crea incidente con estado `Abierto`. |
| 4 | HU-04 | Como usuario, quiero adjuntar evidencia para facilitar el diagnóstico. | Must | 3 | HU-03 | Acepta JPG, PNG o PDF; limita tamaño; asocia archivo al incidente; rechaza tipo no permitido. |
| 5 | HU-05 | Como usuario, quiero consultar mis incidentes para seguirlos. | Must | 3 | HU-03 | Muestra solo reportes propios; exhibe título, fecha y estado; conserva el identificador del incidente. |
| 6 | HU-07 | Como responsable, quiero visualizar incidentes recibidos para organizar la atención. | Must | 3 | HU-03 | Lista incidentes con categoría, ubicación y estado; solo rol autorizado accede; ordena los más recientes. |
| 7 | HU-09 | Como responsable, quiero asignar un incidente a un área para definir responsable. | Should | 2 | HU-07 | Permite seleccionar área válida; registra asignación; muestra responsable en seguimiento. |
| 8 | HU-10 | Como responsable, quiero priorizar incidentes para atender urgencias. | Should | 2 | HU-07 | Registra prioridad válida; cambios quedan trazables; lista ordenada por prioridad y fecha. |
| 9 | HU-08 | Como responsable, quiero actualizar el estado para reflejar el avance. | Must | 3 | HU-07 | Solo rol autorizado actualiza; acepta estados válidos; cambio se conserva y aparece al usuario. |
| 10 | HU-06 | Como usuario, quiero consultar el estado para conocer el avance. | Must | 2 | HU-05, HU-08 | Muestra estado actual; se actualiza tras cambio autorizado; no expone datos de otros usuarios. |
| 11 | HU-16 | Como usuario autorizado, quiero consultar historial para auditar cambios. | Should | 3 | HU-08 | Registra estado anterior/nuevo, fecha y actor autorizado; ordena cronológicamente; protege acceso. |
| 12 | HU-11 | Como usuario, quiero recibir aviso de cambios para no consultar manualmente. | Should | 5 | HU-08 | Notifica cambio de estado; identifica incidente; evita notificar a quien no corresponda. |
| 13 | HU-12 | Como usuario, quiero valorar una solución resuelta para dar retroalimentación. | Should | 3 | HU-08 | Solo permite 1 a 5 en estado `Resuelto`; una valoración por incidente; confirma registro. |
| 14 | HU-14 | Como administrador, quiero gestionar categorías para clasificar incidentes. | Could | 3 | HU-03 | Crea, edita o desactiva categoría; no invalida incidentes existentes; solo administrador accede. |
| 15 | HU-13 | Como responsable, quiero ver estadísticas para detectar problemas recurrentes. | Could | 5 | HU-07, HU-08 | Muestra conteos por categoría/estado; filtra período; evita exponer identidad de reportantes. |
| 16 | HU-15 | Como administrador, quiero gestionar roles para controlar permisos. | Could | 5 | HU-01 | Cambia solo roles permitidos; registra auditoría; impide quitar el último administrador. |

## Cambio obligatorio posterior al Sprint 1

Estas historias no pertenecen al Backlog inicial. Se incorporan después de cerrar Sprint 1, se refinan con Product Owner, seguridad y mantenimiento, y se reordenan para Sprint 3.

| Orden revisado | ID | Historia y beneficio | Pri. | SP | Dependencia | Criterios de aceptación resumidos |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | HU-17 | Como usuario, quiero reportar de forma anónima para comunicar situaciones sensibles sin exponer mi identidad. | Must | 3 | HU-03 | El modo es explícito; no persiste ni vincula usuario, IP o metadata de dispositivo; informa límites de anonimato. |
| 2 | HU-18 | Como usuario, quiero aportar geolocalización para precisar una falla de mantenimiento. | Must | 5 | HU-03 | Solicita consentimiento; permite omitirla y usar referencia manual; reduce precisión; informa propósito y retención. |

La prioridad de HU-17 y HU-18 desplaza HU-13, HU-14 y HU-15 a una Release posterior si la velocidad observada confirma que no caben sin sacrificar el Sprint Goal.
