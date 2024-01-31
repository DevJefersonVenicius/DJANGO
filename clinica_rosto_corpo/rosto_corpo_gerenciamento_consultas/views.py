from django.shortcuts import render, redirect
from .models import Consulta
from django.contrib import messages
from .forms import ConsultaForm

def index(request):
    consultas = Consulta.objects.all()
    return render(request, 'rosto_corpo_gerenciamento_consultas/index.html', {'consultas' : consultas})

def cadastro(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta Cadastrada com Sucesso!')
            form = ConsultaForm()
        else:
            messages.error(request, 'Erro ao Salvar Consulta!')
    else:
        form = ConsultaForm()
    return render(request, 'rosto_corpo_gerenciamento_consultas/cadastro.html', {'form' : form })

def deletar(request, id):
    deleteme = Consulta.objects.get(id=id)
    if request.method == 'POST':
        deleteme.delete()
        return redirect('/')
    return render(request, 'rosto_corpo_gerenciamento_consultas/deletar.html')
    