from django.db import models

# Create your models here.

class Equipamentos (models.Model):
    nome = models.CharField('Nome do Equipamento', max_length=16)
    descr = models.CharField('Descrição', max_length=64)

    def __str__(self):
        return self.nome