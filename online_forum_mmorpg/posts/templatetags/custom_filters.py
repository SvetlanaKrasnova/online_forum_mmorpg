
from django import template

register = template.Library()

@register.filter()
def get_nike(user_email):
    return user_email.split("@")[0]
