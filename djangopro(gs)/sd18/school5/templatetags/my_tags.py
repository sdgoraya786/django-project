from django import template

register = template.Library()
# for get model name m2
@register.filter()
def get_model_name(value):
    return value.__class__.__name__
