"""
Convert bytes to GB in templates
"""
from django import template
register = template.Library()

@register.filter
def to_GB(value):
    return float(value)/1024.0/1024.0/1024.0 