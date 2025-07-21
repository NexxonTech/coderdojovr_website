import uuid
from datetime import date

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import InlinePanel, FieldPanel

from wagtail.models import Page, Orderable


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel("event_dates", label="Data Evento", heading="Eventi Programmati")
    ]

    def past_event_dates(self):
        dates = list(self.event_dates.filter(date__lt=date.today()))
        return dates

    def future_event_dates(self):
        dates = list(self.event_dates.filter(date__gte=date.today()))
        return dates


class EventDate(Orderable):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="event_dates")
    date = models.DateField()
    panels = [ FieldPanel("date") ]

    def get_indicator(self):
        if self.date == date.today():
            return "success animate-pulse"
        elif self.date > date.today():
            return "warning"
        else:
            return "error"