from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post, Reply
from posts.filters import ReplyFilter


# Create your views here.
class Profile(LoginRequiredMixin, ListView):
    """
    Страница профиля (личный кабинет)
    """
    model = Reply
    ordering = '-create_date'
    template_name = 'profile.html'
    context_object_name = 'replies'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(user=self.request.user)
        # q = self.request.GET.copy()
        # if q.get('type') == "my_reactions":
        #     q['type'] = ""
        # print('q', q)
        self.filter_replys = ReplyFilter(self.request.GET, queryset)  # TODO
        return self.filter_replys.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_replys'] = self.filter_replys
        context['col_my_reply'] = Reply.objects.filter(
            post__author=self.request.user).count  # Количество откликов пользователя
        context['col_my_posts'] = Post.objects.filter(
            author=self.request.user).count  # Количество объявлений пользователя
        context['col_active_posts'] = 0  # TODO Количество не принятых объявлений пользователя
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
