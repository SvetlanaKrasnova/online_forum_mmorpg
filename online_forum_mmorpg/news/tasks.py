import redis
import logging
import json
from datetime import datetime, timedelta
from celery import shared_task
from news.models import News
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from online_forum_mmorpg.utils import send_email_notification

logger = logging.getLogger(__name__)


@shared_task
def send_email_task(message: dict):
    send_email_notification(message)


@shared_task
def notify_week_posts() -> None:
    """
    Задача на рассылку новостей за неделю подписчикам
    :return:
    """
    start_date = datetime.now() - timedelta(days=7)
    news = News.objects.filter(create_date__gte=start_date)
    users_emails = User.objects.filter(groups__name='postsletter').values('email')

    if not news:
        return

    msg_html = render_to_string('news/notify_week_news_mail.html', {
        'link_home': settings.SITE_URL,
        'link_filter': f'{settings.SITE_URL}/news/search_news/?title=&create_date__gt={start_date.strftime("%Y-%m-%d")}',
        'news': news,
    })

    for email in users_emails:
        send_email_task.apply_async([{
            "subject": "Новости за неделю",
            "html_content": msg_html,
            "to": [email]
        }], countdown=1)
