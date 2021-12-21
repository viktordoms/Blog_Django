from django.shortcuts import render
from .models import *
from django.http import HttpResponseNotFound

posts = Post.objects.all()
categories = Category.objects.all()


def pageNotFound(request, expertion):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")


def all_post(request):
    data = {"title": "Всі пости",
            "posts": posts,
            "categories": categories,
            "categories_selected": 0,
            }
    return render(request, "post/all_post.html", data)


def post(request, post_id):
    data = {"title": "Деталі поста",
            "post_id": post_id,
            "categories": categories,
            "categories_selected": 0,
            }
    return render(request, "post/post_detail.html", data)


def category(request, category_id):
    post_category = Post.objects.filter(category_id=category_id)
    data = {"title": "Категорія:",
            "post_category": post_category,
            "categories": categories,
            "categories_selected": category_id,
            }

    return render(request, "post/category.html", data)

