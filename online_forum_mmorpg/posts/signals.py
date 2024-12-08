from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reply
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Reply)
def notification_new_reply(sender, instance, created, **kwargs):
    if created:
        send_mail(subject=f'Новый отклик {datetime.now().strftime("%d-%m-%Y %H:%M")}',
                  message=f"""
                     Получен новый отклик на ваше объявление "{instance.post.title}" от {instance.post.create_date.strftime("%d-%m-%Y %H:%M")}
                     """,
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[instance.post.author.email])
