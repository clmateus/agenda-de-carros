from django import forms
from .models import Reserva, Carro
from django.utils import timezone

# Classe para criar o formulário
class AgendamentoForm(forms.ModelForm):
    class Meta:
        # Diz a qual model esse formulário representa
        model = Reserva
        # Define os campos e a ordem
        fields = ['solicitante', 'dataSaida', 'dataEntrega', 'periodo']
        # Define os atributos para o HTML
        widgets = {
            'solicitante': forms.TextInput(attrs={'class': 'form-control', 'value': 'aaa', 'readonly': 'readonly'}),
            'dataSaida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': timezone.now().date().isoformat()}),
            'dataEntrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': timezone.now().date().isoformat()}),
            'periodo': forms.Select(attrs={'class': 'form-select'})
        }
        # Define os campos corretos para o banco
        labels = {
            'solicitante': 'Nome:',
            'dataSaida': 'Data de Saída:',
            'dataEntrega': 'Data de Entrega:',
            'periodo': 'Período:',
        }