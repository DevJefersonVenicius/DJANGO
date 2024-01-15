from django.contrib import admin
from .models import MeuSite

class ListMeuSite(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'estuda', 'busca')

admin.site.register(MeuSite, ListMeuSite)
