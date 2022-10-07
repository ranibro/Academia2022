from django.urls import path
from .views import  ClientesCad, ClienteListagem, ClientesUpdate

app_name = 'funcionarios'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('cadastro-cliente/', ClientesCad.as_view(), name='cadastro-cliente'),
    path('clientes/', ClienteListagem.as_view(), name='clientes'),
    path('update/<int:pk>', ClientesUpdate.as_view(), name='update'),
]