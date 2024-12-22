from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUSES_REPLY = [
    ('approved', "Принят"),
    ("rejected", "Отклонен"),
    ("new", "Новый"),
]

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

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.id)])


class Reply(models.Model):
    """
    Отклик к объявлению
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=35,
                              choices=STATUSES_REPLY,
                              default="new")

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.post.pk})
