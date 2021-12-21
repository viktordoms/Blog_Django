from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('<int:post_id>/', views.post, name="post"),
    path('category/<int:category_id>/', views.category, name="category")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
