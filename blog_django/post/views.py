from django.shortcuts import render


def all_post(request):
    data = {"title": "Всі пости"}
    return render(request, "post/all_post.html", data)
