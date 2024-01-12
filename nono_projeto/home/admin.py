from django.contrib import admin
from .models import Acougue

class ListAcougue(admin.ModelAdmin):
    list_display = ('nome_carne', 'tipo_carne', 'fazenda', 'data_corte', 'preco_carne')

admin.site.register(Acougue, ListAcougue)
