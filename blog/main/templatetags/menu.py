from django import template
from page.models import Page
register = template.Library()

@register.inclusion_tag("main/menu.html")
def menu():
    out = {}
    pages = Page.objects.all()
    out['pages'] = pages
    return out
