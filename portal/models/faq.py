import uuid

from django.db import models
from django.db.models.fields import TextField
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import InlinePanel, FieldPanel
from wagtail.fields import RichTextField

from wagtail.models import Page, Orderable


class FAQ(Page):
    parent_page_types = [ 'portal.HomePage' ]
    subpage_types = []

    content_panels = Page.content_panels + [
        InlinePanel("questions", label="Domanda", heading="Domande della FAQ")
    ]


class FAQQuestion(Orderable):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    page = ParentalKey(FAQ, on_delete=models.CASCADE, related_name="questions")
    title = TextField()
    body = RichTextField()
    panels = [ FieldPanel("title"), FieldPanel("body") ]