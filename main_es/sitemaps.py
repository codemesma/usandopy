from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Tutorial
from django_blog_it.django_blog_it.models import Post


class StaticViewSitemap(Sitemap):
    def items(self):
        return['home-page',  'index', 'sobre']

    def location(self, item):
        return reverse(item)


class TutorialViewSitemap(Sitemap):
    def items(self):
        return Tutorial.objects.all()

    def lastmod(self, obj):
        return obj.updated_on


class PostViewSitemap(Sitemap):
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_on

