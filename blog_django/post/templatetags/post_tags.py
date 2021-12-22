from django import template
from post.models import Category, Post


register = template.Library()


@register.inclusion_tag('post/inclusion_tag_html/list_categories.html')
def list_categories(sort=None, categories_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {"categories": categories, "categories_selected": categories_selected}


@register.inclusion_tag('post/inclusion_tag_html/show_posts.html')
def show_posts(sort=None):
    if not sort:
        posts = Post.objects.all()
    else:
        posts = Post.objects.order_by(sort)

    return {"posts": posts, }


