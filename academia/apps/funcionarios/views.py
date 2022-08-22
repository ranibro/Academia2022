from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def listaclientes(request):
    if request.user.is_authenticated:
        return redirect('alunos:ClienteListagem')
    else:
        return redirect(paginalogin)

def paginalogin(request):
    if request.user.is_authenticated:
        return redirect('alunos:ClienteListagem')
    else:
        if request.method == "POST":
            email = request.POST.get('InputEmail') #'InputEmail' in request.POST
            senha = request.POST.get('InputPassword')#'InputPassword' in request.POST

            user = authenticate(username=email, password=senha)
            if user is not None:
                login(request, user)
                #colocar backend?
                return redirect('alunos:ClienteListagem')
            else:
                messages.error(request, "Usuario ou senha invalidos!")
                return render(request, '../templates/login/login.html')
        else:
            return render(request, '../templates/login/login.html')