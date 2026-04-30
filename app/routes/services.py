from flask import Blueprint, render_template

services_bp = Blueprint("services", __name__, url_prefix="/services")


@services_bp.route("/")
def services():
    return render_template("services.html")
