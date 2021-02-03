from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {
        'title':'Blog',
        'message':'Lista de artículos',
        'articulos': [
            {'title':'artículo uno', 'autor': 'Daried Gil', 'published':True},
            {'title':'artículo dos', 'autor': 'Luis Duran', 'published':True},
            {'title':'artículo tres', 'autor': 'Justo Martinez', 'published':False},
            {'title':'artículo cuatro', 'autor': 'Justo Martinez', 'published':False},
            {'title':'artículo cinco', 'autor': 'Jorge Montiel', 'published':True},
        ]
        
    })

