from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(header=None, item: str = None):
    items = MenuItem.objects.filter(header__title=header)

    def get_items(item=None, submenu=None):
        menu = list(items.filter(root__title=item)) if item else list(items.filter(root=None))
        try:
            menu.insert(menu.index(submenu[0].root) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_items(items.get(title=item).root.title, menu)
        except AttributeError:
            return get_items(submenu=menu)
        except MenuItem.DoesNotExist:
            return menu

    return {'menu': get_items()} if header == item else {'menu': get_items(item)}
