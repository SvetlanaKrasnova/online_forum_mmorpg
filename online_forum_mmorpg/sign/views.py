from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.filters import PostFilter


# Create your views here.
class Profile(LoginRequiredMixin, ListView):
    """
    Страница профиля (личный кабинет)
    """
    model = Post
    ordering = '-create_date'
    template_name = 'profile.html'
    context_object_name = 'reactions'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.GET)
        q = self.request.GET.copy()
        if q.get('type') == "my_reactions":
            q['type'] = ""
        print(q)
        self.filter_posts = PostFilter(q, queryset)  # TODO
        return self.filter_posts.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_tasks'] = self.filter_posts
        context['nike'] = f"@{self.request.user.email.split('@')[0]}"

        context['col_my_reply'] = 0 # TODO Количество откликов пользователя
        context['col_my_posts'] = 0 # TODO Количество объявлений пользователя
        context['col_active_posts'] = 0 # TODO Количество не принятых объявлений пользователя
        return context

class MainPage(ListView):
    """
    Главная страница портала
    """
    model = Post
    template_name = 'main_page.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        print('request.user:', self.request.user.is_authenticated)
        print('request.path:', self.request.path)
