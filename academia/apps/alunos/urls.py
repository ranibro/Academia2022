from django.urls import path
from .views import ExercicioCad, ExercicioListagem

app_name = 'alunos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('cadastro-treino/', ExercicioCad.as_view(), name='cadastro-treino'),
    path('exercicios/', ExercicioListagem.as_view(), name='exercicios')
]