from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('my-post', views.MyPost.as_view(), name='my_post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
