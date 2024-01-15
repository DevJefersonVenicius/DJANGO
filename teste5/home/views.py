from django.shortcuts import render
from django.http import HttpResponse
from .models import Carro

def home(request):
    meus_carros = Carro.objects.all()

    context = {
        'carros' : meus_carros
    }
    
    return render(request, 'home/index.html', context)
