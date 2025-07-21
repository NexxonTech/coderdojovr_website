import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.db.models.fields import TextField
from wagtail.fields import RichTextField
from wagtail.models import Page


class ChiSiamo(Page):
    parent_page_types = [ 'portal.HomePage' ]
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        profiles = MentorProfile.objects.select_related('user').all()
        context['mentors'] = profiles
        return context


class MentorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    display_name = TextField()
    bio = RichTextField()
    avatar = ImageField(upload_to='avatars/')