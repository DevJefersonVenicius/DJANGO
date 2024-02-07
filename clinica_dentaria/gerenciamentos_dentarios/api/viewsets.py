from rest_framework import viewsets
from .serializers import GerenciamentoDentarioSerializer
from gerenciamentos_dentarios.models import GerenciamentoDentario

class GerenciamentoDentarioViewSet(viewsets.ModelViewSet):
    queryset = GerenciamentoDentario.objects.all()
    serializer_class = GerenciamentoDentarioSerializer
    