# portal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),  # Новый маршрут для личного кабинета
]
