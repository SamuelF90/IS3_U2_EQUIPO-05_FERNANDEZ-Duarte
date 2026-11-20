# Matriz de trazabilidad - TP 5 (Anexo A)

> **Caso: incidentes del campus** · Issue #20 · Responsable de validación: Diana Duarte (revisión conjunta con
> Samuel Fernandez antes del tag de entrega)

| Unidad | Decisión / actividad | Artefacto o enlace | Criterio de aceptación |
| --- | --- | --- | --- |
| 2 | Scrum para desarrollo y Kanban con límites WIP para soporte; backlog de 16 historias con DoR y DoD | [`docs/tp5/02-enfoque-y-backlog.md`](tp5/02-enfoque-y-backlog.md) · [Project](https://github.com/users/SamuelF90/projects/1) | Backlog con al menos 15 historias, criterios, prioridad y SP; DoR y DoD verificables |
| 3 | Roadmap, Release Goal, tres Sprint Goals, política de cambios urgentes | [`docs/tp5/03-planificacion-y-estimacion.md`](tp5/03-planificacion-y-estimacion.md) | Cada Sprint tiene objetivo, alcance y capacidad; el cambio post-S1 no altera el Sprint en curso |
| 4 | Planning Poker (referencia HU-02 = 2 SP); capacidad de 20 horas-equipo; forecast revisado | [`docs/tp5/03-planificacion-y-estimacion.md`](tp5/03-planificacion-y-estimacion.md#forecast-y-revisión) | Estimación reproducible con rango ±20 %; forecast actualizado con la velocidad observada (17-18 → 16 SP) |
| 5 | Roles, canales, ceremonias, retrospectiva y conflicto urgente | [`docs/tp5/05-personas-y-comunicacion.md`](tp5/05-personas-y-comunicacion.md) | Cada rol tiene responsabilidades y decisiones; el conflicto se resuelve sin horas extra ni alterar el Sprint Goal |
| 6 | Registro de 11 riesgos con disparador, contingencia, residual y seguimiento | [`docs/tp5/06-riesgos.md`](tp5/06-riesgos.md) · Issues `risk`: [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24), [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25) | Cada riesgo tiene responsable, disparador, contingencia y estado por Sprint; mitigaciones reflejadas en spikes, criterios o DoD |
| 7 | QA/QC, ISO/IEC 25010:2023, DoD ampliada, pruebas, accesibilidad, defectos, cobertura y deuda | [`docs/07-calidad.md`](07-calidad.md) · Issues `bug`: [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24), [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25) · [PR #26](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/pull/26) | Ninguna historia es Hecha sin pruebas, revisión, seguridad y accesibilidad; D-01 y D-02 se cierran con pruebas de regresión antes del tag `tp5-v1.0.0` |
| 8 | Ramas, PR, SemVer, ambientes, workflow `CI-CD TP5` con `pip-audit` | [`docs/08-configuracion-devops.md`](08-configuracion-devops.md) · [`.github/workflows/ci-cd.yml`](../.github/workflows/ci-cd.yml) | El artefacto se publica solo si el job `quality` está en verde |
| 9 | Reviews y retrospectivas de 3 Sprints, métricas, cambio obligatorio, mejora comprobada, bitácora de IA | [`docs/09-seguimiento-mejora.md`](09-seguimiento-mejora.md) | Cada métrica tiene fuente, umbral, acción y limitación; cada acción de mejora se comprueba en el Sprint siguiente |

## Cadena de trazabilidad del aporte de Diana

Issue #20 → rama `docs/tp5-gestion-calidad-mejora` → commits `docs(tp5): …` → PR hacia `main` (revisor: Samuel) →
workflow `CI-CD TP5` → merge → tag de entrega `tp5-v1.0.0`.

> Los enlaces a las Unidades 2, 3, 4 y 8 funcionan una vez fusionado el PR de `feature/tp5-planificacion-devops`.
