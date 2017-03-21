"""
    VMTools Class

    Author  : Niyazi Elvan
    Date    : 16.03.2017
    Updates :
"""

from django import template
register = template.Library()

@register.filter
def to_GB(value):
    return float(value)/1024.0/1024.0/1024.0 