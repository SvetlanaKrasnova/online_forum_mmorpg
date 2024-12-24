import logging
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Users postsletter'

    def handle(self, *args, **options):
        """
        Команда для получения списка пользователей, которым отправляется рассылка новостей
        :param args:
        :param options:
        :return:
        """
        users_emails = User.objects.filter(groups__name='postsletter').values('email')
        print(''.join(users_emails))
