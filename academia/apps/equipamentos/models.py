from django.db import models
from stdimage import StdImageField
# Create your models here.

class Equipamentos (models.Model):
    STATUS_CHOICES = [
        ("Funcionando", "Funcionando"),
        ("Manutenção", "Manutenção"),
        ("Quebrado", "Quebrado")
    ]
    
    nome = models.CharField('Nome do Equipamento', max_length=16)
    descr = models.CharField('Descrição', max_length=200)
    status = models.CharField(max_length=11,choices=STATUS_CHOICES, blank=False, null=False)
    image = StdImageField(upload_to='static/img')
#arrumar imagem
    
    def __str__(self):
        return "{} - ({})".format(self.nome, self.descr)