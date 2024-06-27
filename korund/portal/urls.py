from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),

    path('profile/', views.profile, name='profile'),
    

    path('dialogs/', views.dialog_list, name='dialog_list'),
    path('dialogs/<int:chat_id>/', views.dialog_detail, name='dialog_detail'),
    path('employees/', views.employee_list, name='employee_list'),

    # path('article_detail/<int:news_id>/', views.article_detail, name="article_detail") # со статьей
    path('article_detail/', views.article_detail, name="article_detail")# для верстки
     

]
