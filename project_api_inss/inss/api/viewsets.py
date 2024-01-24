from rest_framework import viewsets
from .serializers import CadastroInssSerializer
from inss.models import CadastroInss

class CadastroInssViewSet(viewsets.ModelViewSet):
    queryset = CadastroInss.objects.all()
    serializer_class = CadastroInssSerializer
    