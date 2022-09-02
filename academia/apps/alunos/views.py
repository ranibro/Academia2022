from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin 

class ClientesCad(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"Funcionario"
    login_url = reverse_lazy('login')
    model = Clientes
    fields = ['nome', 'email','password']
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')

class ClienteListagem(LoginRequiredMixin,ListView):
    group_required = [u"Funcionario", u"Adminstrador"]
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'listas/listaClientes.html'

class ClientesUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = u"Funcionario"
    login_url = reverse_lazy('login')
    model = Clientes
    fields = "__all__" 
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')