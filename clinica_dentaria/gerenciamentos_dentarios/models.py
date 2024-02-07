from django.db import models

class GerenciamentoDentario(models.Model):
    CONSULTA_CHOICES = (
        ('SEG', 'Segunda'),
        ('TER', 'Terça'),
        ('QUA', 'Quarta'),
        ('QUI', 'Quinta'),
        ('SEX', 'Sexta'),
    )
    
    HORARIO_CHOICES = (
        ('H1', '8:00h ás 11:00h'),
        ('H2', '13:00h ás 17:00h'),
        ('H3', '19:00 ás 22:00'),
    )

    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    data_tempo_cadastro = models.DateTimeField(auto_now_add=True)
    idade = models.IntegerField(default=0)
    dia_consulta = models.CharField(max_length=3, choices=CONSULTA_CHOICES, default='SEG')
    horario = models.CharField(max_length=2, choices=HORARIO_CHOICES, default='H1')
    descricao = models.TextField()
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.nome
    