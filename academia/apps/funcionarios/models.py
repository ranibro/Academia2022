from unicodedata import decimal
from django.db import models

# Create your models here.
class Funcionario (models.Model):
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
    password = models.CharField('Digite a senha', max_length=16)
    idade = models.IntegerField('Digite sua idade')
    
    def __str__(self):
        return self.nome
    
   
    