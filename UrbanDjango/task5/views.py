from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

# Create your views here.
users = ['Serg1', 'Serg2', 'Ser3']

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info = {'head': 'html ', 'error': 'Пароли не совпадают'}
            return render(request, 'fifth_task/registration_page.html', context=info)
        if int(age) < 18:
            info = {'head': 'html ', 'error': 'Вы должны быть старше 18'}
            return render(request, 'fifth_task/registration_page.html', context=info)
        if users.count(username) > 0:
            info = {'head': 'html ', 'error': f'Пользователь {username} уже существует'}
            return render(request, 'fifth_task/registration_page.html', context=info)

        return HttpResponse(f'{username}, Вы успешно прошли регистрацию. <p><a href="/">На главную</a></p> ')
    info = {'head': 'html ', 'error': ''}
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info = {'head': 'html ', 'error': 'Пароли не совпадают'}
                return render(request, 'fifth_task/registration_page.html', context=info)
            if int(age) < 18:
                info = {'head': 'html ', 'error': 'Вы должны быть старше 18'}
                return render(request, 'fifth_task/registration_page.html', context=info)
            if users.count(username) > 0:
                info = {'head': 'html ', 'error': f'Пользователь {username} уже существует'}
                return render(request, 'fifth_task/registration_page.html', context=info)
            return HttpResponse(f'{username}, Вы успешно прошли регистрацию. <p><a href="/">На главную</a></p> ')
    else:
        form = UserRegister()
        info = {'form': form, 'head': 'Django ', 'error': ''}
        return render(request, 'fifth_task/registration_page.html', context=info)
