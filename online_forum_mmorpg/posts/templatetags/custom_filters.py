from django import template
from django.utils.safestring import mark_safe
from posts.models import STATUSES_REPLY
from online_forum_mmorpg.utils.parser_html import strip_tags

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


@register.filter()
def convert_status_reply(status):
    for el in STATUSES_REPLY:
        if el[0] == status:
            return el[1]
    return status


@register.filter()
def filter_from_tags(text_html):
    return strip_tags(text_html)
