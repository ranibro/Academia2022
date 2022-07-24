from django.contrib import admin
from django.urls import path
from app.views import index, base, cadastro, ClientesCad

app_name = 'app'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('', index),
    path('base.html', base),
    path('cadastro.html', cadastro),
    path('cadastroCliente.html', ClientesCad.as_view(), name="Cliente_Cadastro" ),
]
