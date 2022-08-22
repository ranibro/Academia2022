from django.urls import path
from .views import paginalogin, listaclientes

app_name = 'funcionarios'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('', paginalogin, name='login'),
    path('clientes/', listaclientes, name='clientes'),
#   path('cadastroDeFuncionario/', ClientesLista.as_view(), name='cadastroFunc'),
]