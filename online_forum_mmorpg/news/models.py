from django.db import models
from django.core.cache import cache
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    """
    Новость
    """
    title = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('detail_news', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'news-{self.pk}')
