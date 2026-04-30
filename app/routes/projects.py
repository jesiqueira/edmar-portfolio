import json
import os
from flask import Blueprint, render_template

projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/")
def projects():

    # Caminho absoluto para o arquivo JSON
    json_path = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")

    # Abrir e carregar o JSON
    with open(json_path, "r", encoding="utf-8") as f:
        projects = json.load(f)

    return render_template("projects.html", projects=projects)
