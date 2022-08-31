from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientesCad(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Clientes
    fields = ['nome', 'email','password','idade', 'altura','peso']
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')

class ClienteListagem(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'listas/listaClientes.html'

class ClientesUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Clientes
    fields = "__all__" 
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')