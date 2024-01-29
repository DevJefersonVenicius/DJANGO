from django.db import models

class AtracaoTuristica(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    aproved = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='atracoes_turisticas', null=True, blank=True) # NULL - nulo BLANK - vazio, pode deixar vazio
    valuation = models.DecimalField(max_digits=4, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    cad_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    