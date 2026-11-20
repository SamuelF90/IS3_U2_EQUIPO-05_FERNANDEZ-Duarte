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
            connection.execute("DELETE FROM incidentes WHERE titulo = ?", ("Luz apagada en Aula 3",))

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


if __name__ == "__main__":
    unittest.main()
