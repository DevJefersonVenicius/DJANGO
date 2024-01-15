from django.contrib import admin
from .models import Animal

class ListAnimal(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'caracteristicas', 'raca', 'reino')

admin.site.register(Animal, ListAnimal)
