from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TiposExames
from django.http import HttpResponse




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
    