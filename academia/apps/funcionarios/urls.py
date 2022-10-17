from django.urls import path
from .views import   ClienteListagem, ClientesUpdate, FuncionarioLista

app_name = 'funcionarios'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('clientes/', ClienteListagem.as_view(), name='clientes'),
    path('update/<int:pk>', ClientesUpdate.as_view(), name='update'),
    path('funcionarios/', FuncionarioLista.as_view(),name='funcionarios' )
]