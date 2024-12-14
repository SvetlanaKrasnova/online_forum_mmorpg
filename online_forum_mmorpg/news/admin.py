from django.contrib import admin
from .models import News
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class NewsAdmin(SummernoteModelAdmin):
    model = News
    summernote_fields = ('text',)
    list_display = ["title", "create_date", "text", "author"]
    list_filter = ('title', 'create_date', 'text', 'author')
    search_fields = ('title', 'create_date', 'text', 'author')


# Register your models here.
admin.site.register(News, NewsAdmin)
