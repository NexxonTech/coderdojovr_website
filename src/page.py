from appwrite.client import Client
from appwrite.query import Query
from appwrite.services.databases import Databases
from flask import render_template, abort

IMAGE_BASE_URL = "{endpoint}/storage/buckets/{bucket}/files/{file}/view?project={project}"


def serve_chi_siamo(config: dict, client: Client) -> str:
    appwrite_conf = config["appwrite"]

    databases = Databases(client)

    mentor_records = databases.list_documents("coderdojo_portal", "mentors", [
        Query.order_asc("fullname")
    ])["documents"]
    for mentor in mentor_records:
        mentor["avatar_url"] = IMAGE_BASE_URL.format(
            endpoint=appwrite_conf["endpoint"], bucket="coderdojo_portal",
            file=mentor["avatar"], project=appwrite_conf["project"],
        )

    return render_template("pages/chi_siamo.html", mentors=mentor_records)


def serve_faqs(client: Client) -> str:
    databases = Databases(client)

    question_records = databases.list_documents("coderdojo_portal", "faqs", [
        Query.order_asc("title")
    ])["documents"]

    return render_template("pages/faqs.html", questions=question_records)


def serve_page(config: dict, client: Client, slug: str) -> str:
    if slug == "chi_siamo":
        return serve_chi_siamo(config, client)
    elif slug == "faqs":
        return serve_faqs(client)

    databases = Databases(client)
    page_records = databases.list_documents("coderdojo_portal", "pages", [
        Query.equal('slug', slug),
    ])["documents"]
    if len(page_records) > 0:
        return render_template("pages/page.html", page=page_records[0])
    abort(404)