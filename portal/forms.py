from django import forms

from .models import MentorProfile


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