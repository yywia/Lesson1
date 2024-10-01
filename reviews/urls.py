from django.urls import path
from reviews.views import text_reviews, celebrity_review, tripadvisor_score


urlpatterns = [
    path('reviews/', text_reviews),
    path('reviews/celebrity', celebrity_review),
    path('reviews/tripadvisor', tripadvisor_score)
]