from django.urls import path
from .views import home, horario


urlpatterns = [
    path('', home , name='url_home' ), 
    path('horario/', horario, name='url_horario' ),     
]
