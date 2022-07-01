
from django.urls import path, include
from .views import NewsApiView, SingleNewsApiView


urlpatterns = [
    path('news_en/', NewsApiView.as_view()),
    path('news_en/<slug:slug>/', SingleNewsApiView.as_view()),
]
