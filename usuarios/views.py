from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        url = request.GET.get("valor")
        print(url)
        return render(request, 'usuarios/cadastro.html',{'get': url})
    if request.method == "POST":        
        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        email = request.POST.get("email")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As Senhas não coincidem')
            return redirect("cadastro")
        
        if len(senha) < 8:
            messages.add_message(request, constants.INFO, "A Senha precisa ter 8 ou mais dígitos")
            return redirect("cadastro")
            

        try:
            user = User.objects.create_user(
            first_name = primeiro_nome,
            last_name = ultimo_nome,
            username = username, 
            password = confirmar_senha,
            email = email,          
        ) 
            messages.add_message(request, constants.SUCCESS, "Cadastro Realizado com Sucesso!!!")
            user.save()  
        except:
            messages.add_message(request, constants.WARNING, "Erro Inesperado")
                   
        messages.add_message(request, constants.INFO, "Dados Validados com sucesso!!")
        return render (request,'usuarios/cadastro.html', {'list':[primeiro_nome, ultimo_nome, username, senha, email, confirmar_senha]} )


def login(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    
    if request.method == "POST":
        username = request.POST.get("usuario")
        senha = request.POST.get("senha")
        usuario =  User()
        usuario(username, senha)
        
        
