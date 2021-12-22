from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponseNotFound
from .forms import *

posts = Post.objects.all()


def pageNotFound(request, expertion):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


def create_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    else:
        form = AddPostForm()

    data = {"title": "Новий пост",
            "form": form,
            }
    return render(request, "post/create_post.html", data)


def all_post(request):
    data = {"title": "Всі пости",
            "posts": posts,
            "categories_selected": 0,
            }
    return render(request, "post/all_post.html", data)


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {'title': post.title,
            'post': post,
            'categories_selected': post.category_id
            }

    return render(request, "post/post_detail.html", data)


def category(request, category_id):
    post_category = Post.objects.filter(category_id=category_id)
    data = {"title": "Категорія:",
            "post_category": post_category,
            "categories_selected": category_id,
            }
    return render(request, "post/category.html", data)


