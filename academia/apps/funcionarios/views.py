from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin
from apps.alunos.models import Clientes


def paginalogin(request):
    if request.user.is_authenticated:
        return redirect('funcionarios:clientes')
    else:
        if request.method == "POST":
            email = request.POST.get('InputEmail')
            senha = request.POST.get('InputPassword')

            user = authenticate(username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('funcionarios:clientes')
            else:
                messages.error(request, "Usuario ou senha invalidos!")
                return render(request, '../templates/login/login.html')
        else:
            return render(request, '../templates/login/login.html')

class ClientesCad( CreateView):
    model = Clientes
    fields = ['nome', 'email','password']
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('funcionarios:clientes')

class ClienteListagem(LoginRequiredMixin,ListView):
    group_required = [u"Funcionario", u"Adminstrador"]
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'listas/listaClientes.html'

class ClientesUpdate(UpdateView):
    # group_required = u"Funcionario"
    # login_url = reverse_lazy('login')
    model = Clientes
    fields = "__all__"
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('funcionarios:clientes')