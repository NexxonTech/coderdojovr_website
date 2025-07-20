from appwrite.client import Client
from appwrite.query import Query
from appwrite.services.databases import Databases
from datetime import datetime, timezone, time
from flask import render_template


def serve_index(client: Client) -> str:
    databases = Databases(client)

    today = datetime.combine(
        datetime.now(timezone.utc).date(),
        time.min,
        timezone.utc
    )
    date_records = databases.list_documents("coderdojo_portal", "dates", [
        Query.order_asc("date")
    ])["documents"]
    next_dates = [
        { "date": date, "indicator": "success animate-pulse" if date == today else "warning" }
        for date_record in date_records
        if (date := datetime.fromisoformat(date_record["date"])) >= today
    ]
    past_dates = [
        { "date": date, "indicator": "error" }
        for date_record in date_records
        if (date := datetime.fromisoformat(date_record["date"])) < today
    ]

    return render_template("pages/index.html", today=today, next_dates=next_dates, past_dates=past_dates)
