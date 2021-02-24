from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html', {
        'title':'Blog',
        'header':'Lista de artículos',
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

    })
