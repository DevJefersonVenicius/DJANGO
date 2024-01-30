from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reuniao
from .forms import ReuniaoForm

def index(request):
    reunioes = Reuniao.objects.all()
    return render(request, 'reunioes_project/index.html', {'reunioes' : reunioes})

def register(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião Cadastrada')
            form = ReuniaoForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = ReuniaoForm()

    return render(request, 'reunioes_project/register.html', {'form' : form},)

def delete_reuniao(request, id):
    reuniao_cancelada = Reuniao.objects.get(id=id)
    if request.method == 'POST':
        reuniao_cancelada.delete()
        return redirect('/')
    return render(request, 'reunioes_project/delete.html')
