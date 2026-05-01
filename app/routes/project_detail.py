import json
import os
from flask import Blueprint, render_template, redirect

project_detail_bp = Blueprint("project_detail", __name__, url_prefix="/projects")

JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)


# ROTA 1 — Detalhes do projeto (sempre mostra detalhes)
@project_detail_bp.route("/<slug>")
def project_detail(slug):
    project = next((p for p in PROJECTS if p["slug"].lower() == slug.lower()), None)

    if not project:
        return render_template("404.html"), 404

    return render_template("project_detail.html", project=project)


# ROTA 2 — Botão GitHub (decide público/privado)
@project_detail_bp.route("/<slug>/github")
def project_github(slug):
    project = next((p for p in PROJECTS if p["slug"].lower() == slug.lower()), None)

    if not project:
        return render_template("404.html"), 404

    # Se for privado → página privada
    if project.get("private") is True:
        return render_template("project_private.html", project=project)

    # Se for público → redireciona para o GitHub
    if project.get("github"):
        return redirect(project["github"])

    # Se não tiver GitHub → volta para detalhes
    return redirect(f"/projects/{slug}")
