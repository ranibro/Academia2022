from django.urls import path
from .views import AdminLogin,AdminLogout
urlpatterns = [
    path('login-adm/', AdminLogin.as_view(),name='login'),
    path('logout-adm/', AdminLogout.as_view(),name='logout'),
]
