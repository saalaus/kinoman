from django import template
from films.models import Film

register = template.Library()

@register.inclusion_tag('films/card.html')
def show_card(film: Film):
    return {'film': film}
