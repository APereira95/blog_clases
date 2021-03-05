from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from .forms import RegisterForm

def index(request):
    return render(request, 'index.html', {
        'title':'Blog',
        'header':'Lista de artículos',
        'metadescription': 'Esto es una descripción para ayudar al posicionamiento SEO de 130 palabras',
        'articulos': [
            {'title':'artículo uno', 'autor': 'Daried Gil', 'published':True},
            {'title':'artículo dos', 'autor': 'Luis Duran', 'published':True},
            {'title':'artículo tres', 'autor': 'Justo Martinez', 'published':False},
            {'title':'artículo cuatro', 'autor': 'Justo Martinez', 'published':False},
            {'title':'artículo cinco', 'autor': 'Jorge Montiel', 'published':True},
        ]

    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña invalida')

    return render(request, 'users/login.html', {
        'title':'Login',
        'header':'Login'
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado con éxito')
            return redirect('index')

    return render(request, 'users/register.html', {
        'title':'Registro',
        'header':'Registro',
        'form':form
    })