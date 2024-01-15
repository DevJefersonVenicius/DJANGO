from django.shortcuts import render
from django.http import HttpResponse
from .models import MeuSite

def home(request):
    meus_sites = MeuSite.objects.all()

    context = {
        'sites' : meus_sites
    }
    
    return render(request, 'home/index.html', context)
