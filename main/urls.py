from django.urls import path, re_path
from django.conf.urls.static import static
from .views import Home,Tutoriais,DownloadCode, SelectedCategoryView, CategoryView, TutorialView, AboutPageView, CookiePageView, Cookie, TermosPageView, SearchView, AdsView
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [

    path('categoria/<int:id>/',SelectedCategoryView.as_view(), name='categoria-page'),
    path('categoria/<str:slug>/', CategoryView.as_view(), name='categoria-view'),
    path('tutorial/<str:slug>/', TutorialView.as_view(), name='tutorial-view'),
    path('download/<str:slug>/', DownloadCode.as_view(), name='download-view'),
    path('sobre/', AboutPageView.as_view(), name='sobre'),
    path('politica/', CookiePageView.as_view(), name='cookie'),
    path('termos/', TermosPageView.as_view(), name='termo'),
    path('cookie/', Cookie.as_view(), name='cokie'),
    path('procura/', SearchView.as_view(), name='searcht'),
    path('tutorial', Tutoriais.as_view(), name='tutorial-page'),
    path('ads.txt', AdsView.as_view()),
    path('', Home.as_view(), name='home-page'),

]
