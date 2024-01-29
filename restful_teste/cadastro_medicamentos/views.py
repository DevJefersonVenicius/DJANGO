from django.shortcuts import render
from django.contrib import messages
from .models import Medicamento
from .forms import MedicamentoForm

def index(request):
    medicamento = Medicamento.objects.all()
    return render(request, 'cadastro_medicamentos/index.html', {'medicamento' : medicamento},)

def register(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento Cadastrado')
            form = MedicamentoForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = MedicamentoForm()

    return render(request, 'cadastro_medicamentos/register.html', {'form' : form},)
