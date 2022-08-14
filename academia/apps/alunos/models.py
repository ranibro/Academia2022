from unicodedata import decimal
from django.db import models

# Create your models here.
class Clientes (models.Model):
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
#Para Senha tem que ser PassworlField
    password = models.CharField('Digite a senha', max_length=16)
    idade = models.IntegerField('Digite sua idade')
#Altura é valor fracionado, não inteiro.
    altura =  models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Digite sua altura')
    peso = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Digite seu peso')

    def __str__(self):
        return self.nome
    
   
    