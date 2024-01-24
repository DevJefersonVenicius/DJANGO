from rest_framework import serializers
from inss.models import CadastroInss

class CadastroInssSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroInss
        fields = '__all__'
        