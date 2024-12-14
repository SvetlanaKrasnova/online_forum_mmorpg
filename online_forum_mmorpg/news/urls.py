from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('', NewsList.as_view(), name='news_portal'),
    path('search_news/', NewsList.as_view(), name='search_news'),
    path('<int:pk>', NewsDetail.as_view(), name='detail_news'),
]
