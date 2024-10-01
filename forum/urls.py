from django.urls import path
from forum.views import login, forget_password, register


urlpatterns = [
    path('forum/', login),
    path('forum/forget_password', forget_password),
    path('forum/register', register)
]