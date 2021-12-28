from django.shortcuts import get_object_or_404, redirect, reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Post as PostModel
from .forms import *
from .utils import *


def pageNotFound(request, expertion):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


@login_required
def LikeView(request, post_slug):
    post = get_object_or_404(PostModel, slug=request.POST.get("post_slug"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post', args=[str(post_slug)]))


class CreatePost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'post/create_post.html'
    login_url = reverse_lazy('login')
    prepopulated_fields = {"slug": ("title",)}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новий пост")
        return dict(list(context.items()) + list(c_def.items()))


class AllPost(DataMixin, ListView):
    paginate_by = 4
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

        staff = get_object_or_404(PostModel, slug=self.kwargs['post_slug'])
        total_likes = staff.total_likes()

        liked = False
        if staff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context["liked"] = liked
        return dict(list(context.items()) + list(c_def.items()))


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, DataMixin, UpdateView):
    form_class = AddPostForm
    model = PostModel
    template_name = 'post/update_post.html'
    login_url = reverse_lazy('login')
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DataMixin, DeleteView):
    model = PostModel
    template_name = 'post/delete_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('my_post')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostCategory(DataMixin, ListView):
    paginate_by = 4
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

