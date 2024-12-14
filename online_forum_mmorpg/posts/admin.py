from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    model = Post
    summernote_fields = ('description',)
    list_display = ["title", "create_date", "description", "category", "author"]
    list_filter = ('title', 'create_date', 'description', 'category', 'author')
    search_fields = ('title', 'create_date', 'description', 'category', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)
