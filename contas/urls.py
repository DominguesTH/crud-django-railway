from django.contrib import admin
from django.urls import path
from .views import listagem


urlpatterns = [
    path('', listagem , name='listagem' ),  
]
