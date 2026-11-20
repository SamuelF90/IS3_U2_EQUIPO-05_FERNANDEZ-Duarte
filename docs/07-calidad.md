# Unidad 7 - Calidad

> **Caso: incidentes del campus** · TP 5 Enfoque Ágil · Issue #20 · Responsable: Diana Duarte
>
> Este documento distingue entre **mediciones reales** sobre el prototipo `prototype_campus/` (rama
> `feature/tp5-planificacion-devops`, commit `1f91b7b`, medido el 20/11/2026) y la **serie simulada** de los tres
> Sprints del caso.

## 7.1. QA y QC

La calidad se construye en cada historia; no hay un "Sprint de calidad".

| | QA - aseguramiento (prevención) | QC - control (detección) |
| --- | --- | --- |
| Objetivo | Que el defecto no se produzca | Encontrar el defecto antes que el usuario |
| Prácticas | DoR con criterios verificables, DoD ampliada, PR con revisión cruzada, ramas cortas, checklist de accesibilidad, refinamiento con el PO | `unittest` en el workflow `CI-CD TP5`, `pip-audit`, pruebas de autorización, prueba exploratoria antes de la Review, aceptación del PO |
| Responsable | Todo el equipo; el SM cuida los acuerdos | Dev 4 (QA y seguridad) coordina; cada Dev prueba lo que construye |

## 7.2. Atributos ISO/IEC 25010:2023

El modelo 2023 tiene nueve características: adecuación funcional, eficiencia de desempeño, compatibilidad,
**capacidad de interacción** (antes "usabilidad"), fiabilidad, seguridad, mantenibilidad, **flexibilidad** (antes
"portabilidad") y protección (*safety*). Se priorizan las que el caso vuelve críticas:

| Característica (subcaracterística) | Necesidad del caso | Criterio verificable | Evidencia |
| --- | --- | --- | --- |
| Adecuación funcional (completitud, corrección) | Reportar, gestionar y valorar un incidente | Cada criterio de aceptación de una historia Hecha tiene una prueba asociada | `prueba_aplicacion.py` cubre el flujo reportar → resolver → valorar |
| Seguridad (confidencialidad, integridad, autenticidad) | Roles, evidencias y reportes anónimos | 401 sin sesión, 403 sin rol; evidencia accesible solo para el reportante o un responsable; contenido del archivo validado; `pip-audit` sin vulnerabilidades | Verificación 7.4; defectos D-01 y D-02 abiertos |
| Capacidad de interacción (accesibilidad, protección contra errores) | Estudiantes y funcionarios con distintos dispositivos y capacidades | Checklist WCAG 2.2 AA: etiquetas, teclado, foco visible, contraste ≥ 4.5:1, mensajes anunciados | Revisión de plantillas 7.6 |
| Fiabilidad (tolerancia a fallos) | No perder el reporte si falla el mapa | Se puede reportar sin geolocalización (referencia manual) | Caso CP-18-03 |
| Mantenibilidad (capacidad de prueba, modificabilidad) | Tres Sprints con cambios de prioridad | Cobertura de `aplicacion.py` ≥ 80 %; deuda técnica registrada y decreciente | Medición real: 76 % (7.7) |
| Eficiencia de desempeño (comportamiento temporal) | Picos de uso al inicio del semestre | p95 < 2 s en las consultas principales con datos de prueba | Spike R-01; prueba de carga DT-04 |

## 7.3. Definition of Done ampliada

Amplía la DoD inicial de la [Unidad 2](tp5/02-enfoque-y-backlog.md#definition-of-done-inicial). Una historia pasa a
**Hecha** solo si:

- [ ] Cumple todos sus criterios de aceptación y el PO la aceptó.
- [ ] Tiene pruebas automatizadas (`unittest`) o pasos manuales reproducibles con el resultado enlazado en la Issue.
- [ ] Su PR fue aprobado por otra persona, con las conversaciones resueltas.
- [ ] El job `quality` de `CI-CD TP5` terminó en verde: pruebas y `pip-audit` sin vulnerabilidades conocidas.
- [ ] Si agrega una ruta protegida: hay pruebas de 401 sin sesión y 403 sin rol (R-10).
- [ ] Si maneja archivos: valida el contenido real y el tamaño, y los sirve solo a usuarios autorizados (R-03, R-11).
- [ ] Si maneja datos personales: guarda lo mínimo; en modo anónimo no guarda `id_reportante`, IP ni metadatos (R-04).
- [ ] Si cambia la interfaz: probada con teclado, con etiquetas y contraste, en 360×800 y 1440×900 (R-06).
- [ ] No agrega secretos, credenciales reales ni datos personales reales al repositorio.
- [ ] No baja la cobertura de `aplicacion.py`.
- [ ] Documentación y matriz de trazabilidad actualizadas.

## 7.4. Estrategia de pruebas

| Nivel | Qué verifica | Herramienta y momento | Estado en el prototipo |
| --- | --- | --- | --- |
| Flujo / integración | Reportar → resolver → valorar | `unittest` + `TestClient`, en cada PR (`quality`) | ✔ 1 prueba en verde |
| Autorización | 401 sin sesión, 403 sin rol | `unittest`, en cada PR | Comportamiento correcto verificado a mano; **falta automatizar** (D-03) |
| Validación de entradas | Campos obligatorios, estados válidos, valoración de 1 a 5 solo si está Resuelto, tipo y tamaño de evidencia | `unittest`, en cada PR | **No cubierto** (líneas 168, 173-180, 204-206, 229 sin ejecutar) |
| Seguridad de dependencias | Vulnerabilidades conocidas | `pip-audit` en `quality` | ✔ En el workflow |
| Análisis estático | Patrones inseguros | CodeQL | No habilitado en el repositorio (Unidad 8) → DT-03 |
| Accesibilidad | WCAG 2.2 AA básico | Checklist manual en cada PR que cambia la interfaz | Revisión 7.6 |
| Regresión | Que no vuelvan defectos corregidos | Una prueba nueva por cada defecto | Se aplica al corregir D-01 a D-03 |
| Exploratoria y aceptación | Uso real del flujo | Sesión de 1 h antes de la Review; aceptación del PO | Verificación del 20/11/2026 |

## 7.5. Casos de prueba de privacidad (HU-17 y HU-18)

**Limitación documentada:** el prototipo todavía no implementa el modo anónimo ni la geolocalización; el campo
`ubicacion` es una referencia de texto. Estos casos quedan **especificados** como criterio de aceptación y se
automatizan cuando las historias se implementen.

| ID | Historia | Caso | Resultado esperado |
| --- | --- | --- | --- |
| CP-17-01 | HU-17 | Reportar con "Modo anónimo" activado | La fila del incidente no tiene `id_reportante` ni IP |
| CP-17-02 | HU-17 | Un responsable abre un incidente anónimo | Ve "Anónimo"; no ve nombre ni rol del reportante |
| CP-17-03 | HU-17 | Abrir el formulario en modo anónimo | Se informa que el texto o las fotos pueden identificar a quien reporta |
| CP-18-01 | HU-18 | Reportar sin dar consentimiento de ubicación | El reporte se crea sin coordenadas |
| CP-18-02 | HU-18 | Reportar con consentimiento | Las coordenadas se guardan con precisión reducida (3 decimales, ≈ 100 m) |
| CP-18-03 | HU-18 | El servicio de mapas no responde | Se puede reportar con la referencia manual |
| CP-18-04 | HU-18 | Incidente cerrado hace más de 90 días | Las coordenadas se eliminan |
| CP-04-03 | HU-04 / R-11 | Pedir una evidencia sin sesión o desde otro usuario | 401 / 403 |

## 7.6. Accesibilidad: revisión de las plantillas

Revisión de `home.html`, `base.html` y `admin.html` contra WCAG 2.2 AA:

| Criterio | Resultado |
| --- | --- |
| Idioma de la página (`lang="es"`) y viewport | ✔ |
| Campos del formulario con `<label>` | ✔ en inicio de sesión, reporte y valoración |
| **A-01**: el `select` de estado en `admin.html` no tiene etiqueta (WCAG 1.3.1 / 4.1.2) | ✘ Agregar `<label>` o `aria-label="Nuevo estado"` |
| **A-02**: el mensaje de confirmación no se anuncia a lectores de pantalla (WCAG 4.1.3) | ✘ Agregar `role="status"` al `<p class="message">` |
| Botones con texto ambiguo ("Guardar", "Actualizar") repetidos por fila | Mejora: incluir el título del incidente en un texto accesible |
| Contraste y foco visible | Pendiente de medir con herramienta del navegador |

## 7.7. Defectos, cobertura y deuda técnica

### Mediciones reales (20/11/2026)

Comando: `CAMPUS_DB_PATH=/tmp/x.db python -m coverage run --source=prototype_campus -m unittest prototype_campus/prueba_aplicacion.py`

| Métrica | Valor | Meta | Decisión |
| --- | --- | --- | --- |
| Pruebas automatizadas | 1 (en verde) | Una por criterio de aceptación crítico | Agregar las pruebas de D-03 y de validación |
| Cobertura de `aplicacion.py` | **76 %** (106/139 sentencias) | ≥ 80 % | Por debajo: lo no cubierto son justamente los caminos de error y seguridad |
| Defectos críticos o altos abiertos | 2 (D-01, D-02) | 0 antes del tag de entrega | Bloquean el `tp5-v1.0.0` |

### Registro de defectos

Severidad: **Crítica** (bloquea el uso o la seguridad) · **Alta** (falla sin alternativa o expone datos) ·
**Media** (hay alternativa) · **Baja** (cosmética). Un defecto crítico abierto bloquea el pase a Hecha y el
despliegue.

| ID | Defecto | Severidad | Historia / riesgo | Corrección propuesta |
| --- | --- | --- | --- | --- |
| D-01 | La evidencia se valida con el `content_type` que declara el cliente: un `.sh` declarado como `image/png` se acepta | Alta | HU-04 / R-03 | Verificar la firma del archivo (bytes iniciales) y la extensión; prueba de regresión |
| D-02 | `/evidencias` se sirve con `StaticFiles` sin autenticación: el archivo se descarga sin sesión | Alta | HU-04 / R-11 | Ruta que verifique sesión y permiso; prueba CP-04-03 |
| D-03 | No hay pruebas automatizadas de 401/403 ni de entradas inválidas | Media | R-10 | Agregar casos a `prueba_aplicacion.py` |
| A-01 | `select` de estado sin etiqueta | Media | HU-08 / R-06 | `aria-label` |
| A-02 | Mensajes no anunciados a lectores de pantalla | Baja | R-06 | `role="status"` |

### Registro de deuda técnica

| ID | Deuda | Origen | Costo estimado |
| --- | --- | --- | --- |
| DT-01 | `SECRET_KEY` con valor por defecto en el código si falta la variable de entorno | Simplificación del prototipo | 0,5 h |
| DT-02 | La cobertura no se mide en el workflow `CI-CD TP5` | Unidad 8 | 1 h |
| DT-03 | Análisis estático (CodeQL) no habilitado | Configuración del repositorio | 1 h |
| DT-04 | Falta prueba de carga (R-08) | Aceptado para la Release 2 | 2 h |

### Serie simulada de los tres Sprints

| Métrica | S1 | S2 | S3 | Umbral | Decisión |
| --- | ---: | ---: | ---: | --- | --- |
| Defectos encontrados en el Sprint | 6 | 4 | 3 | Decreciente | Prueba de regresión por cada defecto |
| Defectos escapados (después de la Review) | 2 | 1 | 0 | ≤ 1 | S1 por encima → WIP de *En pruebas* = 1 (Retro 1) |
| Cobertura de `aplicacion.py` | 65 % | 78 % | 85 % | ≥ 80 % | La DoD exige probar casos de error y de borde |
| Deuda técnica registrada | 5 h | 4 h | 2 h | Decreciente | Pagar con la reserva de calidad |

**Capacidad reservada para calidad:** el 15 % de la capacidad de cada Sprint, unas **3 de las 20 horas-equipo**
(Unidad 4). Forma parte del Sprint Backlog y se usa para regresión, refactorización, documentación y deuda técnica.

> **Limitaciones:** la cobertura indica qué parte del código ejecutan las pruebas, no que no haya defectos. Con
> una sola prueba, el 76 % sobreestima la calidad real de la verificación: el camino feliz recorre mucho código,
> pero los controles de seguridad quedan sin probar.
