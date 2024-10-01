from django.urls import path
from news.views import recent_news, search_news, hot_news


urlpatterns = [
    path('news/', recent_news),
    path('news/search', search_news),
    path('news/hot', hot_news)
]