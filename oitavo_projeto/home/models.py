from django.db import models

class Livraria(models.Model):
    nome_livro = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    editora = models.CharField(max_length=30)
    ano_publicacao = models.IntegerField(default=0)
    qntd_paginas = models.IntegerField(default=0)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome_livro
