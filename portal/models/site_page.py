from django.db.models.fields import TextField
from wagtail.fields import RichTextField
from wagtail.models import Page


class SitePage(Page):
    description = TextField(blank=True)
    body = RichTextField()
    content_panels = Page.content_panels + [ "description", "body" ]
