from django.shortcuts import render
from django.http import HttpResponse
from .models import Musica

def home(request):
    minhas_musicas = Musica.objects.all()

    context = {
        'musicas' : minhas_musicas
    }
    
    return render(request, 'home/index.html', context)
