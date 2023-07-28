from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    return render(request, 'comum/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'comum/dashboard.html')
    else:
        return redirect('index')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            else:
                print('Falha na autenticação')
                return redirect('login')
        else:
            print('Email não cadastrado')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'comum/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')