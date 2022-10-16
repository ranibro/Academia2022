from .models import Treino, Clientes
from django import forms

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome','exercicio','aluno','inicio']
        
