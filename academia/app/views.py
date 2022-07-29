from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes
from django.views.generic.list import ListView


class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email','password','idade', 'altura','peso']
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('app:lista')

class ClientesLista(ListView):
    model = Clientes
    template_name = "listas/listaClientes.html" 

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def cadastro(request):
    return render(request, 'cadastros/cadastro.html')