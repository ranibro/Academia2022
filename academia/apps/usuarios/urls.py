from django.urls import path
from .views import AdminLogin, FuncionarioCreate, UsuarioCreate
from django.contrib.auth import views as auth_views
app_name = 'usuarios'

urlpatterns = [
   
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro-cliente/', UsuarioCreate.as_view(), name='cadastro-cliente'),
    path('cadastrar-funcionario/', FuncionarioCreate.as_view(), name="cadastro-funcionario")
]
