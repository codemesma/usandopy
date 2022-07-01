from django.urls import path, re_path
from django.conf.urls.static import static
from .views import Home, SelectedCategoryView, CategoryView, TutorialView, AboutPageView, CookiePageView, Cookie, TermosPageView, SearchView
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [

    path('categoria/<int:id>/',SelectedCategoryView.as_view(), name='categoria-page_es'),
    path('categoria/<str:slug>/', CategoryView.as_view(), name='categoria-view_es'),
    path('tutorial/<str:slug>/', TutorialView.as_view(), name='tutorial-view_es'),
    path('sobre/', AboutPageView.as_view(), name='sobre_es'),
    path('politica/', CookiePageView.as_view(), name='cookie_es'),
    path('termos/', TermosPageView.as_view(), name='termo_es'),
    path('cookie/', Cookie.as_view(), name='cokie_es'),
    path('procura/', SearchView.as_view(), name='searcht_es'),
    path('', Home.as_view(), name='home-page_es'),

]
