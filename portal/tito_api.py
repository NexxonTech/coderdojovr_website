from typing import Any, final
from django.conf import settings
import requests
from requests.models import Response

@final
class TiToAPI:
    BASE_URL = "https://api.tito.io/v3"
    instance = None

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = TiToAPI(settings.TITO_TOKEN, settings.TITO_ACCOUNT)
        return cls.instance

    def __init__(self, token: str, account: str):
        self.headers = {
            "Authorization": f"Token token={token}",
            "User-Agent": f"coderdojovr_portal/{settings.PROJECT_VERSION} (+https://www.coderdojovr.it)"
        }
        self.account = account

    def try_request(self, url: str, params: dict[str, Any]) -> Response:
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response

    def get_events(self) -> list[dict[str, Any]]:
        url = f"{self.BASE_URL}/{self.account}/events/"
        response = self.try_request(url, {})
        upcoming = response.json().get("events", [])

        url = f"{self.BASE_URL}/{self.account}/events/past"
        response = self.try_request(url, {})
        past = response.json().get("events", [])

        return upcoming + past

    def get_event_by_slug(self, event_slug: str) -> dict[str, Any] | None:
        url = f"{self.BASE_URL}/{self.account}/{event_slug}/"
        response = self.try_request(url, {})
        return response.json().get("event", {})

    def get_next_event(self) -> dict[str, Any] | None:
        url = f"{self.BASE_URL}/{self.account}/events/"
        params = {
            "page": { "size": 1 }
        }
        response = self.try_request(url, params)
        events = response.json().get("events", [])
        return events[0] if events else None

    def get_tickets_by_event(self, event: dict[str, Any]) -> list[dict[str, Any]]:
        url = f"{self.BASE_URL}/{self.account}/{event['slug']}/tickets/?search[sort]=first_name&search[states][]=complete"
        response = requests.get(url, headers=self.headers, params={})
        response.raise_for_status()

        tickets = response.json().get("tickets", [])
        for ticket in tickets:
            ticket["answers"] = self.get_answers_by_ticket(event["slug"], ticket)
        return tickets

    def get_answers_by_ticket(self, event_slug: str, ticket: dict[str, Any]) -> list[dict[str, Any]]:
        url = f"{self.BASE_URL}/{self.account}/{event_slug}/tickets/{ticket['slug']}?expand=answers"
        response = requests.get(url, headers=self.headers, params={})
        response.raise_for_status()

        return response.json().get("ticket", {}).get("answers", {})
