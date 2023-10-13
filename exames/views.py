from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExames, SolicitacaoExame
from django.http import HttpResponse
from datetime import datetime
from django.contrib.messages import constants
from django.contrib import messages




@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()
    
    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    elif request.method == "POST":
        # tipos_exames = TiposExames.objects.all()
        exames_id = request.POST.getlist("exames")
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        preco = 0
        for exame in solicitacao_exames:
            if exame.disponivel:
                preco += exame.preco
        
        exames = request.POST.getlist('exames')


        return render (request, "solicitar_exames.html", {"tipos_exames":tipos_exames, "solicitacao_exames" : solicitacao_exames, "preco":preco})

def fechar_pedido(request):
    if request.method == "GET":
        return HttpResponse("estou GET do pedidos_exames")
    if request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        pedidos_exames = PedidosExames(
            usuario = request.user,
            data = datetime.now()
        )  
        pedidos_exames.save()  

        for exame in solicitacao_exames:
            solicitacao_exames_temp = SolicitacaoExame(
                usuario = request.user, 
                exame = exame, 
                status = 'E'
            )
            solicitacao_exames_temp.save()
            pedidos_exames.exames.add(solicitacao_exames_temp)

        pedidos_exames.save()
        messages.add_message(request, constants.SUCCESS, "Pedidos Salvos com sucesso")

        return redirect("gerenciar_pedidos")
    

@login_required
def gerenciar_pedidos(request):
    pedidos_exames = PedidosExames.objects.filter(usuario=request.user)
    return render(request, 'gerenciar_pedidos.html', {'pedidos_exames': pedidos_exames})



@login_required
def cancelar_pedido(request, pedido_id):
    pedido = PedidosExames.objects.get(id=pedido_id)
    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pedido não é seu')
        return redirect('gerenciar_pedidos')
    
    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pedido não é seu')
        return redirect('gerenciar_pedidos')
    
    pedido.agendado = False
    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido excluido com sucesso')
    return redirect('gerenciar_pedidos')
