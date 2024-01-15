from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def home(request):
    meus_animais = Animal.objects.all()

    context = {
        'animais' : meus_animais
    }
    
    return render(request, 'home/index.html', context)
