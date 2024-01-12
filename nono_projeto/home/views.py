from django.shortcuts import render
from django.http import HttpResponse
from .models import Acougue

def home(request):
    meu_acougue = Acougue.objects.all()

    context = {
        'carnes' : meu_acougue
    }

    return render(request, 'home/index.html', context)
