from django import template
from app.models import ParentCategory, ChildCategory, Cart

register = template.Library()
@register.simple_tag
def parent_category():
    parent_category = ParentCategory.objects.all()
    return parent_category

@register.simple_tag
def child_category():
    child_category = ChildCategory.objects.all()
    return child_category

# @register.simple_tag
# def category():
#     # context = ParentCategory.objects.all()
#     context = ChildCategory.objects.all()
#     return context

# 11
@register.simple_tag
def total_cart(user):
    cart = Cart.objects.filter(user=user)
    total_cart = len(cart)
    return total_cart