from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Exercicio, Treino
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import TreinoForm

def treinoCad(request):
   form = TreinoForm
   context = {'form':form}
   return render(request, 'cadastroTreino.html', context)

class ExercicioCad(CreateView):
    model = Exercicio
    fields = ['equipamento', 'repeticao', 'serie', 'carga', 'tempo']
    template_name = 'cadastros/cadastroExercicio.html'
    success_url = reverse_lazy('alunos:exercicios')

class ExercicioListagem(ListView):
    login_url = reverse_lazy('login')
    model = Exercicio
    template_name = 'listas/listaExercicio.html'

class ExercicioUpdate(UpdateView):
    model = Exercicio
    fields = "__all__"
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:exercicios')