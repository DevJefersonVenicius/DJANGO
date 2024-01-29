from rest_framework import viewsets
from .serializers import FarmaciaSerializer
from farmacias.models import Farmacia

class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer
    