from datetime import datetime, timedelta
from celery import shared_task
from news.models import News
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def sent_email_task(message: dict):
    msg = EmailMultiAlternatives(
        subject=message["subject"],
        body="",
        from_email=message["from_email"],
        to=message["to"],
    )
    msg.attach_alternative(message["html_content"], "text/html")
    msg.send()


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

    msg_html = render_to_string('notify_week_news_mail.html', {
        'link_home': settings.SITE_URL,
        'link_filter': f'{settings.SITE_URL}/news/search_news/?title=&create_date__gt={start_date.strftime("%Y-%m-%d")}',
        'news': news,
    })

    for email in users_emails:
        sent_email_task.apply_async([{
            "subject": "Новости за неделю",
            "html_content": msg_html,
            "from_email": settings.DEFAULT_FROM_EMAIL,
            "to": [email]

        }], countdown=1)
