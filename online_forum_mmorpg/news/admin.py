from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News


# Register your models here.
class NewsAdmin(SummernoteModelAdmin):
    model = News
    summernote_fields = ('text',)
    list_display = ['title', 'author_id', 'create_date', 'author']
    list_filter = ('title', 'author_id', 'create_date', 'text', 'author')
    search_fields = ('title', 'author_id', 'create_date', 'text', 'author')


# Register your models here.
admin.site.register(News, NewsAdmin)
