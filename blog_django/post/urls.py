from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AllPost.as_view(), name='all_post'),
    path('create_post/', views.CreatePost.as_view(), name="create_post"),
    path('<slug:post_slug>/', views.Post.as_view(), name="post"),
    path('category/<slug:category_slug>/', views.PostCategory.as_view(), name="category"),
    path('like/<slug:post_slug>', views.LikeView, name="like_post"),
    path('edit_post/<slug:post_slug>/', views.edit_post, name='edit_post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

