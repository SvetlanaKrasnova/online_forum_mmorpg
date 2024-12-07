from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post


# Create your views here.
class Profile(LoginRequiredMixin, ListView):
    """
    Страница профиля (личный кабинет)
    """
    model = Post
    ordering = '-create_date'
    template_name = 'profile.html'
    context_object_name = 'reactions'