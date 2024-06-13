from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import News, Event

def login_view(request):
    if request.method == "POST":
        username = request.POST['PostgreSQL 16']
        password = request.POST['1234']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'portal/authorisation.html', {'error': 'Неправильный логин или пароль'})
    return render(request, 'portal/authorisation.html')

def index(request):
    news = News.objects.all()
    events = Event.objects.all()
    return render(request, 'portal/index.html', {'news': news, 'events': events})
