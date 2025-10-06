from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.admin.models import Admin

from .tito.list_events import list_events
from .tito.show_event import show_event


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('tito', list_events, name='tito_list_events'),
        path('tito/<event_slug>', show_event, name='tito_show_event'),
    ]


@hooks.register('register_admin_menu_item')
def register_event_menu_item():
    return MenuItem('Eventi', reverse('tito_list_events'), "eventi", icon_name='date')

@hooks.register('register_admin_menu_item')
def register_manual_menu_item():
    return MenuItem('Manuale', "https://github.com/NexxonTech/coderdojovr_website/wiki", "manuale", icon_name='doc-full-inverse', order = 10000)

@hooks.register('construct_main_menu')
def check_menu_permissions(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'help']
    if not request.user.has_perm('wagtailadmin.coderdojo_portal_access_tito_events'):
        menu_items[:] = [item for item in menu_items if item.name != 'eventi']


@hooks.register('register_permissions')
def register_custom_permissions():
    content_type = ContentType.objects.get_for_model(Admin)
    Permission.objects.get_or_create(
        content_type=content_type,
        codename='coderdojo_portal_access_tito_events',
        name='Can access TiTo events'
    )

    return Permission.objects.filter(codename__startswith='coderdojo_portal')
