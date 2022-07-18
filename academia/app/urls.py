from django.contrib import admin
from django.urls import path
from app.views import index, nf404

app_name = 'app'

#path('LinkNoNavegador', ReferenciaNoViews)
urlpatterns = [
    path('index.html', index),
    path('404.html', nf404),
]
