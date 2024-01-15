from django.db import models

class MeuSite(models.Model):
    nome = models.CharField(max_length=30)
    profissao = models.CharField(max_length=30)
    estuda = models.CharField(max_length=60)
    busca = models.TextField(max_length=350)

    def __str__(self):
        return self.nome
