from django.urls import path
from .views import EquipamentosLista

app_name = 'equipamentos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
#Se mecher aqui, tem que mecher no base.html também.
   path('equipamentos/', EquipamentosLista.as_view(), name='equipamentos'),
#   path('cadastroDeEquipamento/', ClientesLista.as_view(), name='cadastroEquip'),
]
