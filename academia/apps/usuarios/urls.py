from django.urls import path
from .views import AdminLogin,AdminLogout
urlpatterns = [
    path('login/', AdminLogin.as_view(),name='login'),
    path('logout/', AdminLogout.as_view(),name='logout'),
]
