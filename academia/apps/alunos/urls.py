from django.urls import path
from .views import ExercicioCad, ExercicioListagem, treinoCad

app_name = 'alunos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('cadastro-treino/', treinoCad, name="cadastro-treino"),
    path('cadastro-exercicio/', ExercicioCad.as_view(), name='cadastro-exercicio'),
    path('exercicios/', ExercicioListagem.as_view(), name='exercicios')
]