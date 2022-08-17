from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
#Implementar model para cadastro de equip e funcionários, depois disso
#Implementar view para cadastro de equip e de funcionários, depois disso
#Criar url para o template de lista do equip e funcionário, que não estão prontos ainda.

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email','password','idade', 'altura','peso']
    template_name = 'cadastros/cadastroCliente.html'
#Tirar esse redirect aqui, no lugar disso usar uma caixa de texto de alerta
    success_url = reverse_lazy('alunos:clientes')

def verificacao(request):
    try:
       if request.session["id"]: 
           return True
    except:
        return False
 
def login(request):
    if verificacao(request):
        return HttpResponseRedirect('/')
    
    template_name = 'login/login.html'
    error_message = None
    
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        if Clientes.objects.filter(email = email).exists():
            if Clientes.objects.filter(email = email, senha = senha).exists():
            
                usuario = Clientes.objects.get(email = email, senha = senha)
            
                request.session['email'] = usuario.email
                request.session['nome'] = usuario.nome
                request.session['id'] = usuario.id

                return HttpResponseRedirect('/')
            else:
                error_message = "Senha de acesso incorreta!"
                return TemplateResponse(request, template_name, locals())
        else:
            error_message = "E-mail inválido ou não encontrado!"
            return TemplateResponse(request, template_name, locals())
    else:
        return TemplateResponse(request, template_name, locals())


class ClienteListagem(ListView):
    model = Clientes
    template_name = 'listas/listaClientes.html'


class ClientesUpdate(UpdateView):
    model = Clientes
    fields = "__all__" 
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')