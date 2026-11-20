"""Prueba del flujo: estudiante reporta, administrador resuelve y estudiante valora."""

import os
from pathlib import Path
import sys
import tempfile
import unittest

os.environ["CAMPUS_DB_PATH"] = str(Path(tempfile.gettempdir()) / "campus-incidentes-prueba.db")
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi.testclient import TestClient
from aplicacion import app, database


class IncidentFlowTest(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        with database() as connection:
            connection.execute(
                "DELETE FROM incidentes WHERE titulo IN (?, ?, ?)",
                ("Luz apagada en Aula 3", "Archivo disfrazado", "Evidencia protegida"),
            )

    def sign_in(self, username: str, password: str = "campus2026") -> None:
        response = self.client.post(
            "/iniciar-sesion",
            data={"nombre_usuario": username, "contrasena": password},
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)

    def test_incident_is_managed_and_rated(self):
        self.sign_in("estudiante")
        response = self.client.post(
            "/incidentes",
            data={
                "titulo": "Luz apagada en Aula 3",
                "categoria": "Iluminación",
                "descripcion": "La luminaria no enciende durante la clase.",
                "ubicacion": "Edificio A - Aula 3",
            },
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)

        with database() as connection:
            incident = connection.execute(
                "SELECT id, estado FROM incidentes WHERE titulo = ?", ("Luz apagada en Aula 3",)
            ).fetchone()
        self.assertEqual(incident["estado"], "Abierto")

        self.sign_in("admin", "AdminCampus2026")
        self.assertEqual(self.client.get("/administracion").status_code, 200)
        response = self.client.post(
            f"/administracion/incidentes/{incident['id']}/estado",
            data={"nuevo_estado": "Resuelto"},
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)

        self.sign_in("estudiante")
        response = self.client.post(
            f"/incidentes/{incident['id']}/valoracion",
            data={"valoracion": "5"},
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)
        with database() as connection:
            updated = connection.execute(
                "SELECT estado, valoracion FROM incidentes WHERE id = ?", (incident["id"],)
            ).fetchone()
        self.assertEqual(updated["estado"], "Resuelto")
        self.assertEqual(updated["valoracion"], 5)

    def test_evidence_validates_content_and_requires_authorization(self):
        self.assertEqual(
            self.client.post(
                "/incidentes",
                data={
                    "titulo": "Sin sesión",
                    "categoria": "Seguridad",
                    "descripcion": "No debe crearse.",
                    "ubicacion": "Edificio A",
                },
                follow_redirects=False,
            ).status_code,
            401,
        )
        self.sign_in("estudiante")
        malicious = self.client.post(
            "/incidentes",
            data={
                "titulo": "Archivo disfrazado",
                "categoria": "Seguridad",
                "descripcion": "No debe aceptarse.",
                "ubicacion": "Edificio A",
            },
            files={"evidencia": ("script.png", b"#!/bin/sh\necho vulnerable", "image/png")},
            follow_redirects=False,
        )
        self.assertEqual(malicious.status_code, 303)
        with database() as connection:
            rejected = connection.execute(
                "SELECT id FROM incidentes WHERE titulo = ?", ("Archivo disfrazado",)
            ).fetchone()
        self.assertIsNone(rejected)

        valid_png = b"\x89PNG\r\n\x1a\ncontenido-de-prueba"
        uploaded = self.client.post(
            "/incidentes",
            data={
                "titulo": "Evidencia protegida",
                "categoria": "Infraestructura",
                "descripcion": "La evidencia requiere autorización.",
                "ubicacion": "Edificio B",
            },
            files={"evidencia": ("evidencia.png", valid_png, "image/png")},
            follow_redirects=False,
        )
        self.assertEqual(uploaded.status_code, 303)
        with database() as connection:
            incident = connection.execute(
                "SELECT id, archivo_evidencia FROM incidentes WHERE titulo = ?", ("Evidencia protegida",)
            ).fetchone()

        self.client.post("/cerrar-sesion", follow_redirects=False)
        self.assertEqual(self.client.get(f"/evidencias/{incident['archivo_evidencia']}").status_code, 404)
        self.assertEqual(self.client.get(f"/incidentes/{incident['id']}/evidencia").status_code, 401)

        self.sign_in("funcionario")
        self.assertEqual(self.client.get("/administracion").status_code, 403)
        self.assertEqual(self.client.get(f"/incidentes/{incident['id']}/evidencia").status_code, 403)

        self.sign_in("admin", "AdminCampus2026")
        evidence = self.client.get(f"/incidentes/{incident['id']}/evidencia")
        self.assertEqual(evidence.status_code, 200)
        self.assertEqual(evidence.content, valid_png)


if __name__ == "__main__":
    unittest.main()
