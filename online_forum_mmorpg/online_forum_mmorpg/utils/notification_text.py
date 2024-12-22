from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from posts.models import Reply
from django.template.loader import render_to_string
from datetime import datetime


def send_email_notification(message: dict):
    msg = EmailMultiAlternatives(
        subject=message["subject"],
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=message["to"],
    )
    msg.attach_alternative(message["html_content"], "text/html")
    msg.send()


def get_message_by_created_reply(reply: Reply) -> dict:
    html_content = render_to_string('sign/notify_reply.html', {
        'post_title': reply.post.title,
        'date_post': reply.post.create_date.strftime("%d-%m-%Y %H:%M"),
        'update_reply': False
    })

    return {
        'subject': f'Новый отклик {datetime.now().strftime("%d-%m-%Y %H:%M")}',
        'to': [reply.post.author.email],
        'html_content': html_content,
    }


def get_message_by_approved_reply(reply: Reply) -> dict:
    html_content = render_to_string('sign/notify_reply.html', {
        'recipient_reply': f'{reply.post.author.first_name} {reply.post.author.last_name}',
        'date_reply': reply.create_date.strftime("%d.%m.%Y %H:%M"),
        'text_reply': reply.text,
        'update_reply': True,
    })

    return {
        'subject': 'Ваш отклик принят!',
        'to': [reply.user.email],
        'html_content': html_content,
    }
