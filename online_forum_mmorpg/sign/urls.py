from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/reactions/search/', ProfileView.as_view(), name='reactions_search'),
]
