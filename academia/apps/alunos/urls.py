from django.urls import path
from .views import ClienteListagem, ClientesCad, ClientesUpdate

app_name = 'alunos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
  
#Base.html como é base não tem que ter um url?
 
#Se mecher aqui, tem que mecher no base.html também.
    path('cadastro-cliente/', ClientesCad.as_view(), name='CadastroCliente'),
    path('clientes/', ClienteListagem.as_view(), name='clientes'),
    path('listas/<int:pk>', ClientesUpdate.as_view() , name='listas'),    
]