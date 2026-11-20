# Trabajo Practico 5 - Enfoque Agil

## Sistema de incidentes del campus

**Asignatura:** Ingenieria de Software III  
**Integrantes:** Samuel Fernandez y Diana Duarte  
**Repositorio:** <https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte>  
**Entrega versionada:** `tp5-v1.0.0`  
**Fecha:** 20/11/2026

## 1. Resumen ejecutivo

El producto propuesto permite a estudiantes y funcionarios reportar incidentes del campus, adjuntar evidencia, consultar el avance y valorar la solucion. El personal autorizado visualiza, prioriza y actualiza los incidentes. La entrega implementa un prototipo demostrable en FastAPI con SQLite y documenta el enfoque agil, la gestion de personas, riesgos, calidad, configuracion y mejora continua.

Se adopto Scrum para entregar incrementos en tres Sprints de dos semanas y Kanban para visualizar el flujo y limitar el trabajo en curso. La planificacion, las metricas y las ceremonias de los tres Sprints son una simulacion academica; las pruebas, los defectos D-01/D-02, la cobertura, el pipeline y la trazabilidad GitHub son evidencia real del prototipo.

## 2. Enfoque y backlog

La vision es centralizar el reporte y seguimiento de incidentes para que las personas conozcan el avance de su solicitud y mantenimiento pueda resolverla de manera trazable. El Release Goal es registrar un incidente, adjuntar evidencia, consultar su estado y permitir que un responsable autorizado lo actualice hasta la resolucion.

El Product Backlog se priorizo por valor, riesgo y dependencias. El flujo minimo contiene registro, inicio de sesion, reporte, adjunto y consulta propia. Luego se incorporan gestion por mantenimiento, asignacion, prioridad, estado, historial, notificaciones y valoracion. Tras Sprint 1 se agregaron como cambio obligatorio el reporte anonimo (HU-17) y la geolocalizacion consentida (HU-18); se pospusieron estadisticas y administracion para no exceder la capacidad.

El tablero Kanban usa Backlog, Preparada, En desarrollo, En pruebas y Hecha. Sus limites WIP son 4 en Preparada, 3 en desarrollo y 2 en pruebas durante Sprint 1, reducidos a 1 desde Sprint 2. Una historia esta lista cuando tiene narrativa, criterios verificables, dependencia, riesgo, estimacion y evidencia de aceptacion. Esta hecha cuando cumple criterios, pruebas, documentacion e integracion; para trabajo nuevo se exige tambien el control de seguridad y calidad definido en la DoD ampliada.

## 3. Planificacion y estimacion

| Sprint | Objetivo | Alcance | Capacidad |
| --- | --- | --- | ---: |
| 1 | Acceso, reporte con evidencia y consulta propia | HU-01 a HU-05 | 16 SP |
| 2 | Gestion de mantenimiento y consulta del avance | HU-06 a HU-10 y HU-16 | 15 SP |
| 3 | Comunicacion y privacidad | HU-11, HU-12, HU-17 y HU-18 | 16 SP |

Se uso Planning Poker con escala Fibonacci modificada (1, 2, 3, 5, 8, 13 y 21). Los Story Points representan complejidad, esfuerzo, riesgo y pruebas, no horas ni rendimiento individual. El caso simulado considera 20 horas-equipo por Sprint, 60 horas para la release y un rango de incertidumbre de +/-20 %. La velocidad observada en la simulacion fue 16, 15 y 16 SP; por eso la Release 2 absorbe HU-13, HU-14, HU-15 y HU-19.

Todo cambio urgente se registra como Issue, se analiza frente al Sprint Goal y se incorpora solo si no compromete capacidad ni objetivo. El conflicto por una exportacion PDF solicitada durante Sprint 2 se resolvio entregando un CSV puntual y planificando HU-19 para Release 2, sin horas extra.

## 4. Personas, comunicacion y acuerdos

El caso define Product Owner, Scrum Master, liderazgo tecnico, backend, interfaz, QA/seguridad y DevOps. En el equipo real Samuel Fernandez aporto las Unidades 2, 3, 4 y 8 y la integracion; Diana Duarte aporto las Unidades 5, 6, 7 y 9, incluidos riesgos, calidad y metricas.

GitHub Issues y Project son la fuente de estado; los Pull Requests registran la revision; la mensajeria se usa para coordinacion diaria y las decisiones se trasladan a Issues o documentacion. Se establecieron Planning, Daily, Refinamiento, Review y Retrospectiva con salidas verificables. Los acuerdos prohiben iniciar trabajo cuando se alcanza WIP y usar horas extra para absorber alcance nuevo.

## 5. Riesgos y privacidad

Los riesgos se califican como Probabilidad x Impacto. Los principales son: rendimiento de estadisticas, dependencia de mapas, carga maliciosa de archivos, ambiguedad de anonimato, disponibilidad limitada del Product Owner, accesibilidad, exceso de alcance, capacidad reducida y autorizacion incompleta.

Los controles relevantes para esta entrega son:

- Validar extension, tamano y firma binaria real de JPG, PNG y PDF.
- Servir evidencias solo por una ruta autenticada y autorizada para el reportante o administrador.
- Probar 401 sin sesion y 403 sin rol para las rutas protegidas.
- Definir anonimato sin identificador de reportante, IP ni metadatos, y geolocalizacion opcional con consentimiento y precision reducida.
- Revisar accesibilidad, foco, etiquetas y comportamiento en 360x800 y 1440x900.

La verificacion real detecto D-01: se aceptaba un script declarado como PNG; y D-02: las evidencias eran publicas. Ambos se corrigieron en el PR #26, con pruebas de regresion y cierre de las Issues #24 y #25. Los riesgos R-03 y R-11 quedan mitigados para el alcance del prototipo.

## 6. Calidad y DevSecOps

El pipeline `CI-CD TP5` se ejecuta en Pull Requests y en `main`. Instala dependencias, ejecuta `unittest`, exige cobertura minima de 80 % sobre `aplicacion.py`, ejecuta `pip-audit` y publica el prototipo como artefacto solo si el trabajo de calidad es exitoso.

La ejecucion final en `main` posterior al merge del PR #26 fue exitosa. Se obtuvieron 2 pruebas en verde, 85 % de cobertura de `aplicacion.py` y ninguna vulnerabilidad conocida en dependencias segun `pip-audit`. Las regresiones comprueban que un archivo con contenido falso es rechazado, que la antigua ruta publica devuelve 404, que una evidencia sin sesion devuelve 401, que un usuario ajeno recibe 403 y que un administrador autorizado puede acceder.

Se registra como deuda tecnica la clave por defecto del prototipo, la ausencia de CodeQL, la falta de prueba de carga y los hallazgos de accesibilidad A-01 y A-02. Estas mejoras pertenecen a una iteracion posterior y no se presentan como resueltas.

## 7. Seguimiento y mejora

Las retrospectivas simuladas produjeron acciones concretas: reducir WIP de pruebas, registrar supuestos funcionales, validar cambios del workflow en PR y preparar las metricas antes de la Review. La simulacion muestra una reduccion del cycle time de 4,6 a 2,9 dias y de defectos escapados de 2 a 0. Estas metricas se usan para mejorar el proceso, no para comparar ni presionar personas.

La matriz de trazabilidad vincula historias, riesgos, Issues, ramas, Pull Requests, workflow y tag. La version de entrega es `tp5-v1.0.0`, publicada sobre el commit de `main` que contiene la correccion de evidencias.

## 8. Evidencia final y limitaciones

| Evidencia | Resultado |
| --- | --- |
| PR #21 | Plan de aportes fusionado |
| PR #22 | Planificacion, estimacion y DevOps fusionados |
| PR #23 | Personas, riesgos, calidad y seguimiento fusionados |
| PR #26 | Correccion de D-01 y D-02 fusionada en `main` |
| CI de `main` | Exitoso despues del PR #26 |
| Issues #24 y #25 | Cerradas |
| Tag | `tp5-v1.0.0` publicado |

Por la proximidad de la entrega, el PR #26 se fusiono despues de que el pipeline paso, sin una aprobacion cruzada registrada. No se atribuye una aprobacion que no ocurrio. Los PR anteriores y la documentacion conservan la evidencia de la colaboracion del equipo. El prototipo no implementa todavia anonimato, geolocalizacion, CodeQL, pruebas de carga ni la totalidad de las mejoras de accesibilidad; esos puntos estan identificados como trabajo futuro.

## 9. Conclusiones

La entrega aplica un enfoque agil trazable a un caso de incidentes del campus. El backlog, los limites WIP, las decisiones de cambio, los riesgos y la calidad se conectan con evidencia verificable en GitHub. La correccion de las vulnerabilidades de evidencias muestra el ciclo completo de detectar, registrar, corregir, probar y entregar con CI. El tag `tp5-v1.0.0` identifica el estado final validado del repositorio.
