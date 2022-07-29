from unicodedata import decimal
from django.db import models
from django import forms
# Create your models here.
class Clientes (models.Model):
    nome = models.CharField('Digite seu nome', max_length=200)
    email = models.EmailField('Digite seu email', max_length=200)
    password = models.CharField('Digite a senha', max_length=200 )
    idade = models.IntegerField('Digite sua idade')
    altura =  models.IntegerField('Digite sua altura')
    peso = models.IntegerField('Digite seu peso')

    def __str__(self):
        return self.nome
    
   
    
