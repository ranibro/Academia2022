from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('alunos/', include('apps.alunos.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.alunos.urls')),
    path('', include('apps.equipamentos.urls')),
    path('', include('apps.funcionarios.urls')),

]