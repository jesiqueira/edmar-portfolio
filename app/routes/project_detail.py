import json
import os
from flask import Blueprint, render_template, abort

project_detail_bp = Blueprint("project_detail", __name__, url_prefix="/projects")

# Carrega o JSON uma vez
json_path = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")
with open(json_path, "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)


def slugify(text):
    return (
        text.lower()
        .replace("–", "-")
        .replace("—", "-")
        .replace(" ", "-")
        .replace("/", "-")
        .replace(".", "")
        .replace(",", "")
    )


@project_detail_bp.route("/<slug>")
def project_detail(slug):
    # Procura o projeto pelo slug
    for project in PROJECTS:
        if slugify(project["title"]) == slug:
            return render_template("project_detail.html", project=project)

    return abort(404)
