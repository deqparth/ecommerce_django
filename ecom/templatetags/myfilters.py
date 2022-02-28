"""module to add css class"""
from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    """returns the class name and pipes to call"""

    return value.as_widget(attrs={'class': arg})
