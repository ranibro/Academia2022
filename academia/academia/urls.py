from django.contrib import admin
from django.urls import path, include
from apps.usuarios.views import AdminLogin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.alunos.urls')),
    path('', include('apps.equipamentos.urls')),
    path('', include('apps.funcionarios.urls')),
    path('', include('apps.usuarios.urls')),
    path('', AdminLogin.as_view(), name='login'),


]