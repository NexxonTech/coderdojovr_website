from appwrite.client import Client
from appwrite.exception import AppwriteException
from appwrite.id import ID
from appwrite.input_file import InputFile
from appwrite.query import Query
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from flask import Blueprint, g, render_template, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.datastructures import FileStorage

from src.admin.auth import User

admin_bp = Blueprint("admin", __name__)


def upload_propic(appwrite: Client, file: FileStorage):
    storage = Storage(appwrite)
    return storage.create_file(
        "coderdojo_portal", ID.unique(),
        InputFile.from_bytes(file.stream.read(), file.name)
    )

@admin_bp.get("/")
@login_required
def admin():
    return redirect("/admin/profile")

@admin_bp.route("/profile", methods = ["GET", "POST"])
@login_required
def mentor_profile():
    databases = Databases(g.appwrite)

    mentor_records = databases.list_documents("coderdojo_portal", "mentors", [
        Query.equal("account", current_user.id)
    ])["documents"]
    mentor_record = mentor_records[0] if len(mentor_records) > 0 else None

    error = False
    if request.method == "POST":
        try:
            if mentor_record:
                mentor_record = databases.update_document("coderdojo_portal", "mentors", mentor_record["$id"], {
                    "bio": request.form.get("bio") if request.form.get("bio") else mentor_record["bio"],
                    "avatar": upload_propic(g.appwrite, request.files.get("propic"))["$id"] if request.files.get("propic") else mentor_record["avatar"]
                })
            else:
                mentor_record = databases.create_document("coderdojo_portal", "mentors", ID.unique(), {
                    "fullname": current_user.name,
                    "bio": request.form.get("bio") if request.form.get("bio") else None,
                    "avatar": upload_propic(g.appwrite, request.files.get("propic"))["$id"] if request.files.get("propic") else None,
                    "account": current_user.id
                })
        except AppwriteException as e:
            error = True

    return render_template("pages/admin/mentor_profile.html", auth=current_user, profile=mentor_record, error=error)

@admin_bp.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("pages/admin/login.html", error=False)
    else:
        try:
            login_user(User.try_login(g.appwrite, request.form.get("email"), request.form.get("password")))
            if target := request.args.get("next"):
                return redirect(target)
            return redirect("/admin")
        except AppwriteException:
            return render_template("pages/admin/login.html", error=True)

@admin_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/admin")