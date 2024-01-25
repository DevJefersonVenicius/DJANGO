from django import forms
from .models import Farmacia

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = '__all__'
