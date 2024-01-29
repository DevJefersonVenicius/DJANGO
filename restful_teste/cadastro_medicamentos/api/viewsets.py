from rest_framework import viewsets
from .serializers import MedicamentoSerializer
from cadastro_medicamentos.models import Medicamento

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    