from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from post.utils import DataMixin
from .forms import *
from post.models import Post as PostModel
from django.contrib.auth.models import User


class MyPost(LoginRequiredMixin, DataMixin, ListView):
    paginate_by = 3
    model = PostModel
    template_name = 'main/my_post.html'
    context_object_name = 'my_posts'

    def get_queryset(self):
        return PostModel.objects.filter(user__id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мої Пости")
        return dict(list(context.items()) + list(c_def.items()))


class Main(DataMixin, ListView):
    paginate_by = 3
    model = PostModel
    template_name = 'main/main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return PostModel.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')
