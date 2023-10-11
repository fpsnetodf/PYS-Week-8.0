from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        print("estou aqui")
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
    if not senha == confirmar_senha:
        # mensagens
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem')

        return redirect('cadastro')
    if len(senha) < 6:
        messages.add_message(request, constants.WARNING, 'As senhas precisam ter no minimo 6 digitos')
        return redirect('cadastro')
    
    try:
    # Username deve ser único!
        user = User.objects.create_user(
        first_name=primeiro_nome,
        last_name=ultimo_nome,
        username=username,
        email=email,
        password=senha,
        )
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        
        return redirect ("login")
        
    except:
        return redirect('cadastro')
    
    # return redirect('cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            messages.add_message(request, constants.SUCCESS, "Você logou com sucesso")
            return redirect('index')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('login')
    
def index(request):
    return render(request, 'index.html')