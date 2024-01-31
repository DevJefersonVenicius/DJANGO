from rest_framework import serializers
from rosto_corpo_gerenciamento_consultas.models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        