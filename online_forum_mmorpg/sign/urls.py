from django.urls import path
from .views import Profile

urlpatterns = [
    path('profile', Profile.as_view(), name='profile'),
    path('profile/reactions/search/', Profile.as_view(), name='reactions_search'),
]
