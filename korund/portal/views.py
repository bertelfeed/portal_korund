# portal/views.py

from django.shortcuts import render, redirect
from .models import Employee, News, Event
from .utils import add_password, get_password, check_password

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = Employee.objects.filter(email=email).first()
        if user:
            stored_password = get_password(email)
            if stored_password and check_password(password, stored_password):
                # Имитация аутентификации для демонстрации
                request.session['user_id'] = user.id
                return redirect('index')
            else:
                return render(request, 'portal/authorisation.html', {'error': 'Неправильный логин или пароль'})
    return render(request, 'portal/authorisation.html')

def register_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        middle_name = request.POST.get('middle_name', '')
        employee_number = request.POST['employee_number']

        if Employee.objects.filter(email=email).exists():
            return render(request, 'portal/register.html', {'error': 'Email уже зарегистрирован'})

        # Добавьте пользователя в базу данных
        Employee.objects.create(
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            employee_number=employee_number,
            employment_status='активный',  # Вы можете задать значения по умолчанию здесь
            role='пользователь',  # Вы можете задать значения по умолчанию здесь
            hire_date='2024-01-01'  # Установите текущую дату найма
        )

        # Сохраните пароль в JSON файл
        add_password(email, password)

        return redirect('login')
    return render(request, 'portal/register.html')

def index(request):
    if 'user_id' not in request.session:
        return redirect('login')
    news = News.objects.all()
    events = Event.objects.all()
    return render(request, 'portal/index.html', {'news': news, 'events': events})

def profile_view(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = Employee.objects.get(id=request.session['user_id'])
    return render(request, 'portal/profile.html', {'user': user})
