from django.core.cache import cache
from django.views.generic import ListView, DetailView
from .models import News
from .filters import NewsFilter


# Create your views here.
class NewsList(ListView):
    """
    Страница с новостями
    """
    model = News
    ordering = '-create_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter_posts = NewsFilter(self.request.GET, queryset)
        return self.filter_posts.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_posts'] = self.filter_posts
        return context


class NewsDetail(DetailView):
    """
    Детальная информация по 1 новости
    """
    model = News
    template_name = 'detail_post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'news-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'news-{self.kwargs["pk"]}', obj)
        return obj
