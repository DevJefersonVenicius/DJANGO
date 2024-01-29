from rest_framework import serializers
from cadastro_medicamentos.models import Medicamento

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
    