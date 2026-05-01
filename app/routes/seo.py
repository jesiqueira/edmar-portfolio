from flask import Blueprint, send_from_directory
import os

seo = Blueprint("seo", __name__)


@seo.route("/robots.txt")
def robots():
    return send_from_directory(os.path.join(os.getcwd(), "app/static"), "robots.txt")


@seo.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.join(os.getcwd(), "app/static"), "sitemap.xml")
