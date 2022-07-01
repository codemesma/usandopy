from datetime import datetime
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Count
from main import settings
from django.contrib import messages
from django.template import Context
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Tutorial, Categoria, Tipo, Sobre , Download
from django_blog_it_en.django_blog_it_en.models import Post, Canal, Equipa
from django.db.models import Q

from hitcount.views import HitCountDetailView

from mainsite_en.models import HomePageSettings
from news_en.models import Category, News



def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)


class Home(ListView):
    template_name = "bases_en/home.html"
    queryset = Categoria.objects.filter(is_active=True).order_by('id')
    context_object_name = "cat"

    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(
            category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(
            category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(
            category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(
            category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(
            category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)

        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:14]
        context['post'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:3]
        context['post_banner'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:14]
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')


        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context

class Tutoriais(ListView):
    template_name = "bases_en/tutorial.html"
    queryset = Categoria.objects.filter(is_active=True).order_by('id')
    context_object_name = "cat"

    def get_context_data(self, *args, **kwargs):
        context = super(Tutoriais, self).get_context_data(*args, **kwargs)

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:20]
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')


        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context

class TutorialView(HitCountDetailView, DetailView, ):
    model = Tutorial
    context_object_name = 'tutorial'
    template_name = 'display_en/detalhe-view.html'
    query_pk_and_slug = True
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(TutorialView, self).get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.all()

        tut = Tutorial.objects.all()
        context['tut'] = tut
        context['categoria'] = Categoria.objects.all()
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.title,
            "keywords": self.object.keywords,
            "author": self.object.user,
            # "short_url": self.get_mini_url(self.request)
        })
        return context


class DownloadCode(HitCountDetailView, DetailView):
    model = Download
    context_object_name = 'tutorial'
    template_name = 'display_en/download.html'
    query_pk_and_slug = True
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(DownloadCode, self).get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.all()
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.nome,
            "keywords": self.object.keywords,
            # "short_url": self.get_mini_url(self.request)
        })
        return context


class SelectedCategoryView(ListView):
    model = Categoria
    template_name = "display_en/categoria.html"

    def get_queryset(self):

        self.tipo = get_object_or_404(Tipo, id=self.kwargs['id'])
        return Categoria.objects.filter(tipo=self.tipo, is_active=True,)


class CategoryView(DetailView):
    model = Categoria
    context_object_name = 'cat'
    template_name = 'bases_en/detalhe.html'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        tut = Tutorial.objects.all()
        context['sobre'] = Sobre.objects.all()

        context['tut'] = tut
        context['categoria'] = Categoria.objects.all()
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.name,
        })
        return context


class CookiePageView(ListView):
    template_name = 'bases_en/cookie.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(CookiePageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class TermosPageView(ListView):
    template_name = 'bases_en/termos.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(TermosPageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class Cookie(ListView):
    template_name = 'bases_en/cokie.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(Cookie, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class SearchView(ListView):
    model = Tutorial
    template_name = "bases_en/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Tutorial.objects.filter(
            Q(title__icontains=query) | Q(keywords__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)

        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class AboutPageView(ListView):
    template_name = 'bases_en/sobre.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutPageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context
