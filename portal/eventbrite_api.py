from django.conf import settings
import requests
from requests.models import Response

class EventbriteAPI:
    BASE_URL = "https://www.eventbriteapi.com/v3/"
    INSTANCE = None

    @classmethod
    def get(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = EventbriteAPI(settings.EVENTBRITE_TOKEN, settings.EVENTBRITE_ORGID)
        return cls.INSTANCE

    def __init__(self, token: str, org_id: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": f"coderdojovr_portal/{settings.PROJECT_VERSION} (+https://www.coderdojovr.it)"
        }
        self.org_id = org_id

    def try_request(self, url, params) -> Response:
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response

    def get_events(self) -> list[dict]:
        url = f"{self.BASE_URL}organizations/{self.org_id}/events/"
        params = {
            "order_by": "start_desc"
        }
        response = self.try_request(url, params)
        return response.json().get("events", [])

    def get_event_by_id(self, event_id: str) -> dict | None:
        url = f"{self.BASE_URL}events/{event_id}/"
        response = self.try_request(url, {})
        return response.json()

    def get_next_event(self) -> dict | None:
        url = f"{self.BASE_URL}organizations/{self.org_id}/events/"
        params = {
            "order_by": "start_desc",
            "status": "live",
            "page_size": 1
        }
        response = self.try_request(url, params)
        events = response.json().get("events", [])
        return events[0] if events else None

    def get_attendees_by_event(self, event: dict) -> list[dict]:
        url = f"{self.BASE_URL}events/{event['id']}/attendees/"
        params = {
            "status": "attending"
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()

        attendees = response.json().get("attendees", [])
        attendees.sort(key=lambda att: att.get("profile", {}).get("name", "").strip().lower())
        return attendees
