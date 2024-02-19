from django.db import models

class Consulta(models.Model):
    DIA_CONSULTA_CHOICES = (
        ('DOM', 'Domingo'),
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
        ('SAB', 'Sabado'),
    )

    nome_paciente = models.CharField(max_length=150)
    idade = models.IntegerField(default=0)
    cpf = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    dia_consulta = models.CharField(max_length=3, choices=DIA_CONSULTA_CHOICES, default='DOM')
    imagem = models.ImageField(upload_to='fotos')
    hora_marcada = models.DateTimeField()
    processo_agendado = models.TextField()

    def __str__(self):
        return self.nome_paciente