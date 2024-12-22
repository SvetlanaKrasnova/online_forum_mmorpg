from django.core.cache import cache
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm, ReplyForm
from .filters import PostFilter
from django.urls import reverse_lazy


# Create your views here.
class PostList(LoginRequiredMixin, ListView):
    """
    Показывает все объявления
    """
    model = Post
    ordering = '-create_date'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Переопределяем функцию получения списка публикаций
        :return:
        """
        queryset = super().get_queryset()
        self.filter_posts = PostFilter(self.request.GET, queryset)
        return self.filter_posts.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_posts'] = self.filter_posts
        return context


class PostEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """
    Редактирование объявления
    """
    permission_required = ('posts.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    """
    Создание объявления
    """
    permission_required = ('posts.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.author = self.request.user
        object.save()
        return redirect('/sign/profile')


class PostDetail(LoginRequiredMixin, DetailView):
    """
    Детальная информация по 1 объявлению
    """
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'
    pk_url_kwarg = "pk"

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = self.request.user
            reply.save()
        return redirect('detail_post', pk=post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


class PostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """
    Удаление публикации
    """
    permission_required = ('posts.delete_post',)
    model = Post
    success_url = reverse_lazy('profile')
