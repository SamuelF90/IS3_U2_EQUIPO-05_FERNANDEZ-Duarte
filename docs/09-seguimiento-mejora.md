# Unidad 9 - Seguimiento y mejora

> **Caso: incidentes del campus** · TP 5 Enfoque Ágil · Issue #20 · Responsable: Diana Duarte
>
> Las reviews, retrospectivas y métricas de los tres Sprints son **simulación académica**, coherente con el
> forecast de [Unidades 3 y 4](tp5/03-planificacion-y-estimacion.md#forecast-y-revisión). No se presentan como datos
> reales. Cuando haya Sprints ejecutados, se reemplazan por datos de GitHub Projects, Issues, PR y Actions.

## 9.1. Sprint Reviews

| | Sprint 1 | Sprint 2 | Sprint 3 |
| --- | --- | --- | --- |
| Sprint Goal | Acceso y reporte con evidencia y consulta propia | Mantenimiento gestiona el incidente y el usuario consulta su avance | Comunicación y privacidad sin superar la capacidad observada |
| Planificado / Hecho | 16 / 16 SP (HU-01 a HU-05) | 15 / 15 SP (HU-06 a HU-10, HU-16) | 16 / 16 SP (HU-11, HU-12, HU-17, HU-18) |
| Incremento demostrado | Registro, inicio de sesión, reporte con evidencia, "Mis reportes" | Bandeja de gestión, estado, asignación, prioridad, historial | Aviso de cambio de estado, valoración, modo anónimo, ubicación consentida |
| Versión | `v0.1.0` | `v0.2.0` | `v0.3.0` |
| Feedback de interesados | Seguridad pide reportes anónimos; Mantenimiento pide geolocalización (**evento de cambio**) | Mantenimiento pide exportar a PDF (→ HU-19, Unidad 5); el PO pide filtrar por área | Los usuarios quieren ver los incidentes en un mapa del campus (→ Release 2) |
| Cambios al backlog | Se agregan HU-17 y HU-18 y se reordenan para S3 | Se agrega HU-19; HU-13, 14 y 15 bajan de prioridad | Cierre de la Release 1; Release 2: HU-13, 14, 15 y 19 |
| Riesgos revisados ([Unidad 6](tp5/06-riesgos.md#64-seguimiento-por-sprint-simulación)) | R-03 baja a 3; R-07 queda como foco | Bajan R-01, R-02, R-05 y R-10 | Bajan R-04 y R-07; R-09 sigue activo |

## 9.2. Retrospectivas de los tres Sprints

Cada retrospectiva deja como máximo dos acciones, con responsable y una métrica para comprobar su efecto en el
Sprint siguiente.

| | Retro S1 | Retro S2 | Retro S3 |
| --- | --- | --- | --- |
| Hallazgo | Dos historias llegaron juntas a *En pruebas*; cycle time de 4,6 días; 2 defectos escapados; bloqueos por dudas al PO | Un cambio de configuración dejó el workflow en rojo 18 min antes de la Review; un supuesto funcional equivocado obligó a rehacer trabajo | Las métricas se armaron a mano el último día; poco tiempo para la prueba exploratoria |
| Acción | (1) WIP de *En pruebas* de 2 a 1 y revisión cruzada temprana. (2) Registro de supuestos funcionales | (1) Probar los cambios del workflow en un PR antes de tocar `main`. (2) Validar los supuestos con el PO en ≤ 2 días | (1) Tomar las métricas del Project y de Actions con una plantilla fija. (2) Agendar la prueba exploratoria el día 9 |
| Responsable | SM; PO y Dev 4 | Dev 5; PO | Dev 5; Dev 4 |
| Métrica de control | Cycle time, defectos escapados, historias bloqueadas más de 1 día | Tiempo de restauración, trabajo rehecho | Horas para armar el tablero, defectos escapados |
| Comprobación | **En S2:** cycle time de 4,6 a 3,4 días; escapados de 2 a 1; ningún bloqueo de más de 1 día → **efectiva, se mantiene** | **En S3:** restauración de 18 a 12 min; ningún trabajo rehecho → **efectiva, se mantiene** | Se comprobará en el Sprint 1 de la Release 2 |

## 9.3. Tablero de métricas ágiles y DevOps (simulación)

| Métrica | S1 | S2 | S3 | Lectura | Decisión |
| --- | ---: | ---: | ---: | --- | --- |
| Burndown (SP restantes) | 16 → 0 | 15 → 0 | 16 → 0 | En S1 la curva quedó plana hasta el día 7: trabajo acumulado al final | Si faltan 3 días y queda más del 40 %, se negocia alcance con el PO |
| Velocidad (SP Hechos) | 16 | 15 | 16 | Media 15,7; estable | Forecast de la Release 2 con 15-16 SP, no con los 17-18 iniciales |
| Lead time (días, Backlog → Hecha) | 8,0 | 7,2 | 6,4 | Baja por mejor refinamiento | Mantener el Refinamiento a mitad del Sprint |
| Cycle time (días, En desarrollo → Hecha) | 4,6 | 3,4 | 2,9 | Baja después del WIP = 1 en *En pruebas* | Mantener el límite |
| WIP máximo | 3 | 2 | 2 | Menos trabajo en paralelo | — |
| Throughput (historias Hechas) | 5 | 6 | 4 | Depende del tamaño de las historias | No comparar Sprints solo por cantidad |
| Defectos escapados | 2 | 1 | 0 | Mejora | Ver [Unidad 7](07-calidad.md) |
| Ejecuciones de `CI-CD TP5` en `main` | 3 | 5 | 6 | Integración más frecuente | — |
| Tasa de fallo de cambios | 0 % | 20 % (1/5) | 0 % | Un fallo de configuración en S2 | Acción 1 de la Retro S2 |
| Tiempo de restauración | — | 18 min | 12 min | Mejora | — |

**Uso ético:** las métricas sirven para que el equipo decida, no para comparar personas ni para presionar. La
velocidad no se compara con otros equipos y los SP no equivalen a horas.

**Limitaciones:** tres Sprints son una muestra pequeña; los datos son simulados; la cobertura no demuestra que no
haya defectos.

## 9.4. Fichas de métricas (Anexo C)

| Métrica | Pregunta de gestión | Fórmula y fuente | Frecuencia / responsable | Línea base → umbral | Acción ante desvío |
| --- | --- | --- | --- | --- | --- |
| Velocidad | ¿Cuánto alcance podemos pronosticar? | Σ SP de historias Hechas según la DoD · Project | Por Sprint / SM | 16 SP → ±20 % de la media | Recalcular el forecast; revisar capacidad e impedimentos |
| Burndown | ¿Llegamos al Sprint Goal? | SP restantes por día · Project | Diaria / SM | Línea ideal → más del 40 % restante con 3 días por delante | Negociar alcance con el PO |
| Cycle time | ¿El trabajo fluye? | Fecha Hecha − fecha En desarrollo · Project | Semanal / Dev 5 | 4,6 días → más de 4 días | Revisar WIP y bloqueos en la Daily |
| Lead time | ¿Cuánto espera un pedido? | Fecha Hecha − fecha de creación de la Issue · Project | Por Sprint / PO | 8 días → más de 8 días | Refinar antes; acortar la cola |
| WIP | ¿Empezamos más de lo que terminamos? | Tarjetas en Preparada, En desarrollo y En pruebas · Project | Diaria / SM | 3 → por encima del límite de la columna | No iniciar trabajo nuevo; ayudar a terminar |
| Defectos escapados | ¿Funciona la DoD? | Issues `bug` abiertas después de la Review | Por Sprint / Dev 4 | 2 → más de 1 | Prueba de regresión; revisar la DoD en la Retro |
| Cobertura | ¿Está probada la lógica? | Sentencias ejecutadas / sentencias de `aplicacion.py` · coverage.py | Por PR / Dev 4 | **76 % real (20/11/2026)** → menos de 80 % | No pasar a Hecha sin pruebas nuevas |
| Fallo de cambios y restauración | ¿Integrar es seguro? | Ejecuciones fallidas / total; minutos de rojo a verde · Actions | Por Sprint / Dev 5 | 0 % → más del 15 % o más de 30 min | Analizar la causa en la Retro |

## 9.5. Evento de cambio obligatorio (post-Sprint 1)

**Pedido:** Seguridad pide reportes anónimos y Mantenimiento pide geolocalización.

1. **Proteger el Sprint Goal:** el pedido llega en la Review 1, con el Sprint 1 cerrado; no se modifica ningún Sprint
   en curso.
2. **Refinar y evaluar la privacidad:**

| Historia | Criterios refinados | Evaluación de privacidad | Verificación |
| --- | --- | --- | --- |
| HU-17 Reporte anónimo (3 SP) | Modo explícito; no guarda `id_reportante`, IP ni metadatos; informa los límites del anonimato | Minimización de datos; R-04 | CP-17-01 a 03 |
| HU-18 Geolocalización (5 SP) | Consentimiento previo; ubicación opcional; referencia manual; precisión reducida; se borra 90 días después del cierre | Consentimiento, finalidad y retención definidos; R-02 | CP-18-01 a 04 |

3. **Reordenar:** con la velocidad observada (16 SP), el Sprint 3 incluye HU-11, HU-12, HU-17 y HU-18. HU-13, HU-14 y
   HU-15 pasan a la Release 2 (R-07).

## 9.6. Mejora de proceso comprobada

| Elemento | Registro |
| --- | --- |
| Hallazgo S1 | Dos historias llegaron juntas a *En pruebas*; cycle time de 4,6 días; 2 defectos escapados |
| Acción | WIP de *En pruebas* de 2 a 1 (ya reflejado en la tabla Kanban de la Unidad 2) y revisión cruzada temprana |
| Comprobación S2 | WIP máximo de 3 a 2; cycle time de 4,6 a 3,4 días; defectos escapados de 2 a 1 |
| Conclusión | La mejora tuvo efecto sin aumentar los defectos; se mantiene y se vuelve a revisar en S3 (cycle time 2,9) |

## 9.7. Bitácora de uso de IA

Según la regla 4 de la guía. No se ingresaron datos personales, credenciales ni documentos institucionales no
autorizados. Responsable de la validación de esta sección: Diana Duarte. Solo se registran usos de IA que se pueden documentar con datos verificables.

| Fecha | Herramienta | Propósito | Indicación (resumen) | Resultado aprovechado | Verificación humana | Correcciones |
| --- | --- | --- | --- | --- | --- | --- |
| 20/11/2026 | Claude | Revisar las Unidades 5, 6, 7 y 9 contra la guía y el plan de aportes; verificar el prototipo | Guía del TP, borrador .docx y "guiame para desarrollar las Unidades 5, 6, 7 y 9 en el repositorio" | Disparadores y contingencias de riesgos; reviews y retros de 3 Sprints; fichas de métricas; medición de cobertura; pruebas de seguridad del prototipo | Sobre el commit `1f91b7b` del prototipo se ejecutaron `python -m unittest prototype_campus/prueba_aplicacion.py` (1 prueba, OK) y `python -m coverage run --source=prototype_campus -m unittest prototype_campus/prueba_aplicacion.py` (`aplicacion.py`: 76 %, 106/139 sentencias). Se reprodujeron D-01 (un `.sh` declarado como `image/png` devuelve 303 y queda guardado) y D-02 (`GET /evidencias/<archivo>` sin sesión devuelve 200), y se confirmó que coinciden con el código: línea 173 (`content_type`) y línea 33 (`StaticFiles`). Diana revisó los archivos del PR #23 antes de pasarlo a revisión. | Prioridades P×I recalculadas; HU-13 coherente con la Release 2; stack alineado a FastAPI y SQLite; capacidad alineada a 20 horas-equipo |

> El equipo es responsable del contenido final, aunque haya sido sugerido por una herramienta de IA.
