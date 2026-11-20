"""Prototipo demostrable de reporte y seguimiento de incidentes del campus."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import os
import sqlite3
from urllib.parse import quote
from uuid import uuid4

import jwt
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile, status
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = Path(os.environ.get("CAMPUS_DB_PATH", BASE_DIR / "datos" / "campus.db"))
EVIDENCE_DIR = BASE_DIR / "evidencias"
SECRET_KEY = os.environ.get("CAMPUS_SECRET_KEY", "solo-demostracion-local-no-produccion")
ALGORITHM = "HS256"
ALLOWED_EVIDENCE_TYPES = {"image/jpeg", "image/png", "application/pdf"}
EVIDENCE_EXTENSIONS = {
    "image/jpeg": {".jpg", ".jpeg"},
    "image/png": {".png"},
    "application/pdf": {".pdf"},
}
EVIDENCE_SIGNATURES = {
    "image/jpeg": (b"\xff\xd8\xff",),
    "image/png": (b"\x89PNG\r\n\x1a\n",),
    "application/pdf": (b"%PDF-",),
}
VALID_STATUSES = {"Abierto", "En proceso", "Resuelto"}

password_hash = PasswordHash.recommended()
app = FastAPI(title="Incidentes del campus", docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory=BASE_DIR / "templates")

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


def database() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """Creates only fictitious local accounts and a resolved incident for the demo."""
    with database() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre_usuario TEXT UNIQUE NOT NULL,
                nombre_mostrado TEXT NOT NULL,
                rol TEXT NOT NULL CHECK(rol IN ('ESTUDIANTE', 'FUNCIONARIO', 'ADMINISTRADOR')),
                hash_contrasena TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS incidentes (
                id INTEGER PRIMARY KEY,
                id_reportante INTEGER NOT NULL REFERENCES usuarios(id),
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                ubicacion TEXT NOT NULL,
                estado TEXT NOT NULL CHECK(estado IN ('Abierto', 'En proceso', 'Resuelto')),
                archivo_evidencia TEXT,
                nombre_evidencia TEXT,
                valoracion INTEGER CHECK(valoracion BETWEEN 1 AND 5),
                fecha_creacion TEXT NOT NULL
            );
            """
        )
        accounts = (
            ("estudiante", "Ana Estudiante", "ESTUDIANTE", "campus2026"),
            ("funcionario", "Luis Funcionario", "FUNCIONARIO", "campus2026"),
            ("admin", "Administración de mantenimiento", "ADMINISTRADOR", "AdminCampus2026"),
        )
        for username, display_name, role, password in accounts:
            existing = connection.execute(
                "SELECT id FROM usuarios WHERE nombre_usuario = ?", (username,)
            ).fetchone()
            if existing:
                connection.execute(
                    "UPDATE usuarios SET nombre_mostrado = ?, rol = ?, hash_contrasena = ? WHERE nombre_usuario = ?",
                    (display_name, role, password_hash.hash(password), username),
                )
            else:
                connection.execute(
                    "INSERT INTO usuarios (nombre_usuario, nombre_mostrado, rol, hash_contrasena) VALUES (?, ?, ?, ?)",
                    (username, display_name, role, password_hash.hash(password)),
                )


def create_session_token(user: sqlite3.Row) -> str:
    expiry = datetime.now(timezone.utc) + timedelta(minutes=60)
    return jwt.encode({"sub": user["nombre_usuario"], "rol": user["rol"], "exp": expiry}, SECRET_KEY, algorithm=ALGORITHM)


def current_user(request: Request) -> sqlite3.Row | None:
    token = request.cookies.get("campus_token")
    if not token:
        return None
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
    except InvalidTokenError:
        return None
    if not username:
        return None
    with database() as connection:
        return connection.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (username,)).fetchone()


def require_user(request: Request, roles: set[str]) -> sqlite3.Row:
    user = current_user(request)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inicie sesión.")
    if user["rol"] not in roles:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tiene permiso para esta acción.")
    return user


def redirect(path: str, message: str) -> RedirectResponse:
    separator = "&" if "?" in path else "?"
    return RedirectResponse(f"{path}{separator}mensaje={quote(message)}", status_code=status.HTTP_303_SEE_OTHER)


def is_valid_evidence(content: bytes, filename: str, media_type: str | None) -> bool:
    """Accepts only a supported extension whose binary signature matches its declared type."""
    if media_type not in ALLOWED_EVIDENCE_TYPES:
        return False
    suffix = Path(filename).suffix.lower()
    return suffix in EVIDENCE_EXTENSIONS[media_type] and any(
        content.startswith(signature) for signature in EVIDENCE_SIGNATURES[media_type]
    )


@app.get("/")
def home(request: Request):
    user = current_user(request)
    if user and user["rol"] == "ADMINISTRADOR":
        return RedirectResponse("/administracion", status_code=status.HTTP_303_SEE_OTHER)
    incidents: list[sqlite3.Row] = []
    if user:
        with database() as connection:
            incidents = connection.execute(
                "SELECT * FROM incidentes WHERE id_reportante = ? ORDER BY id DESC", (user["id"],)
            ).fetchall()
    return templates.TemplateResponse(request=request, name="home.html", context={"usuario": user, "incidentes": incidents})


@app.post("/iniciar-sesion")
def sign_in(request: Request, nombre_usuario: str = Form(), contrasena: str = Form()):
    with database() as connection:
        user = connection.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (nombre_usuario,)).fetchone()
    if not user or not password_hash.verify(contrasena, user["hash_contrasena"]):
        return redirect("/", "Credenciales inválidas.")
    destination = "/administracion" if user["rol"] == "ADMINISTRADOR" else "/"
    response = redirect(destination, f"Sesión iniciada como {user['nombre_mostrado']}.")
    response.set_cookie("campus_token", create_session_token(user), httponly=True, samesite="lax")
    return response


@app.post("/cerrar-sesion")
def sign_out():
    response = redirect("/", "Sesión cerrada.")
    response.delete_cookie("campus_token")
    return response


@app.post("/incidentes")
async def create_incident(
    request: Request,
    titulo: str = Form(),
    categoria: str = Form(),
    descripcion: str = Form(),
    ubicacion: str = Form(),
    evidencia: UploadFile | None = File(default=None),
):
    user = require_user(request, {"ESTUDIANTE", "FUNCIONARIO"})
    if not all(value.strip() for value in (titulo, categoria, descripcion, ubicacion)):
        return redirect("/", "Complete todos los campos del reporte.")

    evidence_file = None
    evidence_name = None
    if evidencia and evidencia.filename:
        content = await evidencia.read()
        if len(content) > 5 * 1024 * 1024:
            return redirect("/", "La evidencia no puede superar 5 MB.")
        if not is_valid_evidence(content, evidencia.filename, evidencia.content_type):
            return redirect("/", "La evidencia debe ser un JPG, PNG o PDF válido.")
        evidence_file = f"{uuid4().hex}-{Path(evidencia.filename).name}"
        evidence_name = Path(evidencia.filename).name
        (EVIDENCE_DIR / evidence_file).write_bytes(content)

    with database() as connection:
        connection.execute(
            """
            INSERT INTO incidentes
            (id_reportante, titulo, categoria, descripcion, ubicacion, estado, archivo_evidencia, nombre_evidencia, fecha_creacion)
            VALUES (?, ?, ?, ?, ?, 'Abierto', ?, ?, ?)
            """,
            (user["id"], titulo.strip(), categoria.strip(), descripcion.strip(), ubicacion.strip(), evidence_file, evidence_name, datetime.now(timezone.utc).isoformat()),
        )
    return redirect("/", "Incidente registrado con estado Abierto.")


@app.get("/incidentes/{incident_id}/evidencia")
def download_evidence(request: Request, incident_id: int):
    user = require_user(request, {"ESTUDIANTE", "FUNCIONARIO", "ADMINISTRADOR"})
    with database() as connection:
        incident = connection.execute(
            "SELECT * FROM incidentes WHERE id = ?", (incident_id,)
        ).fetchone()
    if not incident or not incident["archivo_evidencia"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evidencia no encontrada.")
    if user["rol"] != "ADMINISTRADOR" and incident["id_reportante"] != user["id"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tiene permiso para esta evidencia.")

    evidence_path = EVIDENCE_DIR / incident["archivo_evidencia"]
    if not evidence_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evidencia no encontrada.")
    return FileResponse(evidence_path, filename=incident["nombre_evidencia"])


@app.post("/incidentes/{incident_id}/valoracion")
def rate_incident(request: Request, incident_id: int, valoracion: int = Form()):
    user = require_user(request, {"ESTUDIANTE", "FUNCIONARIO"})
    if valoracion not in {1, 2, 3, 4, 5}:
        return redirect("/", "La valoración debe estar entre 1 y 5.")
    with database() as connection:
        incident = connection.execute(
            "SELECT * FROM incidentes WHERE id = ? AND id_reportante = ?", (incident_id, user["id"])
        ).fetchone()
        if not incident:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incidente no encontrado.")
        if incident["estado"] != "Resuelto":
            return redirect("/", "Solo se puede valorar un incidente resuelto.")
        connection.execute("UPDATE incidentes SET valoracion = ? WHERE id = ?", (valoracion, incident_id))
    return redirect("/", "Valoración registrada.")


@app.get("/administracion")
def administration(request: Request):
    user = require_user(request, {"ADMINISTRADOR"})
    with database() as connection:
        incidents = connection.execute(
            """
            SELECT incidentes.*, usuarios.nombre_mostrado, usuarios.rol AS rol_reportante
            FROM incidentes JOIN usuarios ON usuarios.id = incidentes.id_reportante
            ORDER BY incidentes.id DESC
            """
        ).fetchall()
    return templates.TemplateResponse(request=request, name="admin.html", context={"usuario": user, "incidentes": incidents, "estados": sorted(VALID_STATUSES)})


@app.post("/administracion/incidentes/{incident_id}/estado")
def update_status(request: Request, incident_id: int, nuevo_estado: str = Form()):
    require_user(request, {"ADMINISTRADOR"})
    if nuevo_estado not in VALID_STATUSES:
        return redirect("/administracion", "Estado no válido.")
    with database() as connection:
        result = connection.execute("UPDATE incidentes SET estado = ? WHERE id = ?", (nuevo_estado, incident_id))
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incidente no encontrado.")
    return redirect("/administracion", "Estado del incidente actualizado.")


initialize_database()
