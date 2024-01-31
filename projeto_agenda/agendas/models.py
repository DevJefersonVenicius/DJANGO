from django.db import models

class Agenda(models.Model):
    DIAS_CHOICES =  (
        ('DOM', 'Domingo'),
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sabado'),
    )

    disciplina = models.CharField(max_length=100)
    assunto = models.TextField()
    tempo_estudado = models.IntegerField(default=0)
    dia_semana = models.CharField(max_length=3, choices=DIAS_CHOICES, default='DOM')
    foto = models.ImageField(upload_to='assuntos')

    def __str__(self):
        return self.disciplina
