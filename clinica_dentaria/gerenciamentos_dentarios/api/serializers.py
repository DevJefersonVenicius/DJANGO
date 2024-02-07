from rest_framework import serializers
from gerenciamentos_dentarios.models import GerenciamentoDentario

class GerenciamentoDentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GerenciamentoDentario
        fields = '__all__'
        