from logging import PlaceHolder
from this import d
from django.db import models

# Create your models here.
class Clientes (models.Model):
    nome = models.CharField('Digite seu nome', max_length=200)
    email = models.EmailField('Digite seu email', max_length=200)
    
    def __str__(self):
        return self.nome