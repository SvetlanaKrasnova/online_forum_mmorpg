import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_forum_mmorpg.settings')

app = Celery('online_forum_mmorpg')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'notify_week_news_every_monday_8am': {
        'task': 'news.tasks.notify_week_posts',
        'schedule': crontab(hour='8', minute='0', day_of_week='monday'),
    },
    'clear_task_redis_every_2_hour': {
        'task': 'news.tasks.clear_task_redis',
        'schedule': crontab(hour='*/2'),
    }
}

app.autodiscover_tasks()
