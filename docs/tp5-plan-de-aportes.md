# TP 5 - Plan de aportes verificables

## Propósito

Este plan organiza el Trabajo Práctico 5, **Enfoque Ágil**, para el caso de la aplicación de reporte y seguimiento de incidentes del campus. Cada integrante desarrolla, prueba y documenta su parte en una rama propia. La integración solo ocurre mediante Pull Request (PR) revisado por la otra integrante.

El repositorio conserva evidencia anterior de la Unidad 2 sobre solicitudes ciudadanas. Los artefactos de TP 5 deben identificarse explícitamente como **caso: incidentes del campus** para no mezclar ambos casos.

## Diagnóstico de partida

Ya existe material relevante fuera de esta copia de trabajo: tres versiones del informe, capturas de Product Backlog y Sprint, un prototipo FastAPI con autenticación por roles, carga de evidencia, consulta, actualización de estado y valoración, pruebas automatizadas, y documentación inicial de las Unidades 7 a 9.

Antes de la entrega final se debe asegurar evidencia evaluable de las Unidades 2 a 9:

| Área pendiente o a consolidar | Evidencia exigida por la guía |
| --- | --- |
| Unidades 2 a 4 | Backlog de al menos 15 historias con criterios, DoR/DoD, Scrum/Kanban con WIP, roadmap, tres planes de sprint, estimación reproducible, capacidad y forecast. |
| Unidades 5 y 6 | Roles reales, comunicación, conflicto resuelto, registro de al menos 10 riesgos con responsables, disparadores, contingencia y evolución por sprint. |
| Unidad 7 | QA/QC, atributos ISO/IEC 25010, pruebas, accesibilidad, defectos, cobertura y deuda técnica. |
| Unidad 8 | Ramas, PR, SemVer, trazabilidad, ambientes, pipeline CI/CD/DevSecOps y evidencia de ejecución. |
| Unidad 9 | Tres reviews y retrospectivas, métricas interpretadas, cambio obligatorio, mejora comprobada, matriz de trazabilidad y bitácora de IA. |

## Reparto 60/40

| Responsable | Peso | Aporte verificable |
| --- | ---: | --- |
| Samuel Fernandez | 60% | Unidades 2, 3, 4 y 8; integración final del informe y del prototipo. |
| Diana Duarte | 40% | Unidades 5, 6, 7 y 9; validación de calidad, riesgos, métricas y evidencia de ceremonias. |

### Samuel Fernandez - 60%

1. **Unidad 2 - Enfoque y backlog (15%)**
   - Crear `docs/tp5/02-enfoque-y-backlog.md`.
   - Justificar Scrum para desarrollo y Kanban para soporte.
   - Documentar columnas y límites WIP.
   - Incorporar Product Backlog inicial de 16 historias, prioridad por valor/riesgo/dependencia, puntos y criterios de aceptación.
   - Definir DoR y DoD iniciales.

2. **Unidad 3 - Planificación (10%)**
   - Crear `docs/tp5/03-planificacion.md`.
   - Registrar roadmap, Release Goal, objetivos, capacidad y Sprint Backlog de los tres Sprints.
   - Definir la política de cambios y preservar el Sprint Goal ante la solicitud posterior al Sprint 1.

3. **Unidad 4 - Estimación y calendario (15%)**
   - Completar en `docs/tp5/03-planificacion.md` la técnica Planning Poker, historia de referencia, escala, entradas, responsables, capacidad, esfuerzo, costo supuesto, incertidumbre y forecast.
   - Diferenciar claramente estimación inicial, velocidad observada y datos simulados.

4. **Unidad 8 - Configuración, DevOps y entrega (15%)**
   - Adaptar `docs/08-configuracion-devops.md` al caso campus.
   - Incorporar el prototipo real y ejecutar su prueba Python dentro de `.github/workflows/ci-cd.yml`.
   - Verificar que el pipeline tenga calidad, pruebas, análisis de seguridad, artefacto y despliegue a pruebas condicionado al éxito de calidad.
   - Vincular Issue -> rama -> PR -> commit -> workflow -> versión/despliegue.

5. **Integración (5%)**
   - Actualizar `README.md` con enlaces a todos los artefactos de TP 5.
   - Generar el informe final de máximo 20 páginas después de integrar ambos PR.

### Diana Duarte - 40%

1. **Unidad 5 - Personas y comunicación (10%)**
   - Crear `docs/tp5/05-personas-y-comunicacion.md`.
   - Definir responsabilidades de Product Owner, Scrum Master y desarrollo; canales, cadencias y acuerdos.
   - Documentar una retrospectiva y el conflicto entre urgencia del stakeholder y sostenibilidad del equipo, con decisión registrada.

2. **Unidad 6 - Riesgos (10%)**
   - Crear `docs/tp5/06-riesgos.md`.
   - Registrar como mínimo 10 riesgos en formato causa-evento-efecto.
   - Cada fila debe incluir categoría, probabilidad, impacto, prioridad, mitigación, responsable, fecha, disparador, contingencia, residual/secundario, estado y evidencia de revisión.
   - Reflejar las mitigaciones en historias, spikes, criterios de aceptación o DoD.

3. **Unidad 7 - Calidad (10%)**
   - Revisar y completar `docs/07-calidad.md`.
   - Vincular atributos ISO/IEC 25010, QA/QC, pruebas, accesibilidad, defectos, cobertura y deuda técnica con criterios verificables.
   - Verificar que las dos historias de privacidad, reporte anónimo y geolocalización con consentimiento, tengan casos de prueba reales o una limitación documentada.

4. **Unidad 9 - Seguimiento y mejora (10%)**
   - Revisar y completar `docs/09-seguimiento-mejora.md` y `docs/trazabilidad-tp5.md`.
   - Registrar las tres Sprint Reviews y retrospectivas, métricas con fuente/fórmula/umbral/limitaciones/decisión, el cambio obligatorio y la mejora comprobada en el sprint siguiente.
   - Completar matriz de trazabilidad para Unidades 2 a 9 y bitácora de IA con responsable de validación.

## Flujo obligatorio de GitHub

1. Crear una Issue para el aporte, con checklist de los entregables asignados.
2. Crear una rama desde `main` usando el prefijo acordado.
3. Hacer commits pequeños y descriptivos, firmados por la persona que realizó el trabajo.
4. Abrir un PR hacia `main`, enlazando la Issue con `Closes #<numero>`.
5. Ejecutar las pruebas indicadas en el PR y adjuntar el resultado o enlace a GitHub Actions.
6. La otra integrante revisa criterios, evidencia y trazabilidad. No se permite autoaprobación.
7. Solo después de la aprobación y de checks exitosos se hace merge.

## Ramas, PR y commits propuestos

| Responsable | Rama | Título del PR | Commits sugeridos |
| --- | --- | --- | --- |
| Samuel | `feature/tp5-planificacion-devops` | `TP5: planificación, estimación y DevOps del caso campus` | `docs(tp5): definir enfoque, backlog y planificación`; `ci(tp5): validar prototipo y entrega`; `docs(tp5): integrar evidencia de configuración` |
| Diana | `docs/tp5-gestion-calidad-mejora` | `TP5: personas, riesgos, calidad y seguimiento` | `docs(tp5): documentar personas y comunicación`; `docs(tp5): registrar riesgos y mitigaciones`; `docs(tp5): completar calidad y métricas` |

El PR de Samuel debe ser revisado por Diana. El PR de Diana debe ser revisado por Samuel. Los commits existentes de ambos en el repositorio quedan como evidencia histórica, pero estos dos PR prueban la contribución específica al TP 5.

## Cierre de la entrega

Una vez fusionados ambos PR:

1. Samuel integra el informe y sus enlaces.
2. Diana revisa que el informe no exceda 20 páginas y que los datos simulados estén marcados como tales.
3. Ambos validan la matriz de trazabilidad, la bitácora de IA y la demo de 15 minutos.
4. Se crea un tag de entrega, por ejemplo `tp5-v1.0.0`, y se adjunta el enlace al workflow exitoso y al ambiente de pruebas.
