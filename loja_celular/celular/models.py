from django.db import models

class Celular(models.Model):
    nome = models.CharField(max_length=100)
    