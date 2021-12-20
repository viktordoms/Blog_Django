from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy


def main(request):
    data = {"title": "Головна сторінка"}
    return render(request, "main/main.html", data)


def registration(request):
    data = {"title": "Реєстрація користувача"}
    return render(request, "main/registration.html", data)


def login(request):
    data = {"title": "Авторизація"}
    return render(request, "main/login.html", data)
