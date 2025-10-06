from django import template
from wagtail.models import Site

from ..tito_api import TiToAPI


register = template.Library()


@register.simple_tag
def get_next_event():
    next_event = TiToAPI.get().get_next_event()
    if next_event:
        next_event["account"] = TiToAPI.get().account
    return next_event
