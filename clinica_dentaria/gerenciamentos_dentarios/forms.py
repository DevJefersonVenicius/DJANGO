from django import forms
from .models import GerenciamentoDentario

class GerenciamentoDentarioForm(forms.ModelForm):
    class Meta:
        model = GerenciamentoDentario
        fields = '__all__'
