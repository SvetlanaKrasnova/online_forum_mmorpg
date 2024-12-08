from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    """
    Объявление
    """
    CATEGORIES = [
        ('tank', "Танки"),
        ("hilt", "Хилы"),
        ("dd", "ДД"),
        ("traders", 'Торговцы'),
        ("guild_master", 'Гилдмастеры'),
        ("questgiver", 'Квестгиверы'),
        ("blacksmith", 'Кузнецы'),
        ("tanner", 'Кожевники'),
        ("potion_maker", 'Зельевары'),
        ("spellmaster", 'Мастера заклинаний'),
    ]
    title = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.CharField(max_length=35,
                                choices=CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Reply(models.Model):
    """
    Отклик к объявлению
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # К какому объявлению оставлен отклик
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто написал
    text = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)