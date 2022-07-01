
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views as sitemap_views
from main.sitemaps import StaticViewSitemap, TutorialViewSitemap, PostViewSitemap

from classroom.views import classroom, students, teachers
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404


sitemaps = {
    'home-page': StaticViewSitemap,
    'tutorial': TutorialViewSitemap,
    'blog':  PostViewSitemap,
}


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', include('main.urls')),
    path('noticias/', include('mainsite.urls')),
    path('news/', include('mainsite_en.urls')),
    path('en/', include('main_en.urls')),
    path('es/', include('main_es.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('django_blog_it.urls')),
    path('blog_en/', include('django_blog_it_en.urls')),
    path('sitemaps.xml/', sitemap, {'sitemaps': sitemaps}),
    #url(r'^accounts/', include('allauth.urls')),

    path('quiz/', include('classroom.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),
    
    # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls'),name='signup_'),
    path('accounts/signup/', students.StudentSignUpView.as_view(), name='signup'),
    # path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.error_404_view'

