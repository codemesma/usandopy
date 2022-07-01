import os
import requests
import json
from datetime import datetime
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.shortcuts import redirect
from django_blog_it_en.django_blog_it_en.models import Post, Category, Tags, Canal, Equipa, Author
from django_blog_it_en.django_blog_it_en.forms import FeedbackForm
from django.db.models import Count
from django_blog_it_en import settings
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django_blog_it_en.django_blog_it_en.models import Post_Slugs
from django.db.models import Q
from main_en.models import Categoria, Sobre


def categories_tags_lists():
    categories_list = Category.objects.filter(
        is_active=True, post__status='Published').distinct()

    posts = Post.objects.filter(
        status='Published').order_by('-updated_on')[0:3]
    return {'categories_list': categories_list, 'recent_posts': posts}


class Home(ListView):
    template_name = "posts_en/home.html"
    queryset = Post.objects.filter(
        status='Published', category__is_active=True).order_by('-updated_on')
    context_object_name = "blog_posts"

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)

        categories_list = Category.objects.filter(
            is_active=True, post__status='Published').distinct()
        context['categoria'] = Categoria.objects.all()
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        posts = Post.objects.filter(
            status='Published').order_by('-updated_on')[0:3]
        context.update({
            'categories_list': categories_list,
            'recent_posts': posts,
            "description": settings.BLOG_DESCRIPTION,
            "title": 'UsandoPy - Blog',
            "keywords": settings.BLOG_KEYWORDS,
            "author": settings.BLOG_AUTHOR,
        })
        return context


class BlogPostView(DetailView):
    template_name = 'posts_en/detalhe.html'
    model = Post
    slug_url_kwarg = "blog_slug"
    context_object_name = "blog_name"

    def dispatch(self, request, *args, **kwargs):
        self.object = Post.objects.filter(slug=kwargs.get("blog_slug")).last()
        if not self.object:
            post_slug = get_object_or_404(
                Post_Slugs, slug=self.kwargs.get("blog_slug"))
            if self.kwargs.get("blog_slug") != post_slug.blog.slug:
                return HttpResponseRedirect(reverse('blog_post_view', kwargs={"blog_slug": post_slug.blog.slug}), status=301)
        return super(BlogPostView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostView, self).get_context_data(*args, **kwargs)

        author = Author.objects.all()
        categories_list = Category.objects.filter(
            is_active=True, post__status='Published').distinct()
        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        posts = Post.objects.filter(
            status='Published').order_by('-updated_on')[0:3]
        related_posts = Post.objects.filter(
            status='Published',
            category=self.object.category,
        ).exclude(id=self.object.id).distinct()[:3]
        context.update({
            'categories_list': categories_list,
            'recent_posts': posts,
            "related_posts": related_posts,
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.title,
            "keywords": self.object.keywords,
            "author": author,
            #"short_url": self.get_mini_url(self.request),

        })
        return context


class SelectedCategoryView(ListView):
    template_name = "posts_en/detalhe-cat.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, slug=self.kwargs.get("category_slug"))
        return Post.objects.filter(category=self.category, category__is_active=True, status='Published')

    def get_context_data(self, *args, **kwargs):
        context = super(SelectedCategoryView,
                        self).get_context_data(*args, **kwargs)
        user = self.category.user
        author = Author.objects.all()
        categories_list = Category.objects.filter(
            is_active=True, post__status='Published').distinct()
        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        posts = Post.objects.filter(
            status='Published').order_by('-updated_on')[0:3]
        context.update({
            'categories_list': categories_list,
            'recent_posts': posts,
            "description": self.category.description,
            "title": self.category.name,
            "keywords": self.category.meta_keywords,
            "author": author,
            "category": self.category,
        })
        return context


class ArchiveView(ListView):
    template_name = "posts_en/detalhe-cat.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        self.date = datetime(int(year), int(month), 1)
        return Post.objects.filter(
            category__is_active=True, status="Published", updated_on__year=year, updated_on__month=month).order_by('-updated_on')

    def get_context_data(self, *args, **kwargs):
        context = super(ArchiveView, self).get_context_data(*args, **kwargs)
        categories_list = Category.objects.filter(
            is_active=True, post__status='Published').distinct()
        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        posts = Post.objects.filter(
            status='Published').order_by('-updated_on')[0:3]
        context.update({
            'categories_list': categories_list,
            'recent_posts': posts,
            "description": "Blog Archive - " + self.date.strftime("%B %Y"),
            "title": "Blog Archive - " + self.date.strftime("%B %Y"),
            "keywords": "Blog Archive - " + self.date.strftime("%B %Y"),
            "author": settings.BLOG_AUTHOR,
            "date": self.date,
        })
        return context


class blog_SearchView(ListView):
    model = Post
    template_name = "posts_en/detalhe-sea.html"

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(keywords__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(blog_SearchView, self).get_context_data(
            *args, **kwargs)

        categories_list = Category.objects.filter(
            is_active=True, post__status='Published').distinct()
        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        posts = Post.objects.filter(
            status='Published').order_by('-updated_on')[0:3]

        context.update({
            'categories_list': categories_list,
            'recent_posts': posts,
            "description": settings.BLOG_DESCRIPTION,
            "title": 'Programador Angolano - Blog',
            "keywords": settings.BLOG_KEYWORDS,
            "author": settings.BLOG_AUTHOR,
        })
        return context


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'posts_en/contact.html', {'form': f})
