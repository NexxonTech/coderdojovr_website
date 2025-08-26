from django.shortcuts import render
from wagtail.admin.auth import permission_required


from ...eventbrite_api import EventbriteAPI


@permission_required("wagtailadmin.coderdojo_portal_access_eventbrite_events")
def list_events(request):
    events = EventbriteAPI.get().get_events()

    return render(request, "admin/list_events.html", {
        "breadcrumbs_items": [{ "label": "Eventi", "url": "/admin/eventbrite" }],
        "events": events
    })
