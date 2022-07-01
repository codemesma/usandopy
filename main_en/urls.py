from django.urls import path, re_path
from django.conf.urls.static import static
from .views import Home,Tutoriais, DownloadCode, SelectedCategoryView, CategoryView, TutorialView, AboutPageView, CookiePageView, Cookie, TermosPageView, SearchView
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [

    path('en/categoria/<int:id>/',SelectedCategoryView.as_view(), name='categoria-page_en'),
    path('category/<str:slug>/', CategoryView.as_view(), name='categoria-view_en'),
    path('tutorial/<str:slug>/', TutorialView.as_view(), name='tutorial-view_en'),
    path('downloads/<str:slug>/', DownloadCode.as_view(), name='download-view_en'),
    path('about/', AboutPageView.as_view(), name='sobre_en'),
    path('policy/', CookiePageView.as_view(), name='cookie_en'),
    path('terms/', TermosPageView.as_view(), name='termo_en'),
    path('cookie/', Cookie.as_view(), name='cokie_en'),
    path('tutorial_en', Tutoriais.as_view(), name='tutorial-page_en'),
    path('search/', SearchView.as_view(), name='searcht_en'),
    path('', Home.as_view(), name='home-page_en'),

]
