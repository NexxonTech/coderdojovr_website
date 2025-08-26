from django import template
from wagtail.models import Site

from ..eventbrite_api import EventbriteAPI


register = template.Library()


@register.simple_tag
def get_next_event():
    return EventbriteAPI.get().get_next_event()
