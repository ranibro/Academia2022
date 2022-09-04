from django.db import models
from apps.equipamentos.models import Equipamentos
from django.contrib.auth.models import User

# Create your models here.
#fazer um status de inativo ou ativo

class Clientes (models.Model):
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
    password = models.CharField('Digite a senha', max_length=16)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return "{} - {} - {}".format(self.nome, self.email, self.usuario)

#Mover esse exercicio para outro APP depois
class Exercicio (models.Model):
    repetições = models.IntegerField()
    carga = models.IntegerField()
    serie = models.IntegerField()
    tempo = models.IntegerField(null=True, help_text="Opcional")
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.equipamento)

class Treino (models.Model):
    nome = models.CharField('Nome do Treino', max_length=16)
    exercicio = models.ManyToManyField(Exercicio)