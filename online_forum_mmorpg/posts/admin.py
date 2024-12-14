from django.contrib import admin
from .models import Post, Reply
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    model = Post
    summernote_fields = ('description',)
    list_display = ["title", "create_date", "description", "category", "author"]
    list_filter = ('title', 'create_date', 'description', 'category', 'author')
    search_fields = ('title', 'create_date', 'description', 'category', 'author')


class ReplyAdmin(admin.ModelAdmin):
    model = Reply
    search_fields = ('create_date', 'text', 'status', 'user')
    list_display = ('create_date', 'text', 'status', 'user')
    list_filter = ('create_date', 'text', 'status', 'user')


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
