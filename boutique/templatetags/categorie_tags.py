from django import template
from boutique.models import Categorie

register = template.Library()

@register.inclusion_tag('boutique/categories.html', takes_context=True)
def categories(context):
    return {
        'categories': Categorie.objects.all(),
        'request': context['request'],
    }