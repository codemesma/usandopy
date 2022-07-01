
from django.urls import path
from .views import *


app_name = "newspaper_en"

urlpatterns = [
    path('', HomeView.as_view(), name='noticias_en'),
    path('single/', SingleView.as_view(), name='single-page_en'),
    path('blog/', BlogView.as_view(), name='blog_en'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_en'),
    path('post/<slug:slug>/', PostSingleView.as_view(), name='single-post_en'),
    path('tag/<slug:tag>/', FilterByTag, name='tag_en'),
]
