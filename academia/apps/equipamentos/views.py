from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from .models import Equipamentos
from django.views.generic.list import ListView

class EquipamentoCad(CreateView):
    model = Equipamentos
    fields = '__all__'
    template_name = 'cadastros/cadastroEquipamentos.html'
    success_url = reverse_lazy('equipamentos:equipamentos')


class EquipamentosLista(ListView):
    model = Equipamentos
    template_name = "listas/listaEquipamentos.html" 


class EquipamentosUpdate(UpdateView):
    model = Equipamentos
    fields = '__all__'
    template_name = 'cadastros/cadastroEquipamentos.html'
    success_url = reverse_lazy('equipamentos:equipamentos')


class EquipamentosDelete(DeleteView):
    model = Equipamentos
    template_name = 'listas/listaEquipamentos.html'
    success_url = reverse_lazy('equipamentos:equipamentos')
    

