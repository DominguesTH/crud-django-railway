from django.urls import path,include
from .views import login, cadastro

urlpatterns = [
    path('', login, name='url_login'),
    path('cadastro/', cadastro, name='url_cadastro'),
]
