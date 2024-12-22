from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostEdit, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='posts_portal'),
    path('create_post/', PostCreate.as_view(), name='create_post'),
    path('search_posts/', PostList.as_view(), name='search_posts'),
    path('<int:pk>', PostDetail.as_view(), name='detail_post'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='edit_post'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
]
