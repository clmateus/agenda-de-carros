from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendamentoForm
from .models import Carro, Reserva
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            # 1. Criar o objeto sem salvar no banco
            agendamento = form.save(commit=False)
            
            # 2. Forçar o campo 'solicitante' a ser o usuário logado
            agendamento.solicitante = request.user.get_full_name() or request.user.username
            
            # 3. Salva o banco de dados
            agendamento.save()
            
            return redirect('home')
    else:
        # 4. Guarda o nome de quem está logado
        nome_logado = request.user.get_full_name() or request.user.username
        
        # 5. Criar o formulário já com o nome preenchido no campo 'solicitante'
        form = AgendamentoForm(initial={'solicitante': nome_logado})

    return render(request, 'agenda/home.html', {'form': form})


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'agenda/listar_carros.html', {'carros': carros})

@login_required
def listar_agendamentos(request):
    # agendamentos = Reserva.objects.all().order_by('data')
    agendamentos = Reserva.objects.filter(aprovada = True).order_by('dataSaida')
    return render(request, 'agenda/listar_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def solicitacoes(request):
    solicitacoes = Reserva.objects.filter(aprovada = False).order_by('horarioSolicitacao')
    return render(request, 'agenda/solicitacoes.html', {'solicitacoes': solicitacoes})

def responder_solicitacao(request, id, acao):
    reserva = get_object_or_404(Reserva, id=id)

    if acao == 'aprovar':
        reserva.aprovada = True
        reserva.save()
        messages.success(request, 'Aprovado')
    elif acao == 'negar':
        reserva.delete()
        messages.warning(request, 'Negado')

    return redirect('solicitacoes')