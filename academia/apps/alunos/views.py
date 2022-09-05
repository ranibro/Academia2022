from django.urls import reverse_lazy
from .models import Exercicio
from django.views.generic.edit import CreateView

class ExercicioCad(CreateView):
    login_url = reverse_lazy('login')
    model = Exercicio
    fields = ['equipamento', 'repeticao','carga', 'serie', 'tempo']
    template_name = 'cadastros/cadastroTreino.html'