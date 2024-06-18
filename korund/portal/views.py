from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import News, Employee, Chat, Message

def index(request):
    news_list = News.objects.all()
    return render(request, 'portal/index.html', {'news_list': news_list})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                Employee.objects.create(user=user, email=email, last_name='', first_name='', employment_status='активный', employee_number='', role='пользователь', hire_date='2024-01-01')
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'portal/register.html', {'error_message': 'Пользователь с таким логином уже существует'})
        else:
            return render(request, 'portal/register.html', {'error_message': 'Пароли не совпадают'})
    return render(request, 'portal/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'portal/login.html', {'error_message': 'Неправильное имя пользователя или пароль'})
    return render(request, 'portal/login.html')

@login_required
def profile(request):
    return render(request, 'portal/profile.html', {'user': request.user})

@login_required
def dialog_list(request):
    chats = Chat.objects.filter(chatparticipant__employee=request.user.employee)
    return render(request, 'portal/dialog_list.html', {'chats': chats})

@login_required
def dialog_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        Message.objects.create(chat=chat, employee=request.user.employee, message_content=message_content)
        return redirect('dialog_detail', chat_id=chat.id)
    messages = Message.objects.filter(chat=chat)
    return render(request, 'portal/dialog_detail.html', {'chat': chat, 'messages': messages})

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'portal/employee_list.html', {'employees': employees})
