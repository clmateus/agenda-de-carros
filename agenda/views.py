from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from .models import Carro, Reserva
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def enviar_email_teste(remetente):
    send_mail(
        subject='Teste de Email',
        message='Este é um teste usando o console do Django.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[remetente],
        fail_silently=False,
    )
    return HttpResponse("Email enviado (no console)")

@login_required
def home(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            enviar_email_teste(request.user.email)
            return redirect('home')
    else:
        form = AgendamentoForm()

    return render(request, 'agenda/home.html', {'form': form})


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'agenda/listar_carros.html', {'carros': carros})

@login_required
def listar_agendamentos(request):
    # agendamentos = Reserva.objects.all().order_by('data')
    agendamentos = Reserva.objects.filter(aprovada = True).order_by('dataSaida')
    return render(request, 'agenda/listar_agendamentos.html', {'agendamentos': agendamentos})