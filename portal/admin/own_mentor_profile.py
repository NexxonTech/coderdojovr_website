from django import forms
from wagtail import hooks
from wagtail.admin.views.account import BaseSettingsPanel, SettingsTab
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from ..models import MentorProfile


public_profile_tab = SettingsTab('public_profile_tab', "Profilo Pubblico", order=300)


class OwnMentorProfileForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = [ "display_name", "bio", "avatar" ]
        widgets = {
            "display_name": forms.TextInput(),
        }

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.instance, _ = MentorProfile.objects.get_or_create(user=instance, defaults={"user": instance})
        for field in self.fields:
            self.fields[field].initial = getattr(self.instance, field)


@hooks.register('register_account_settings_panel')
class OwnMentorProfilePanel(BaseSettingsPanel):
    name = 'public_profile'
    title = "Profilo Pubblico"
    tab = public_profile_tab
    order = 0
    form_class = OwnMentorProfileForm
    form_object = 'user'
