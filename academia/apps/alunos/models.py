from django.db import models
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
    
