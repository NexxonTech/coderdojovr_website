from appwrite.query import Query
from appwrite.services.databases import Databases
from appwrite.services.users import Users
from flask import Flask, g
from flask_login import LoginManager

from src.admin import admin_bp, User
from src.appwrite_client import AppwriteClient
from src.config import Config
from src.public import public_bp


app = Flask(__name__, static_folder="../static", template_folder="../template")
app.secret_key = Config.get()["secret_key"]
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/admin/login"

app.register_blueprint(public_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")


@app.before_request
def load_context():
    AppwriteClient.load()
    Config.load()


@login_manager.user_loader
def user_loader(userid):
    return User.try_recover(g.appwrite, userid)


@app.context_processor
def inject_utilities():
    AppwriteClient.load()

    databases = Databases(g.appwrite)

    def get_menu():
        page_records = databases.list_documents("coderdojo_portal", "pages", [
            Query.select(["title", "slug"]),
            Query.equal("show_menu", True),
        ])["documents"]
        return page_records

    return dict(get_menu=get_menu)