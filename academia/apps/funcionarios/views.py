from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

def listaclientes(request):
    if request.user.is_authenticated:
        return redirect('alunos:clientes')
    else:
        return redirect(paginalogin)

def paginalogin(request):
    if request.user.is_authenticated:
        return redirect('alunos:clientes')
    else:
        if request.method == "POST":
            email = request.POST.get('InputEmail')
            senha = request.POST.get('InputPassword')

            user = authenticate(username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('alunos:clientes')
            else:
                messages.error(request, "Usuario ou senha invalidos!")
                return render(request, '../templates/login/login.html')
        else:
            return render(request, '../templates/login/login.html')