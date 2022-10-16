from django.urls import path
from .views import AdminLogin,AdminLogout, UsuarioCreate
app_name = 'usuarios'

urlpatterns = [
    path('', AdminLogin.as_view(), name='login'),
    path('logout/', AdminLogout.as_view(), name='logout'),
    path('cadastrar/', UsuarioCreate.as_view(), name='sign-in')

]
