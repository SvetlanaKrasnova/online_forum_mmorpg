from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    summernote_fields = ('description',)
    list_display = ['user', 'user_id', 'avatar',]
    list_filter = ('user',)
    search_fields = ('user__first_name', 'user__last_name',)


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
