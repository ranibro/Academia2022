from .models import Treino, Clientes, Exercicio
from django import forms

class TreinoForm(forms.ModelForm):
    exercicios = forms.ModelMultipleChoiceField(queryset=Exercicio.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)
    alunos = forms.ModelMultipleChoiceField(queryset=Clientes.objects.all(),
                                            widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Treino
        fields = ['nome','exercicios','alunos','inicio']