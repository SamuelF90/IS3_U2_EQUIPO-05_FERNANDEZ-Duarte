# Unidad 6 - Gestión de riesgos

> **Caso: incidentes del campus** · TP 5 Enfoque Ágil · Issue #20 · Responsable: Diana Duarte · Estructura según
> el Anexo B de la guía. La evolución por Sprint es **simulación académica**, salvo la sección 6.5, que registra
> una verificación real sobre el prototipo.

## 6.1. Escala y método

- **Probabilidad (P)** e **Impacto (I)**: 1 = bajo, 2 = medio, 3 = alto.
- **Prioridad = P × I** → **Crítica** 6-9 · **Alta** 4 · **Media** 2-3 · **Baja** 1.
- Cada riesgo se redacta como *causa → evento → efecto*. Los riesgos activos o que requieren trabajo técnico se
  registran como Issues con etiqueta `risk`; los demás se controlan en este registro. Todos se revisan en cada
  Sprint Review (estado) y en cada Retrospectiva (acciones).
- Issues `risk` existentes al 20/11/2026: [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24) (D-01, R-03) y [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25) (D-02, R-11).
- Los responsables son los roles definidos en la [Unidad 5](05-personas-y-comunicacion.md#51-roles-y-responsabilidades).

## 6.2. Identificación y análisis

| ID | Categoría | Causa → evento → efecto | P | I | Prioridad | Respuesta |
| --- | --- | --- | ---: | ---: | --- | --- |
| R-01 | Técnico | Por poca experiencia en optimizar consultas SQL, las estadísticas (HU-13) podrían responder lento con muchos incidentes y desalentar su uso por mantenimiento. | 2 | 3 | 6 Crítica | Mitigar |
| R-02 | Técnico / proveedor | Por cuotas y latencia del servicio externo de mapas, la geolocalización (HU-18) podría fallar y dejar reportes sin ubicación. | 2 | 2 | 4 Alta | Mitigar |
| R-03 | Seguridad | Por una validación débil de la evidencia (HU-04), podrían subirse archivos maliciosos y comprometer el servidor o a quien los abra. | 2 | 3 | 6 Crítica | Evitar |
| R-04 | Requisitos / privacidad | Por ambigüedad sobre qué significa "anónimo" (HU-17), podrían guardarse datos que identifiquen al reportante y provocar desconfianza o exposición. | 2 | 2 | 4 Alta | Mitigar |
| R-05 | Personas | Por la disponibilidad del PO de dos días por semana, las dudas funcionales podrían bloquear historias en pleno Sprint. | 3 | 2 | 6 Crítica | Mitigar |
| R-06 | Calidad / usabilidad | Por la variedad de dispositivos y navegadores del campus, la interfaz podría verse mal o ser inaccesible en pantallas pequeñas o con teclado. | 2 | 2 | 4 Alta | Mitigar |
| R-07 | Alcance | Por la carga inicial del Sprint 3 (21 SP frente a 17-18 SP proyectados) y el cambio posterior al Sprint 1, podrían quedar historias sin terminar en la Release 1. | 3 | 2 | 6 Crítica | Mitigar |
| R-08 | Técnico | Por no tener pruebas de carga, la aplicación FastAPI con SQLite podría degradarse en picos de uso (inicio de semestre) y quedar no disponible. | 1 | 3 | 3 Media | Aceptar + contingencia |
| R-09 | Organizacional | Por exámenes y entregas académicas simultáneas, podría bajar la capacidad efectiva del Sprint y retrasar historias. | 2 | 2 | 4 Alta | Mitigar |
| R-10 | Seguridad | Por un control de acceso incompleto, un usuario sin permisos podría usar funciones de administración y modificar incidentes ajenos. | 1 | 3 | 3 Media | Evitar |
| R-11 | Seguridad / privacidad | Por servir las evidencias como archivos públicos, cualquiera con el enlace podría ver fotos o documentos del reportante y exponer datos personales. *Identificado en la verificación de calidad (6.5).* | 2 | 3 | 6 Crítica | Evitar |

## 6.3. Respuesta, disparador y contingencia

| ID | Acción preventiva y artefacto donde se refleja | Responsable | Identificado / revisión | Disparador | Contingencia |
| --- | --- | --- | --- | --- | --- |
| R-01 | **Spike** de 4 h en el Sprint 2 sobre índices y paginación antes de construir HU-13. | Dev 1 | Planning S1 / cada Review | Consulta de estadísticas > 2 s con 1.000 incidentes de prueba. | Estadísticas precalculadas una vez por día. |
| R-02 | **Spike** en el Sprint 2 con Leaflet/OpenStreetMap; **criterio de aceptación** de HU-18: ubicación opcional y referencia manual. | Dev 2 | Review S1 / cada Review | Más del 5 % de errores de mapa en pruebas o aviso de cuota al 80 %. | Desactivar el mapa y usar solo la referencia manual (campo `ubicacion`). |
| R-03 | **Criterio de aceptación** de HU-04: JPG, PNG o PDF, máximo 5 MB, validación del **contenido real** del archivo y no solo del tipo declarado. | Dev 4 | Planning S1 / cada Review | Una prueba con un archivo malicioso pasa la validación. | Desactivar la carga de evidencias y aislar los archivos sospechosos. |
| R-04 | **Criterio de aceptación** de HU-17: no guarda `id_reportante`, IP ni metadatos del dispositivo; informa los límites del anonimato. Revisión de privacidad en la DoD. | Product Owner | Review S1 / cada Review | Una prueba encuentra un dato identificatorio en un reporte anónimo. | Ocultar el modo anónimo hasta corregirlo y eliminar los datos guardados de más. |
| R-05 | **Registro de supuestos funcionales** y canal asincrónico (acción de la Retrospectiva 1). | SM | Planning S1 / cada Retro | Una historia bloqueada más de 1 día por una consulta al PO. | El SM escala al PO; el equipo toma la siguiente historia Preparada. |
| R-06 | **DoD**: probar en 360×800 y 1440×900, con teclado, foco visible y contraste. | Dev 3 | Planning S1 / cada Review | Defecto de interfaz encontrado en la Review o reportado por usuarios. | Corrección prioritaria con la capacidad reservada para calidad. |
| R-07 | **Reordenar el backlog** en la Planning 3 con la velocidad observada, no la deseada. | Product Owner | Planning S1 / cada Planning | Sprint Backlog mayor que la velocidad media + 10 %. | Pasar a la Release 2 las historias de menor valor (HU-13, HU-14, HU-15). |
| R-08 | Aceptado: el piloto tiene poco volumen. La prueba de carga queda como **deuda técnica** DT-04. | Dev 1 | Planning S1 / cada Review | p95 > 3 s o errores 5xx en el ambiente de pruebas. | Limitar pedidos por usuario y avisar en el canal de interesados. |
| R-09 | **Capacidad explícita** en cada Planning (20 horas-equipo por Sprint, Unidad 4), descontando exámenes. | SM | Planning S1 / cada Planning | Capacidad declarada < 80 % de la planificada. | Reducir el alcance con el PO, sin horas extra. |
| R-10 | **DoD**: cada ruta protegida tiene una prueba que confirma 401 sin sesión y 403 sin rol. | Dev 2 | Planning S1 / cada Review | Una prueba de autorización falla. | Bloquear el merge y desactivar la ruta en pruebas. |
| R-11 | **Historia técnica**: servir evidencias por una ruta que verifique sesión y que sea el reportante o un responsable. | Dev 2 | Verificación de calidad 20/11/2026 / próxima Review | Evidencia accesible sin sesión (prueba CP-04-03 en rojo). | Desactivar el enlace a evidencias hasta corregirlo. |

## 6.4. Seguimiento por Sprint (simulación)

**Residual** = prioridad después de la respuesta. **Secundario** = riesgo nuevo que puede crear la respuesta.

| ID | Inicio | Tras S1 | Tras S2 | Tras S3 | Estado | Evidencia de revisión | Riesgo secundario |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| R-01 | 6 | 6 | 2 (P2×I1) | Release 2 | **Transferido** | Spike S2 con índices y paginación; HU-13 pasa a la Release 2 (R-07). | Estadísticas con hasta 1 día de atraso. |
| R-02 | 4 | 4 | 2 (P1×I2) | 2 | Mitigado | Spike S2; HU-18 con ubicación opcional y referencia manual. | Referencia manual imprecisa. |
| R-03 | 6 | 3 (P1×I3) | 3 | 3 | **Reabierto** en el prototipo | Simulación: validación entregada en S1. Verificación real: defecto D-01, [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24) (6.5). | Rechazo de archivos legítimos (por ejemplo, HEIC). |
| R-04 | 4 | 4 | 4 | 2 (P1×I2) | Mitigado en el diseño | Criterios de HU-17 refinados; casos de prueba CP-17 especificados ([Unidad 7](../07-calidad.md#75-casos-de-prueba-de-privacidad-hu-17-y-hu-18)). | Reportes anónimos falsos → moderación en la Release 2. |
| R-05 | 6 | 6 | 2 (P1×I2) | 2 | Mitigado | Registro de supuestos: ninguna historia bloqueada más de 1 día en S2 y S3. | Supuestos equivocados que haya que rehacer (1 en S2). |
| R-06 | 4 | 4 | 2 (P1×I2) | 2 | Mitigado | Checklist de resoluciones en la DoD; hallazgos A-01 y A-02 registrados. | — |
| R-07 | 6 | 6 | 6 | 2 (P1×I2) | Mitigado | Planning 3 en 16 SP = velocidad observada; HU-13, 14 y 15 pasan a la Release 2. | Expectativa de administración postergada, comunicada en la Review 2. |
| R-08 | 3 | 3 | 3 | 3 | Aceptado | Sin picos en pruebas; DT-04 registrada. | — |
| R-09 | 4 | 4 | 4 | 4 | **Activo** | S2 con 85 % de capacidad por parciales, absorbida sin horas extra. | — |
| R-10 | 3 | 3 | 1 (P1×I1) | 1 | Mitigado | Verificación real: 401 y 403 correctos (6.5); falta prueba automatizada (D-03). | — |
| R-11 | — | — | — | 6 | **Abierto** | Detectado el 20/11/2026: D-02, [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25). | — |

**Riesgos reducidos por entrega temprana:** R-03 se pudo **probar** con el primer incremento, en vez de estimarlo
en abstracto (y justamente esa prueba real lo reabrió en el prototipo). R-05 se redujo porque el proceso se corrigió
después de la primera Retrospectiva. R-02 bajó porque el spike se hizo antes de construir HU-18.

## 6.5. Verificación real sobre el prototipo

Verificación de Diana Duarte del 20/11/2026 sobre `prototype_campus/` de la rama `feature/tp5-planificacion-devops`
(commit `1f91b7b`), con `fastapi.testclient`:

| Riesgo | Prueba | Resultado | Acción |
| --- | --- | --- | --- |
| R-10 | `POST /incidentes` sin sesión | **401** ✔ | Agregar como prueba automatizada (D-03). |
| R-10 | `GET /administracion` con rol estudiante | **403** ✔ | Agregar como prueba automatizada (D-03). |
| R-03 | Subir un script `.sh` declarado como `image/png` | **Aceptado y guardado** ✘ | Defecto D-01 → [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24): validar la firma real del archivo. |
| R-11 | `GET /evidencias/<archivo>` sin sesión | **200, archivo descargado** ✘ | Defecto D-02 → [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25) y nuevo riesgo R-11. |

**Cierre técnico:** D-01 y D-02 se corrigen en el [PR #26](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/pull/26), con pruebas de regresión, y **bloquean el tag `tp5-v1.0.0`** hasta que se apruebe, se fusione y se cierren [#24](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/24) y [#25](https://github.com/SamuelF90/IS3_U2_EQUIPO-05_FERNANDEZ-Duarte/issues/25). R-03 y R-11 pasan a *Mitigado* después de ese cierre.

> **Correcciones respecto del borrador .docx:** las prioridades se recalcularon con P × I (por ejemplo, R-03 con
> P = 1 e I = 3 es 3, Media, no 2, Baja). R-01 ya no dice que HU-13 se desarrolló en el Sprint 3, porque pasa a la
> Release 2. Las referencias a Flutter, Node/Express y PostgreSQL se reemplazaron por el stack real del prototipo
> (FastAPI y SQLite).
