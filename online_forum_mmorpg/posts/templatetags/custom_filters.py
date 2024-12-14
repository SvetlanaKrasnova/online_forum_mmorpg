
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def get_nike(user_email):
    return user_email.split("@")[0]

@register.filter()
def get_title(current_url, is_html: bool = False):
    if is_html:
        return mark_safe('<em>О</em>бъявления' if 'post' in current_url else '<em>Н</em>овости')
    else:
        return 'Объявления' if 'post' in current_url else 'Новости'
