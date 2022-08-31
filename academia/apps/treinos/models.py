from django.db import models
from academia.apps import equipamentos
from equipamentos import models

class Treinos (models.Model):
    nome = models.CharField('Digite seu nome', max_length=32)
    idade = models.IntegerField('Digite sua idade')
    
    def __str__(self):
        return self.nome

class Ficha (models.Model):
    treino = models.models.ForeignKey(Treinos, verbose_name=("Treino"), on_delete=models.CASCADE)
    