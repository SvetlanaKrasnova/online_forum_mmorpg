from django.shortcuts import redirect

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post, Reply
from posts.filters import ReplyFilter
from posts.forms import ReplyChengeStatusForm


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
        self.filter_replys = ReplyFilter(self.request.GET, queryset.filter(post__author=self.request.user))  # TODO
        return self.filter_replys.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_replys'] = self.filter_replys
        context['form_chenge_status_reply'] = ReplyChengeStatusForm()

        # Количество откликов пользователя
        context['col_my_reply'] = Reply.objects.filter(user=self.request.user).count

        # Количество объявлений пользователя
        my_posts = Post.objects.filter(author=self.request.user)
        context['col_my_posts'] = my_posts.count
        context['col_active_posts'] = Reply.objects.filter(status='new', post__author=self.request.user).count

        context['my_posts'] = my_posts
        return context

    def post(self, request, *args, **kwargs):
        status = request.POST.get("status_reply")
        id_reply = request.POST.get("id_reply")
        if status == 'remove':
            Reply.objects.get(id=id_reply).delete()
        elif status == 'default':
            pass
        else:
            r = Reply.objects.get(id=id_reply)
            r.status = status
            r.save()

        return redirect('profile')


class MainPage(ListView):
    """
    Главная страница портала
    """
    model = Post
    template_name = 'main_page.html'
    context_object_name = 'news'
