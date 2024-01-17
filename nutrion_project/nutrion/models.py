from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    nome = models.CharField(max_length=100)
    carboidratos = models.FloatField(default=0.0)
    proteinas = models.FloatField(default=0.0)
    gorduras = models.FloatField(default=0.0)
    calorias = models.IntegerField(default=0.0)

    def __str__(self):
        return self.nome

class Consumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeira - é uma informação que pertence ao model User
    comida_consumida = models.ForeignKey(Food, on_delete=models.CASCADE)
