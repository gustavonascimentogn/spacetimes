from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    data = {} #dicionario
    data['usuario'] = request.user
    #empresa = request.user.empregado.empresa
    #data['total_clientes'] = empresa.total_clientes
    #data['total_campanhas'] = empresa.total_campanhas
    #data['total_clientes_sem_pedidos'] = empresa.total_clientes_sem_pedido

    return render(request, 'core/index.html', data)




