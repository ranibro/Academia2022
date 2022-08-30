from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class AdminLogin(LoginView):
    template_name = 'login/loginAdm.html'
    
class AdminLogout(LogoutView):
    template_name = 'login/loginAdm.html'
