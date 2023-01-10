from django.shortcuts import render
from .models import Pessoa
import datetime
from django.contrib.auth.decorators import login_required


def home(request):
  return render(request, 'core/home.html')

@login_required
def horario(request):
  data =  {} 
  data['transações'] = ['t1','t2', 't3']
  data['now'] = datetime.datetime.now()
  return render(request, 'core/horario.html', data)


def salvar(request):
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})