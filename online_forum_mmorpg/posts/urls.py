from django.urls import path
from .views import PostList, PostCreate, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='posts_portal'),
    path('create_post/', PostCreate.as_view(), name='create_post'),
    path('search_posts/', PostList.as_view(), name='search_posts'),
    path('<int:pk>', PostDetail.as_view(), name='detail_post'),
]
