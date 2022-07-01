from datetime import datetime
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Count
from main import settings
from django.contrib import messages
from django.template import Context
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Tutorial, Categoria, Tipo, Sobre
from django_blog_it.django_blog_it.models import Post, Canal, Equipa
from django.db.models import Q

from hitcount.views import HitCountDetailView


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)


class Home(ListView):
    template_name = "bases_es/home.html"
    queryset = Categoria.objects.filter(is_active=True).order_by('id')
    context_object_name = "cat"

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:6]
        context['post'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:6]
        context['post_banner'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:6]
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')


        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class TutorialView(HitCountDetailView, DetailView):
    model = Tutorial
    context_object_name = 'tutorial'
    template_name = 'display_es/detalhe-view.html'
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


class SelectedCategoryView(ListView):
    model = Categoria
    template_name = "display_es/categoria.html"

    def get_queryset(self):

        self.tipo = get_object_or_404(Tipo, id=self.kwargs['id'])
        return Categoria.objects.filter(tipo=self.tipo, is_active=True,)


class CategoryView(DetailView):
    model = Categoria
    context_object_name = 'cat'
    template_name = 'bases_es/detalhe.html'
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
    template_name = 'bases_es/cookie.html'
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
    template_name = 'bases_es/termos.html'
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
    template_name = 'bases_es/cokie.html'
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
    template_name = "bases_es/search.html"

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
    template_name = 'bases_es/sobre.html'
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
