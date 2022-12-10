from django import template
from product.models import Category

register = template.Library()

@register.inclusion_tag('inc/header.html')
def caregory_navbar():
        categories = Category.objects.filter(is_navbar=True)
        return {'categories':categories}