from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('create_post/', views.create_post, name="create_post"),
    path('<slug:post_slug>/', views.post, name="post"),
    path('category/<int:category_id>/', views.category, name="category"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


