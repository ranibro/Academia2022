from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes #, Equipamentos, Funcionarios
from django.views.generic.list import ListView

#Implementar model para cadastro de equip e funcionários, depois disso
#Implementar view para cadastro de equip e de funcionários, depois disso
#Criar url para o template de lista do equip e funcionário, que não estão prontos ainda.

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email','password','idade', 'altura','peso']
    template_name = 'cadastros/cadastroCliente.html'
#Tirar esse redirect aqui, no lugar disso usar uma caixa de texto de alerta
    success_url = reverse_lazy('alunos:lista')

class ClientesLista(ListView):
    model = Clientes
    template_name = "listas/listaClientes.html"


#Não implementados
#Criar view pra funcionário e equipamento.
'''
class EquipamentosLista(ListView):
    model = Equipamentos
    template_name = "listas/listaEquipamentos.html" 
    
class FuncionariosLista(ListView):
    model = Funcionarios
    template_name = "listas/listaFuncionarios.html" 
    
'''

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def cadastro(request):
    return render(request, 'cadastros/cadastro.html')