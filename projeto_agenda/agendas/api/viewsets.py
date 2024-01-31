from rest_framework import viewsets
from .serializers import AgendaSerializer
from agendas.models import Agenda

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    