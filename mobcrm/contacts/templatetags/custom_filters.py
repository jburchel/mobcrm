from django import template
from django.db.models import Model

register = template.Library()

@register.filter
def object_to_dict(obj):
    if isinstance(obj, Model):
        return {field.name: getattr(obj, field.name) for field in obj._meta.fields}
    return {}