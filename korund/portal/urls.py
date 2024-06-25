from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include #добваила-изменила 
from portal import views


urlpatterns = [
    path('admin/', admin.site.urls), # import admin urls !only! at the project root
    path('', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dialogs/', views.dialog_list, name='dialog_list'),
    path('dialogs/<int:chat_id>/', views.dialog_detail, name='dialog_detail'),
    path('employees/', views.employee_list, name='employee_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
