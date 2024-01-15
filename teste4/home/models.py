from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=30)
    artista = models.CharField(max_length=30)
    data_gravacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
