from flask import Blueprint, g

from src.public.index import serve_index
from src.public.page import serve_page

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def index() -> str:
    return serve_index(g.appwrite)

@public_bp.route("/page/<slug>")
def page(slug) -> str:
    return serve_page(g.config, g.appwrite, slug)
