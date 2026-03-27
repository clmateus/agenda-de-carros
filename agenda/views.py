from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendamentoForm, VeiculoForm
from .models import Veiculo, Reserva
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def enviar_email_teste(remetente, mensagem):
    send_mail(
        subject='Teste de Email',
        message='Parabéns, sua reserva foi confirmada!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[remetente],
        fail_silently=False,
    )
    return HttpResponse("Email enviado (no console)")

@login_required
def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.solicitante = request.user.get_full_name() or request.user.username
            agendamento.save()

            # ✅ Envia e-mail de confirmação para o usuário logado
            enviar_email_teste(request.user.email)

            return redirect('agendamento')
    else:
        nome_logado = request.user.get_full_name() or request.user.username
        form = AgendamentoForm(initial={'solicitante': nome_logado})

    return render(request, 'agenda/agendamento.html', {'form': form})

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
        enviar_email_teste(request.user.email) 
        messages.success(request, 'Aprovado')
    elif acao == 'negar':
        reserva.delete()
        messages.warning(request, 'Negado')

    return redirect('solicitacoes')

@login_required
def veiculos(request):
    veiculos = Veiculo.objects.filter(status = True)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('veiculos')
    else:
        form = VeiculoForm()

    return render(request, 'agenda/veiculos.html', {'veiculos': veiculos, 'form': form})

def remover_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    veiculo.delete()
    return redirect('veiculos')

def editar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        # PRIMEIRO - Checa se o usuário quer remover a foto
        if 'foto-clear' in request.POST:
            if veiculo.foto:
                veiculo.foto.delete(save=False)
                veiculo.foto = None

        # SEGUNDO - Tenta salvar as outras alterações
        form = VeiculoForm(request.POST, request.FILES, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo atualizado com sucesso!')
            return redirect('veiculos')
        else:
            messages.error(request, 'Erro ao atualizar o veículo. Verifique os dados informados.')
    else:
        form = VeiculoForm(instance=veiculo)
    
    return render(request, 'agenda/editar_veiculo.html', {'form': form, 'veiculo': veiculo})