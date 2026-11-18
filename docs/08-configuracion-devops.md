# Unidad 8 - Configuración, CI/CD y DevSecOps

## Estrategia de configuración

| Elemento | Acuerdo |
| --- | --- |
| Ramas | `feature/<issue>-descripcion`, `fix/<issue>-descripcion` y `docs/<issue>-descripcion`. Son breves y se integran solo mediante Pull Request. |
| Pull Request | Incluye Issue enlazada, criterios de aceptación, pruebas ejecutadas y una aprobación cruzada. No se permite autoaprobación. |
| Protección de `main` | Requiere PR, conversaciones resueltas y el check `quality` exitoso. |
| Versionado | SemVer: `v0.1.0` para el incremento inicial; `MINOR` para capacidad compatible y `PATCH` para corrección. |
| Trazabilidad | Issue -> rama -> PR -> commit -> workflow -> tag/release -> artefacto o despliegue. |
| Datos sensibles | No se versionan base de datos, adjuntos, claves, IP ni información personal; `.gitignore` excluye datos locales y evidencias. |

## Ambientes

| Ambiente | Propósito | Datos | Evidencia |
| --- | --- | --- | --- |
| Local | Desarrollo y prueba del prototipo. | Cuentas y base SQLite ficticias. | `python -m unittest prototype_campus/prueba_aplicacion.py`. |
| CI | Verificación repetible de cada PR. | Base temporal de prueba. | Workflow `CI-CD TP5`. |
| Pruebas | Demostración de Sprint Review. | Datos ficticios o anonimizados. | Artefacto descargable del workflow. |
| Producción | Fuera de alcance del TP. | Requeriría aprobación y evaluación adicional de privacidad. | No se despliega. |

## Pipeline CI/CD

`.github/workflows/ci-cd.yml` se ejecuta en Pull Requests y cambios a `main`:

1. Obtiene el código con permisos mínimos de solo lectura.
2. Configura Python 3.12 e instala las dependencias del prototipo.
3. Ejecuta la prueba del flujo completo: estudiante reporta, administrador resuelve y estudiante valora.
4. Ejecuta CodeQL para análisis estático de Python.
5. Publica el prototipo validado como artefacto descargable únicamente si calidad fue exitosa.

El workflow no usa `pull_request_target` ni secretos de forks. El job de calidad no cuenta con permisos de despliegue; por eso un cambio no puede publicar por sí mismo fuera del ambiente de pruebas.

## Ejecución local

```powershell
python -m pip install -r prototype_campus/requirements.txt
python -m unittest prototype_campus/prueba_aplicacion.py
python -m uvicorn aplicacion:app --app-dir prototype_campus --reload
```

Abrir `http://127.0.0.1:8000`. Las cuentas son ficticias: `estudiante / campus2026`, `funcionario / campus2026` y `admin / AdminCampus2026`.
