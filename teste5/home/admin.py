from django.contrib import admin
from .models import Carro

class ListCarro(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'modelo', 'motor', 'pintura', 'ano', 'placa')

admin.site.register(Carro, ListCarro)
