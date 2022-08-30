from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from ...apps.equipamentos.models import Equipamentos
from django.views.generic.list import ListView
from django import template
register=template.Library()
# Create your views here.

# Não implementados
# Criar view pra equipamento.

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
    
def equip_list(request):
    context = {
        'equipamentos': Equipamentos.objects.all()
    }
    return render(request, 'filme_list.html', context)

def get_context_data(self, **kwargs):
    context = super(Equipamentos).get_context_data(**kwargs)
    context['top_three_images'] = [
        product.Image.url
        for product in Equipamentos.objects.exclude(Image=None)[:3]
    ]
    return context