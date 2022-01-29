from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Category
from django.contrib.auth.models import User


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['categories'] = categories

        if 'categories_selected' not in context:
            context['categories_selected'] = 0
        return context