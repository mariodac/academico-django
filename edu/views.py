from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Matricula
from django.utils import timezone

# Create your views here.
def index(request):
    matriculas = Matricula.objects.all()
    
    dados = {
        'matriculas': matriculas
    }
    return render(request, 'index.html', dados)


def edu(request, matricula_id):
    matricula = get_object_or_404(Matricula, pk=matricula_id)
    data_acesso = timezone.now()
    matricula_a_exibir = {
        'matricula':matricula,
        'data_acesso': data_acesso
    }
    return render(request, 'matricula.html', matricula_a_exibir)
