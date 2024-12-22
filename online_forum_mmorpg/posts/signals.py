from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reply
from online_forum_mmorpg.utils.notification_text import *

@receiver(post_save, sender=Reply)
def notification_reply(sender, instance, created, **kwargs):
    if created:
        message = get_message_by_created_reply(instance)
    elif instance.status == "approved":
        message = get_message_by_approved_reply(instance)
    else:
        return
    send_email_notification(message)
