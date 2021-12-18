from django.shortcuts import render


def main_header(request):
    return render(request, "main/main.html")


def registration(request):
    return render(request, "main/registration.html")


def login(request):
    return render(request, "main/login.html")
