from django import forms
from django.contrib.auth import get_user_model
from wagtail import hooks
from wagtail.admin.views.account import BaseSettingsPanel, SettingsTab
from wagtail.permission_policies import OwnershipPermissionPolicy
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .forms import OwnMentorProfileForm
from .models import MentorProfile


@register_snippet
class MentorProfileAdmin(SnippetViewSet):
    model = MentorProfile
    menu_label = "Profili Mentor"
    add_to_admin_menu = True
    icon = "user"
    list_display = [ "display_name", "user" ]
    exclude_form_fields = [ "id" ]


public_profile_tab = SettingsTab('public_profile_tab', "Profilo Pubblico", order=300)


@hooks.register('register_account_settings_panel')
class CustomSettingsPanel(BaseSettingsPanel):
    name = 'public_profile'
    title = "Profilo Pubblico"
    tab = public_profile_tab
    order = 0
    form_class = OwnMentorProfileForm
    form_object = 'user'
