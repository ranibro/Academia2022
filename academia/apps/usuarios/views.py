from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm

# Create your views here.
class AdminLogin(LoginView):
    template_name = 'login/loginAdm.html'
    
class AdminLogout(LogoutView):
    template_name = 'login/loginAdm.html'
    
class UsuarioCreate (CreateView):
    template_name= "sign/sign-in.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:login")

    

 