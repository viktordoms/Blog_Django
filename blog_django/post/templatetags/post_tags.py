from django import template
from post.models import Category, Post

from django.db.models import Count

register = template.Library()


@register.inclusion_tag('post/inclusion_tag_html/list_categories.html')
def list_categories(sort=None, categories_selected=0):
    categories = Category.objects.annotate(Count('post'))
    if not sort:
        categor = categories.all()
    else:
        categor = categories.order_by(sort)

    return {"categor": categor, "categories_selected": categories_selected}


@register.inclusion_tag('post/inclusion_tag_html/show_posts.html')
def show_posts(sort=None):
    publish_post = Post.objects.filter(is_published=True)
    if not sort:
        posts = publish_post
    else:
        posts = publish_post.order_by(sort)

    return {"posts": posts, }
