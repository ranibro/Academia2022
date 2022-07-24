from django.shortcuts import render
from django.views.generic.edit import CreateView
from app.models import Clientes

#definir função para refernciar os templates em urls.
#return render(request, 'nomeDoTemplate')

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email']
    template_name = 'cadastros/cadastroCliente.html'


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def cadastro(request):
    return render(request, 'cadastros/cadastro.html')