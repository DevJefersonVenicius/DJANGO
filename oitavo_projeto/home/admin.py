from django.contrib import admin
from .models import Livraria

class ListLivraria(admin.ModelAdmin):
    list_display = ('nome_livro', 'autor', 'editora', 'ano_publicacao', 'qntd_paginas', 'preco')

admin.site.register(Livraria, ListLivraria)
