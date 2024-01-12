from django.db import models

class Acougue(models.Model):
    nome_carne = models.CharField(max_length=30)
    tipo_carne = models.CharField(max_length=30)
    fazenda = models.CharField(max_length=30)
    data_corte = models.IntegerField(default=0)
    preco_carne = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome_carne
