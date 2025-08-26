from django.shortcuts import render
from wagtail.admin.auth import permission_required


from ...eventbrite_api import EventbriteAPI


@permission_required("wagtailadmin.coderdojo_portal_access_eventbrite_events")
def show_event(request, event_id):
    event = EventbriteAPI.get().get_event_by_id(event_id)
    if event:
        event["attendees"] = EventbriteAPI.get().get_attendees_by_event(event)

    return render(request, "admin/show_event.html", {
        "breadcrumbs_items": [
            { "label": "Eventi", "url": "/admin/eventbrite" },
            {
                "label": event.get("name", {}).get("text", "Error") if event else "Error",
                "url": f"/admin/eventbrite/{event_id}"
            }
        ],
        "event": event
    })
