from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Carro, Reserva
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse

def enviar_email_teste(request):
    send_mail(
        subject='Teste de Email',
        message='Este é um teste usando o console do Django.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['teste@email.com'],
        fail_silently=False,
    )
    return HttpResponse("Email enviado (no console)")

# def solicitar_reserva(request, reserva_id):
#     reserva = get_object_or_404(Reserva, id=reserva_id)
#     # Buscando o gestor do setor do usuário que solicitou
#     gestor_email = reserva.usuario.perfil.setor.gestor.email
    
#     if gestor_email:
#         send_mail(
#             'Nova Solicitação de Reserva',
#             f'O funcionário {reserva.usuario.first_name} solicitou o carro {reserva.carro}.',
#             'sistema@empresa.com',
#             [gestor_email],
#             fail_silently=False,
#         )
#     # Lógica de feedback para o usuário...


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
    # agendamentos = Reserva.objects.all().order_by('data')
    agendamentos = Reserva.objects.filter(aprovada = True).order_by('dataSaida')
    return render(request, 'agenda/listar_agendamentos.html', {'agendamentos': agendamentos})

