from django import template
from django.urls import resolve
from menu.models import Menu, MenuItem
from menu.utils import build_tree

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    items = MenuItem.objects.filter(menu=menu).select_related('parent')
    tree = build_tree(items, current_url)
    return {'menu_tree': tree}
