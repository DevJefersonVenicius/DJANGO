from django.db import models

class Farmacia(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='farmacias', blank=True, null=True)
    valuation = models.DecimalField(max_digits=4, decimal_places=2)
    cad_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
