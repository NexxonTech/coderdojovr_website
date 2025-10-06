from django.shortcuts import render
from wagtail.admin.auth import permission_required


from ...tito_api import TiToAPI


@permission_required("wagtailadmin.coderdojo_portal_access_tito_events")
def list_events(request):
    events = TiToAPI.get().get_events()

    return render(request, "admin/list_events.html", {
        "breadcrumbs_items": [{ "label": "Eventi", "url": "/admin/eventbrite" }],
        "events": events
    })
