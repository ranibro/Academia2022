from django.urls import reverse_lazy
from .models import Exercicio
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

class ExercicioCad(CreateView):
    model = Exercicio
    fields = ['equipamento', 'repeticao','carga', 'serie', 'tempo']
    template_name = 'cadastros/cadastroTreino.html'
    success_url = reverse_lazy('funcionarios:Exercicio')

class ExercicioListagem(ListView):
    login_url = reverse_lazy('login')
    model = Exercicio
    template_name = 'listas/listaExercicio.html'

class ExercicioUpdate(UpdateView):
    model = Exercicio
    fields = "__all__"
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('funcionarios:Exercicio')