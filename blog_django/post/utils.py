from .models import Post, Category


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['categories'] = categories

        if 'categories_selected' not in context:
            context['categories_selected'] = 0
        return context