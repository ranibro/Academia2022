from django.urls import path
from .views import ExercicioCad

app_name = 'alunos'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('cadastro-treino/', ExercicioCad.as_view(), name='CadastroTreino')
]