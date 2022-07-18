from django.shortcuts import render

#definir função para refernciar os templates em urls.
#return render(request, 'nomeDoTemplate')
def index(request):
    return render(request, 'index.html')

def nf404(request):
    return render(request, '404.html')