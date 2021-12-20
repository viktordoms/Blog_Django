from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_post, name='all_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
