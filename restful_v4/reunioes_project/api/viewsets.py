from rest_framework import viewsets
from .serializers import ReuniaoSerializer
from reunioes_project.models import Reuniao

class ReuniaoViewSet(viewsets.ModelViewSet):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer
    