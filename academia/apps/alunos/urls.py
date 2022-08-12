from django.urls import path
from .views import index, base, cadastro, ClientesCad, ClientesLista #,EquipamentosLista, FuncionariosLista

app_name = 'alunos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('', index),
#Base.html como é base não tem que ter um url?
    path('base.html', base),
    path('cadastro', cadastro),
#Se mecher aqui, tem que mecher no base.html também.
    path('cadastroDeCliente/', ClientesCad.as_view(), name='CadastroCliente'),
    path('clientes/', ClientesLista.as_view(), name='clientes'),
]
