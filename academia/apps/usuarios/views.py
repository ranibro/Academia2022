from lib2to3.pgen2.token import GREATER
from tokenize import group
from unittest import mock
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm, FuncionarioForm
from django.contrib.auth.models import  Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import User

# Create your views here.
class AdminLogin(LoginView):
    template_name = 'login/loginAdm.html'


class UsuarioCreate ( CreateView):
    #group_required = [u"Funcionario"]
    #login_url = reverse_lazy('login')
    template_name= "cadastros/cadastroCliente.html"
    model = User
    success_url = reverse_lazy("listas/listaClientes.html")
    fields = ["username",'first_name', 'last_name','email','password']
    forms = FuncionarioForm()
    def form_valid(self, form):
        
        grupo = get_object_or_404(Group, name="Alunos")
        
        self.object.groups.add(grupo)
        self.object.save()
        
        return super().form_valid(form)

class FuncionarioCreate ( LoginRequiredMixin,CreateView):
    #group_required = [u"Administrador"]
    login_url = reverse_lazy('login')
    template_name = "cadastros/cadastroFuncionario.html "
    forms = FuncionarioForm()
    success_url = reverse_lazy("funcionarios:funcionarios")
    
    def form_valid(self, form):
        
        grupo = Group.objects.get(name='Funcionarios') 
        grupo.user_set.add( self.object)
       
  
        
        return super().form_valid(form)


 