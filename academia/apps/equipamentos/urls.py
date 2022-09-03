from django.urls import path
from .views import EquipamentosLista, EquipamentoCad, EquipamentosUpdate, EquipamentosDelete
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.mixins import LoginRequiredMixin

app_name = 'equipamentos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
#Se mecher aqui, tem que mecher no base.html também.
   path('equipamentos/', EquipamentosLista.as_view(), name='equipamentos'),
   path('cadastro-equipamento/', EquipamentoCad.as_view(), name='cadastro-equipamento'),
   path('eq-update/<int:pk>', EquipamentosUpdate.as_view(), name='eq-update'),
   path('delete-eq/<int:pk>',EquipamentosDelete.as_view(),name='delete-eq')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 