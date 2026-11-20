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

### 2.1 Product Backlog priorizado

| Orden | ID | Historia resumida | Prioridad | SP | Dependencia | Criterio de aceptacion verificable |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | HU-01 | Registrarse para acceder a funciones personalizadas | Must | 3 | Ninguna | Valida obligatorios, evita identificador duplicado y confirma la creacion |
| 2 | HU-02 | Iniciar sesion para proteger los reportes | Must | 2 | HU-01 | Credenciales validas permiten acceso y las rutas protegidas lo exigen |
| 3 | HU-03 | Reportar un incidente del campus | Must | 5 | HU-02 | Captura categoria y descripcion, valida requeridos y crea estado Abierto |
| 4 | HU-04 | Adjuntar evidencia para diagnosticar | Must | 3 | HU-03 | Acepta JPG, PNG o PDF, limita tamano, valida contenido real y protege acceso |
| 5 | HU-05 | Consultar incidentes propios | Must | 3 | HU-03 | Muestra solo reportes propios, con fecha, titulo y estado |
| 6 | HU-07 | Visualizar incidentes recibidos | Must | 3 | HU-03 | Solo el rol autorizado accede y lista los incidentes recientes |
| 7 | HU-09 | Asignar un incidente a un area | Should | 2 | HU-07 | Registra una asignacion valida y la muestra en el seguimiento |
| 8 | HU-10 | Priorizar incidentes urgentes | Should | 2 | HU-07 | Conserva la prioridad y ordena por prioridad y fecha |
| 9 | HU-08 | Actualizar estado del incidente | Must | 3 | HU-07 | Solo rol autorizado actualiza estados validos y conserva el cambio |
| 10 | HU-06 | Consultar el estado actualizado | Must | 2 | HU-05, HU-08 | Refleja cambios autorizados sin exponer datos ajenos |
| 11 | HU-16 | Consultar historial para auditar | Should | 3 | HU-08 | Registra actor, fecha, estado anterior y nuevo en orden cronologico |
| 12 | HU-11 | Recibir aviso de cambios | Should | 5 | HU-08 | Notifica al usuario correcto e identifica el incidente |
| 13 | HU-12 | Valorar una solucion resuelta | Should | 3 | HU-08 | Acepta 1 a 5, una valoracion por incidente resuelto |
| 14 | HU-14 | Gestionar categorias | Could | 3 | HU-03 | Solo administrador crea, edita o desactiva sin invalidar incidentes |
| 15 | HU-13 | Consultar estadisticas | Could | 5 | HU-07, HU-08 | Muestra conteos por categoria y estado, con filtro de periodo |
| 16 | HU-15 | Gestionar roles | Could | 5 | HU-01 | Restringe roles permitidos y evita quitar el ultimo administrador |

### 2.2 Cambio de alcance posterior a Sprint 1

| ID | Historia incorporada | SP | Decision de privacidad y prioridad |
| --- | --- | ---: | --- |
| HU-17 | Reportar de forma anonima | 3 | No persiste identificador, IP ni metadatos; Must para Sprint 3 |
| HU-18 | Aportar geolocalizacion | 5 | Requiere consentimiento, permite omitirla y reduce precision; Must para Sprint 3 |

El cambio se registro despues de cerrar Sprint 1. No se cambio retrospectivamente el alcance comprometido y las historias HU-13, HU-14 y HU-15 se trasladaron a Release 2.

### 2.3 Acuerdos de flujo y calidad

| Elemento | Acuerdo verificable |
| --- | --- |
| Definition of Ready | Narrativa, criterios verificables, valor, prioridad, dependencia, riesgo, estimacion y evidencia de aceptacion comprensible |
| Definition of Done inicial | Criterios implementados, prueba reproducible, revision por otra persona, sin secretos ni defectos criticos, integrado y demostrable |
| WIP Preparada | Maximo 4 historias |
| WIP En desarrollo | Maximo 3 historias; se ayuda a terminar antes de iniciar una cuarta |
| WIP En pruebas | Maximo 2 en Sprint 1 y 1 desde Sprint 2 |
| Trabajo urgente | Entra como Issue y se evalua contra capacidad y Sprint Goal; no se acepta trabajo informal directo |

## 3. Planificacion y estimacion

| Sprint | Objetivo | Alcance | Capacidad |
| --- | --- | --- | ---: |
| 1 | Acceso, reporte con evidencia y consulta propia | HU-01 a HU-05 | 16 SP |
| 2 | Gestion de mantenimiento y consulta del avance | HU-06 a HU-10 y HU-16 | 15 SP |
| 3 | Comunicacion y privacidad | HU-11, HU-12, HU-17 y HU-18 | 16 SP |

Se uso Planning Poker con escala Fibonacci modificada (1, 2, 3, 5, 8, 13 y 21). Los Story Points representan complejidad, esfuerzo, riesgo y pruebas, no horas ni rendimiento individual. El caso simulado considera 20 horas-equipo por Sprint, 60 horas para la release y un rango de incertidumbre de +/-20 %. La velocidad observada en la simulacion fue 16, 15 y 16 SP; por eso la Release 2 absorbe HU-13, HU-14, HU-15 y HU-19.

Todo cambio urgente se registra como Issue, se analiza frente al Sprint Goal y se incorpora solo si no compromete capacidad ni objetivo. El conflicto por una exportacion PDF solicitada durante Sprint 2 se resolvio entregando un CSV puntual y planificando HU-19 para Release 2, sin horas extra.

### 3.1 Roadmap, capacidad y forecast

| Momento | Velocidad usada | Alcance y decision |
| --- | ---: | --- |
| Inicio | 17-18 SP proyectados | Backlog inicial de 51 SP; Sprint 1 se compromete por 16 SP |
| Cierre Sprint 1 | 16 SP | Se agregan 8 SP de HU-17/HU-18; Sprint 2 se mantiene en 15 SP |
| Cierre Sprint 2 | 15 SP | Sprint 3 se limita a 16 SP y se traslada administracion/estadisticas |
| Cierre Sprint 3 | 16 SP | Se completa el Release Goal revisado |

La capacidad de referencia fue de cinco roles por cuatro horas efectivas por Sprint. Es un supuesto academico explicitado para hacer reproducible el calculo, no un presupuesto ni una medicion de productividad individual. La estimacion de costo resultante es USD 600, con rango de USD 480 a 720 por la incertidumbre de disponibilidad, cambios y privacidad.

### 3.2 Politica de cambios urgentes

1. El Product Owner registra el pedido como Issue con origen y urgencia.
2. El equipo analiza valor, riesgo, dependencia, esfuerzo, privacidad y efecto sobre el Sprint Goal.
3. Si el pedido altera el objetivo o excede la capacidad, se refina y prioriza para un Sprint futuro.
4. Si es una obligacion de seguridad, se negocia alcance; un interesado no agrega trabajo directamente al equipo.
5. La decision queda enlazada desde Issue, backlog, Review y Pull Request.

## 4. Personas, comunicacion y acuerdos

El caso define Product Owner, Scrum Master, liderazgo tecnico, backend, interfaz, QA/seguridad y DevOps. En el equipo real Samuel Fernandez aporto las Unidades 2, 3, 4 y 8 y la integracion; Diana Duarte aporto las Unidades 5, 6, 7 y 9, incluidos riesgos, calidad y metricas.

GitHub Issues y Project son la fuente de estado; los Pull Requests registran la revision; la mensajeria se usa para coordinacion diaria y las decisiones se trasladan a Issues o documentacion. Se establecieron Planning, Daily, Refinamiento, Review y Retrospectiva con salidas verificables. Los acuerdos prohiben iniciar trabajo cuando se alcanza WIP y usar horas extra para absorber alcance nuevo.

### 4.1 Roles del caso y responsabilidades

| Rol | Responsabilidad principal | Rinde cuentas en |
| --- | --- | --- |
| Product Owner | Vision, prioridad, criterios de aceptacion y aceptacion del incremento | Planning, refinamiento y Review |
| Scrum Master | Facilitar eventos, remover impedimentos y proteger el Sprint Goal | Retrospectiva |
| Lider tecnico | Arquitectura, base de datos, rendimiento y revision tecnica | Daily y Pull Request |
| Backend | FastAPI, autenticacion, autorizacion e integraciones | Daily y Pull Request |
| Interfaz | Plantillas, responsividad y accesibilidad | Daily y Pull Request |
| QA y seguridad | Estrategia de pruebas, regresion y defectos; puede bloquear el pase a Hecha | Review y Retrospectiva |
| DevOps | Workflow, ambientes y metricas | Review |

### 4.2 Ceremonias y comunicacion

| Evento o canal | Cadencia | Salida verificable |
| --- | --- | --- |
| Sprint Planning | Dia 1, 2 horas | Sprint Goal, backlog seleccionado y capacidad |
| Daily Scrum | Diaria, 15 minutos | Impedimentos registrados en el tablero |
| Refinamiento | Mitad del Sprint, 1 hora | Historias que cumplen DoR |
| Sprint Review | Ultimo dia, 1 hora | Incremento demostrado y backlog actualizado |
| Retrospectiva | Despues de Review, 1 hora | Una o dos acciones con responsable y metrica |
| GitHub Issues y Project | Actualizacion por cambio de estado | Fuente unica de estado del trabajo |
| Pull Requests | Por cada integracion | Observaciones, aprobacion y checks registrados |

## 5. Riesgos y privacidad

Los riesgos se califican como Probabilidad x Impacto. Los principales son: rendimiento de estadisticas, dependencia de mapas, carga maliciosa de archivos, ambiguedad de anonimato, disponibilidad limitada del Product Owner, accesibilidad, exceso de alcance, capacidad reducida y autorizacion incompleta.

Los controles relevantes para esta entrega son:

- Validar extension, tamano y firma binaria real de JPG, PNG y PDF.
- Servir evidencias solo por una ruta autenticada y autorizada para el reportante o administrador.
- Probar 401 sin sesion y 403 sin rol para las rutas protegidas.
- Definir anonimato sin identificador de reportante, IP ni metadatos, y geolocalizacion opcional con consentimiento y precision reducida.
- Revisar accesibilidad, foco, etiquetas y comportamiento en 360x800 y 1440x900.

La verificacion real detecto D-01: se aceptaba un script declarado como PNG; y D-02: las evidencias eran publicas. Ambos se corrigieron en el PR #26, con pruebas de regresion y cierre de las Issues #24 y #25. Los riesgos R-03 y R-11 quedan mitigados para el alcance del prototipo.

### 5.1 Registro de riesgos

| ID | Riesgo causa, evento y efecto | P x I | Respuesta y disparador |
| --- | --- | ---: | --- |
| R-01 | Consultas de estadisticas lentas desalientan su uso | 6 | Spike de indices y paginacion; consulta mayor a 2 s con 1.000 incidentes |
| R-02 | Cuota o latencia de mapas deja reportes sin ubicacion | 4 | Spike con alternativa manual; errores de mapa superiores a 5 % |
| R-03 | Archivo malicioso compromete servidor o usuario | 6 | Validar firma real y tamano; archivo malicioso pasa la prueba |
| R-04 | Ambiguedad de anonimato expone al reportante | 4 | Minimizar datos; una prueba encuentra dato identificatorio |
| R-05 | PO disponible solo dos dias bloquea historias | 6 | Registro de supuestos; bloqueo mayor a un dia |
| R-06 | Interfaz inaccesible o defectuosa en dispositivos diversos | 4 | Checklist WCAG; defecto en Review o prueba manual |
| R-07 | Alcance Sprint 3 excede velocidad y deja historias incompletas | 6 | Reordenar por velocidad; backlog mayor a media mas 10 % |
| R-08 | SQLite/FastAPI se degrada ante picos de uso | 3 | Aceptar con contingencia; p95 mayor a 3 s o error 5xx |
| R-09 | Examenes reducen capacidad y retrasan historias | 4 | Declarar capacidad; menos de 80 % de lo planificado |
| R-10 | Autorizacion incompleta permite cambios ajenos | 3 | Pruebas 401/403; una ruta protegida falla |
| R-11 | Evidencias publicas exponen datos del reportante | 6 | Ruta con sesion y autorizacion; archivo accesible sin sesion |

### 5.2 Respuesta a los defectos reales

| Defecto | Evidencia inicial | Correccion aplicada | Regresion verificada |
| --- | --- | --- | --- |
| D-01 / Issue #24 | Un script declarado PNG era aceptado | Extension compatible y firma PNG, JPEG o PDF obligatoria | El archivo disfrazado se rechaza y no crea incidente |
| D-02 / Issue #25 | `/evidencias/` permitia descarga publica | Se retiro `StaticFiles`; nueva ruta verifica sesion y propietario/administrador | Ruta publica 404, sin sesion 401, ajeno 403 y administrador 200 |

## 6. Calidad y DevSecOps

El pipeline `CI-CD TP5` se ejecuta en Pull Requests y en `main`. Instala dependencias, ejecuta `unittest`, exige cobertura minima de 80 % sobre `aplicacion.py`, ejecuta `pip-audit` y publica el prototipo como artefacto solo si el trabajo de calidad es exitoso.

La ejecucion final en `main` posterior al merge del PR #26 fue exitosa. Se obtuvieron 2 pruebas en verde, 85 % de cobertura de `aplicacion.py` y ninguna vulnerabilidad conocida en dependencias segun `pip-audit`. Las regresiones comprueban que un archivo con contenido falso es rechazado, que la antigua ruta publica devuelve 404, que una evidencia sin sesion devuelve 401, que un usuario ajeno recibe 403 y que un administrador autorizado puede acceder.

Se registra como deuda tecnica la clave por defecto del prototipo, la ausencia de CodeQL, la falta de prueba de carga y los hallazgos de accesibilidad A-01 y A-02. Estas mejoras pertenecen a una iteracion posterior y no se presentan como resueltas.

### 6.1 Atributos de calidad priorizados

| Caracteristica ISO/IEC 25010 | Criterio y evidencia |
| --- | --- |
| Adecuacion funcional | El flujo reportar, resolver y valorar tiene prueba de integracion |
| Seguridad | Sesion, roles, contenido real de archivo y evidencia autorizada; `pip-audit` sin vulnerabilidades conocidas |
| Capacidad de interaccion | Etiquetas, teclado, foco y contraste se revisan contra WCAG 2.2 AA |
| Fiabilidad | El reporte puede usar referencia manual si no hay geolocalizacion |
| Mantenibilidad | Cobertura de `aplicacion.py` mayor o igual a 80 % y deuda registrada |
| Eficiencia de desempeno | Meta p95 menor a 2 s; prueba de carga registrada como deuda DT-04 |

### 6.2 Estrategia de pruebas y resultados reales

| Nivel | Verificacion | Resultado final |
| --- | --- | --- |
| Integracion | Reportar, resolver y valorar con `unittest` y `TestClient` | 2 pruebas en verde |
| Autorizacion | Sin sesion 401; sin rol 403; evidencia restringida | Cubierto por regresion de PR #26 |
| Entradas | Campos, estados, valoracion, extension, tamano y firma de evidencia | Firma y extension cubiertas; bordes restantes como D-03 |
| Dependencias | `pip-audit` en workflow | Sin vulnerabilidades conocidas |
| Accesibilidad | Revision manual WCAG 2.2 AA | A-01 y A-02 siguen registrados para iteracion posterior |
| Regresion | Prueba nueva por defecto corregido | Aplicada a D-01 y D-02 |

### 6.3 Calidad, defectos y deuda tecnica

| Medicion real despues de PR #26 | Valor | Meta o decision |
| --- | ---: | --- |
| Pruebas automatizadas | 2 en verde | Mantener y ampliar caminos de error |
| Cobertura de `aplicacion.py` | 85 % | Cumple minimo de 80 % bloqueado por CI |
| Defectos altos abiertos D-01/D-02 | 0 | Cerrados por Issues #24 y #25 |
| Auditoria de dependencias | 0 vulnerabilidades conocidas | Ejecutar en cada PR y push a main |

| Deuda | Origen | Accion futura |
| --- | --- | --- |
| DT-01 | `SECRET_KEY` por defecto si falta variable de entorno | Exigir configuracion por ambiente |
| DT-03 | CodeQL no habilitado | Incorporar analisis estatico |
| DT-04 | No hay prueba de carga | Medir p95 con datos de prueba |
| A-01/A-02 | Etiqueta de estado y anuncio de mensajes | Corregir accesibilidad de plantillas |

## 7. Seguimiento y mejora

Las retrospectivas simuladas produjeron acciones concretas: reducir WIP de pruebas, registrar supuestos funcionales, validar cambios del workflow en PR y preparar las metricas antes de la Review. La simulacion muestra una reduccion del cycle time de 4,6 a 2,9 dias y de defectos escapados de 2 a 0. Estas metricas se usan para mejorar el proceso, no para comparar ni presionar personas.

La matriz de trazabilidad vincula historias, riesgos, Issues, ramas, Pull Requests, workflow y tag. La version de entrega es `tp5-v1.0.0`, publicada sobre el commit de `main` que contiene la correccion de evidencias.

### 7.1 Reviews, retrospectivas y mejora

| Sprint | Review e incremento | Hallazgo de retrospectiva | Accion y comprobacion |
| --- | --- | --- | --- |
| 1 | Registro, inicio de sesion, reporte con evidencia y consulta propia | Dos historias llegaron juntas a pruebas; cycle time 4,6 dias | WIP de pruebas baja a 1 y se crea registro de supuestos; en S2 cycle time 3,4 dias |
| 2 | Bandeja de gestion, estado, asignacion, prioridad e historial | Cambio de workflow dejo CI rojo durante 18 min; supuesto funcional errado | Probar workflow en PR y validar supuestos en dos dias; en S3 restauracion 12 min y sin rehacer trabajo |
| 3 | Avisos, valoracion, anonimato y ubicacion consentida en el caso planificado | Metricas armadas tarde y poco tiempo exploratorio | Plantilla fija y prueba exploratoria desde dia 9; se verifica en siguiente release |

### 7.2 Tablero de metricas agiles y DevOps

| Metrica | S1 | S2 | S3 | Uso de gestion |
| --- | ---: | ---: | ---: | --- |
| Velocidad, SP hechos | 16 | 15 | 16 | Forecast de Release 2 con 15-16 SP |
| Lead time, dias | 8,0 | 7,2 | 6,4 | Refinar antes si supera 8 dias |
| Cycle time, dias | 4,6 | 3,4 | 2,9 | Revisar WIP y bloqueos si supera 4 dias |
| WIP maximo | 3 | 2 | 2 | No iniciar trabajo nuevo por encima del limite |
| Defectos escapados | 2 | 1 | 0 | Agregar regresion y revisar DoD si supera 1 |
| Fallo de cambios | 0 % | 20 % | 0 % | Analizar en retrospectiva si supera 15 % |
| Tiempo de restauracion | - | 18 min | 12 min | Actuar si supera 30 min |

Estas cifras representan la simulacion academica de tres Sprints y se mantienen separadas de las mediciones reales de cobertura, defectos, auditoria y CI del prototipo.

### 7.3 Trazabilidad de la entrega

| Cadena | Evidencia |
| --- | --- |
| Historia y riesgo | Product Backlog, criterios, registro de riesgos y matriz de trazabilidad |
| Trabajo tecnico | Issue #24 o #25, rama `fix/tp5-evidencias-seguras`, commits `cf797b9` y `55077d8` |
| Revision e integracion | PR #26 fusionado a `main` |
| Verificacion automatizada | Workflow `CI-CD TP5` exitoso, con pruebas, cobertura y `pip-audit` |
| Version de entrega | Tag remoto `tp5-v1.0.0` |

## 8. Anexo A - Casos de prueba criticos

Los siguientes casos convierten los criterios de seguridad, privacidad y autorizacion en verificaciones reproducibles. Los casos HU-17 y HU-18 se especifican para el alcance planificado: el prototipo actual aun no implementa esos modulos, por lo que no se presentan como pruebas ejecutadas.

| ID | Historia o riesgo | Escenario | Resultado esperado | Estado |
| --- | --- | --- | --- | --- |
| CP-04-01 | HU-04 / R-03 | Subir JPG, PNG o PDF con extension y firma validas | Se asocia la evidencia al incidente | Automatizado |
| CP-04-02 | HU-04 / R-03 | Subir script declarado como `image/png` | Se rechaza y no se crea incidente | Automatizado en PR #26 |
| CP-04-03 | HU-04 / R-11 | Pedir evidencia sin sesion, como usuario ajeno y como administrador | 401, 403 y 200 respectivamente | Automatizado en PR #26 |
| CP-10-01 | R-10 | Crear incidente sin sesion | Respuesta 401 | Verificado durante QA; ampliacion pendiente D-03 |
| CP-10-02 | R-10 | Abrir administracion como estudiante | Respuesta 403 | Verificado durante QA; ampliacion pendiente D-03 |
| CP-12-01 | HU-12 | Valorar incidente no resuelto | No permite valoracion | Cubierto por flujo del prototipo |
| CP-17-01 | HU-17 / R-04 | Crear reporte con modo anonimo | No guarda id de reportante, IP ni metadata | Especificado para Sprint 3 |
| CP-17-02 | HU-17 / R-04 | Responsable abre reporte anonimo | Ve Anonimo sin identidad del reportante | Especificado para Sprint 3 |
| CP-18-01 | HU-18 / R-02 | Negar permiso de ubicacion | El reporte se crea con referencia manual | Especificado para Sprint 3 |
| CP-18-03 | HU-18 / R-02 | Servicio de mapas no responde | Se puede reportar sin coordenadas | Especificado para Sprint 3 |

## 9. Anexo B - Matriz de entregables y evidencia

| Entregable solicitado | Evidencia en el repositorio | Verificacion |
| --- | --- | --- |
| Product Backlog, historias y criterios | `docs/tp5/02-enfoque-y-backlog.md` | 16 historias priorizadas, Story Points, dependencias y criterios resumidos |
| DoR, DoD, roadmap y planes | `docs/tp5/02-enfoque-y-backlog.md` y `03-planificacion-y-estimacion.md` | Politicas, tres Sprint Goals, capacidad y forecast |
| Tablero Scrum/Kanban y WIP | Product de GitHub y politicas documentadas | Limites para Preparada, Desarrollo y Pruebas; politica de terminar antes de empezar |
| Reviews y retrospectivas | `docs/09-seguimiento-mejora.md` | Tres ciclos simulados con hallazgo, accion, responsable y comprobacion |
| Incremento y prototipo | `prototype_campus/` | Aplicacion FastAPI demostrable, cuentas ficticias y pruebas automatizadas |
| CI/CD y DevSecOps | `.github/workflows/ci-cd.yml` | `unittest`, cobertura minima, `pip-audit` y artefacto de workflow |
| Riesgos y calidad | `docs/tp5/06-riesgos.md` y `docs/07-calidad.md` | Registro con P x I, respuestas, defectos, ISO/IEC 25010 y deuda |
| Metricas agiles y DevOps | `docs/09-seguimiento-mejora.md` | Velocidad, lead/cycle time, WIP, defectos, fallo de cambios y restauracion |
| Trazabilidad y version | `docs/trazabilidad-tp5.md`, PR, Issues, Actions y tag | Relacion Issue -> rama -> PR -> workflow -> tag |

## 10. Anexo C - Ejecucion y reproduccion local

El prototipo usa datos y cuentas ficticias. Puede ejecutarse localmente sin exponer informacion personal:

```powershell
python -m pip install -r prototype_campus/requirements.txt
python -m unittest prototype_campus/prueba_aplicacion.py
python -m uvicorn aplicacion:app --app-dir prototype_campus --reload
```

La aplicacion queda disponible en `http://127.0.0.1:8000`. Las cuentas demostrativas son `estudiante / campus2026`, `funcionario / campus2026` y `admin / AdminCampus2026`. Los adjuntos, bases locales y secretos estan excluidos del control de versiones.

## 11. Evidencia final y limitaciones

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

## 12. Conclusiones

La entrega aplica un enfoque agil trazable a un caso de incidentes del campus. El backlog, los limites WIP, las decisiones de cambio, los riesgos y la calidad se conectan con evidencia verificable en GitHub. La correccion de las vulnerabilidades de evidencias muestra el ciclo completo de detectar, registrar, corregir, probar y entregar con CI. El tag `tp5-v1.0.0` identifica el estado final validado del repositorio.
