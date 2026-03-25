from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Carro, Reserva

# def index(request):
#     carros = Carro.objects.all()
#     context = {
#         'carros': carros,
#         }
#     return render(request, 'agenda/index.html', context)

# def car_page(request):
#     print(carros)

#     return render(request, 'agenda/base.html', )

def home(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AgendamentoForm()

    return render(request, 'agenda/home.html', {'form': form})


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'agenda/listar_carros.html', {'carros': carros})

def listar_agendamentos(request):
    agendamentos = Reserva.objects.all().order_by('data')
    return render(request, 'agenda/listar_agendamentos.html', {'agendamentos': agendamentos})