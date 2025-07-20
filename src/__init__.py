from appwrite.client import Client
from appwrite.query import Query
from appwrite.services.databases import Databases
from flask import Flask
import os

from src.config import Config
from src.index import serve_index
from src.page import serve_page

config = Config.get()

client = Client()
app = Flask(__name__, static_folder="../static", template_folder="../template")


@app.route("/")
def index() -> str:
    return serve_index(client)

@app.route("/page/<slug>")
def page(slug) -> str:
    return serve_page(config, client, slug)


@app.context_processor
def inject_utilities():
    databases = Databases(client)

    def get_menu():
        page_records = databases.list_documents("coderdojo_portal", "pages", [
            Query.select(["title", "slug"]),
            Query.equal("show_menu", True),
        ])["documents"]
        return page_records

    return dict(get_menu=get_menu)


with app.app_context():
    appwrite_conf = config["appwrite"]

    client.set_endpoint(appwrite_conf["endpoint"]).set_project(appwrite_conf["project"]).set_key(appwrite_conf["key"])