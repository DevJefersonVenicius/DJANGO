from django.db import models

class PontoTuristico(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    comments = models.TextField()
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True) # NULL - nulo BLANK - vazio, pode deixar vazio
    valuation = models.DecimalField(max_digits=2, decimal_places=2)
    cad_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
