from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    motor = models.CharField(max_length=30)
    pintura = models.CharField(max_length=30)
    ano = models.IntegerField(default=0)
    placa = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
