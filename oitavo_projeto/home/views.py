from django.shortcuts import render
from django.http import HttpResponse
from .models import Livraria

def home(request):
    meus_livros = Livraria.objects.all()

    context = {
        'livros' : meus_livros
    }
    
    return render(request, 'home/index.html', context)
