from django.shortcuts import render
from django.contrib import messages
from .models import Farmacia
from .forms import FarmaciaForm

def index(request):
    farmacias = Farmacia.objects.all()
    return render(request, 'farmacias/index.html', {'farmacias' : farmacias},)

def register(request):
    if request.method == 'POST':
        form = FarmaciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmacia Cadastrada')
            form = FarmaciaForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = FarmaciaForm()

    return render(request, 'farmacias/register.html', {'form' : form},)
