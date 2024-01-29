from django.db import models

class Medicamento(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cadastro_medicamentos')
    type_drug = models.CharField(max_length=30)
    bula = models.TextField()
    efects = models.CharField(max_length=100)
    date_use = models.TimeField()
    bagde_drug = models.CharField(max_length=100)

    def __str__(self):
        return self.name
