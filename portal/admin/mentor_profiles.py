from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from ..models import MentorProfile


@register_snippet
class MentorProfileAdmin(SnippetViewSet):
    model = MentorProfile
    menu_label = "Profili Mentor"
    add_to_admin_menu = True
    icon = "user"
    list_display = [ "display_name", "user" ]
    exclude_form_fields = [ "id" ]
