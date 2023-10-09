from django.shortcuts import render
    
def Index (request):
    context={}
    if request.method == 'GET':
        pesquisa = request.GET.get('pesquisa')
        context['pesquisa'] = pesquisa 
        print(pesquisa, "get")       
    else:    
        pesquisa = request.POST.get('pesquisa')
        context['pesquisa'] = pesquisa
        print(pesquisa, "Post") 

    return render(request, 'cursos/exemplo.html', context)


def cadastro(request):
    titulo = "Pagina incial de Cadastros"
    return render(request,"cursos/cadastros.html", {'titulo':titulo })