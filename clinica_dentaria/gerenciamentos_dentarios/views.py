from django.shortcuts import render, redirect
from .models import GerenciamentoDentario
from django.contrib import messages
from .forms import GerenciamentoDentarioForm

def index(request):
    dentes = GerenciamentoDentario.objects.all()
    return render(request, 'gerenciamentos_dentarios/index.html', {'dentes' : dentes})

def register(request):
    if request.method == 'POST':
        form = GerenciamentoDentarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento Dentario Cadastrado com Sucesso!')
            form = GerenciamentoDentarioForm()
        else:
            messages.error(request, 'Erro ao Cadastrar Agendamento Dentario')
    else:
        form = GerenciamentoDentarioForm()
    return render(request, 'gerenciamentos_dentarios/register.html', {'form' : form})

def deletar(request, id):
    deleteme = GerenciamentoDentario.objects.get(id=id)
    if request.method == 'POST':
        deleteme.delete()
        return redirect('/')
    return render(request, 'gerenciamentos_dentarios/deletar.html')

def area_exibicao(request):
    return render(request, 'gerenciamentos_dentarios/area_exibicao.html')
