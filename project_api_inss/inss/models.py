from django.db import models

class CadastroInss(models.Model):
    nome = models.CharField(max_length=120)
    idade = models.IntegerField(default=0)
    data_nascimento = models.DateField(blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=10, blank=False, null=False)
    data_cadastro = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.nome
