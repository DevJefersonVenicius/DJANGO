from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    caracteristicas = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    reino = models.CharField(max_length=30)

    def __str__(self):
        return self.nome 
