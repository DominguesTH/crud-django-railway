from django.contrib import admin
from django.urls import path
from .views import home, horario


urlpatterns = [
    path('home', home , name='home' ), 
    path('horario', horario, name='horario' ),     
]
