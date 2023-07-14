from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    dados_dos_institutos = {
        'IF Goiano': 'Goiás',
        'IFSP' : 'São Paulo',
        'IFMG' : 'Minas Gerais',
    }
    dados = {
        'dados_dos_institutos': dados_dos_institutos
    }
    return render(request, 'index.html', dados)

def cadastro(request):
    return render(request, 'cadastro.html')
