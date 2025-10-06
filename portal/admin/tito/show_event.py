from django.shortcuts import render
from wagtail.admin.auth import permission_required


from ...tito_api import TiToAPI


@permission_required("wagtailadmin.coderdojo_portal_access_tito_events")
def show_event(request, event_slug: str):
    event = TiToAPI.get().get_event_by_slug(event_slug)
    if event:
        event["tickets"] = TiToAPI.get().get_tickets_by_event(event)

    return render(request, "admin/show_event.html", {
        "breadcrumbs_items": [
            { "label": "Eventi", "url": "/admin/tito" },
            {
                "label": event.get("title", "Error") if event else "Error",
                "url": f"/admin/tito/{event_slug}"
            }
        ],
        "event": event
    })
