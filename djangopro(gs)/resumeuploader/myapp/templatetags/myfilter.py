# 14 Custom Filter - ['Lahore', 'Pasror']
from django import template
register = template.Library()

@register.filter(name='remove_special')
def remove_chars(value, args):
    # print(args)
    # print('value: ', value)
    for character in args:
        # print(character)
        value = value.replace(character, "")
    return value