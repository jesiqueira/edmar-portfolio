import json
import os

# Caminho absoluto para o JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "projects.json")

# Carrega o JSON
with open(JSON_PATH, "r", encoding="utf-8") as f:
    PROJECTS = json.load(f)


# Adiciona slug automaticamente
def slugify(title):
    return (
        title.lower()
        .replace(" ", "-")
        .replace("–", "")
        .replace("—", "")
        .replace("/", "-")
        .replace(".", "")
    )
