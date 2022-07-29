from django.contrib import admin
from django.urls import path
from app.views import index, base, cadastro, ClientesCad, ClientesLista

app_name = 'app'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('', index),
    path('base.html', base),
    path('cadastro.html', cadastro),
    path('cadastro/', ClientesCad.as_view(), name='cadastro'),
    path('lista/', ClientesLista.as_view(), name='lista'),
]
