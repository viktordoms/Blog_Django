from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post as PostModel
from .forms import *
from .utils import *


def pageNotFound(request, expertion):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


class CreatePost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'post/create_post.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новий пост")
        return dict(list(context.items()) + list(c_def.items()))


class AllPost(DataMixin, ListView):
    paginate_by = 2
    model = PostModel
    template_name = 'post/all_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Всі пости")
        return dict(list(context.items()) + list(c_def.items()))


class Post(DataMixin, DetailView):
    model = PostModel
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PostCategory(DataMixin, ListView):
    paginate_by = 1
    model = PostModel
    template_name = 'post/category.html'
    context_object_name = 'post_category'
    allow_empty = False

    def get_queryset(self):
        return PostModel.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - ' + str(context['post_category'][0].category),
                                      categories_selected=context['post_category'][0].category_id)

        return dict(list(context.items()) + list(c_def.items()))

