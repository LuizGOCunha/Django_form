from django.shortcuts import render
from formulario.forms import OnibusForms
# Create your views here.


# Esse index irá criar um campo de formulário com base nas características de OnibusForm
# Instanciando o objeto em form, então explicitando seu conteudo e sua chave em um contexto
# Então se retorna um render passando como argumento o request, explicitando o html, e entregando o contextoa ser usado
def index(request):
    form = OnibusForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao(request):
    if request.method == 'POST':
        form = OnibusForms(request.POST)
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'revisao.html', contexto)
        else:
            contexto = {'form':form}
            print('Caractere invalido')
            return render(request, 'index.html', contexto)