from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Equipamentos
from django.views.generic.list import ListView

# Create your views here.

# Não implementados
# Criar view pra equipamento.

class EquipamentoCad(CreateView):
    model = Equipamentos
    fields = ['nome', 'descr']
    template_name = 'cadastros/cadastroEquipamentos.html'

class EquipamentosLista(ListView):
    model = Equipamentos
    template_name = "listas/listaEquipamentos.html" 
