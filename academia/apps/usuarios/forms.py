from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UsuarioForm(UserCreationForm):
   
    
    class Meta:
        model = User
        fields = '__all__'

class FuncionarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','is_staff','is_active',"date_joined"]
        
