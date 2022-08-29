from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,  UpdateView
from .models import Clientes
from django.views.generic.list import ListView

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email','password','idade', 'altura','peso']
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')

def verificacao(request):
    try:
       if request.session["id"]: 
           return True
    except:
        return False

class ClienteListagem(ListView):
    model = Clientes
    template_name = 'listas/listaClientes.html'


class ClientesUpdate(UpdateView):
    model = Clientes
    fields = "__all__" 
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('alunos:clientes')