from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView

from .models import Post as PostModel
from .forms import *


def pageNotFound(request, expertion):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


class CreatePost(CreateView):
    form_class = AddPostForm
    template_name = 'post/create_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новий пост'
        return context


class AllPost(ListView):
    model = PostModel
    template_name = 'post/all_post.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Всі пости'
        context['categories_selected'] = 0
        return context

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)


class Post(DetailView):
    model = PostModel
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['categories_selected'] = 0
        return context


class PostCategory(ListView):
    model = PostModel
    template_name = 'post/category.html'
    context_object_name = 'post_category'
    allow_empty = False

    def get_queryset(self):
        return PostModel.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія - ' + str(context['post_category'][0].category)
        context['categories_selected'] = context['post_category'][0].category_id
        return context


