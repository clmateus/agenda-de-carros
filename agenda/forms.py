from django import forms
from .models import Reserva, Veiculo
from django.utils import timezone

# Classe para criar o formulário
class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            now_for_input = timezone.now().strftime('%Y-%m-%dT%H:%M')
            self.initial['dataSaida'] = now_for_input
            self.fields['dataSaida'].widget.attrs['min'] = now_for_input
            self.fields['dataEntrega'].widget.attrs['min'] = now_for_input

    class Meta:
        # Diz a qual model esse formulário representa
        model = Reserva
        # Define os campos e a ordem
        fields = ['solicitante', 'dataSaida', 'dataEntrega', 'destino']
        # Define os atributos para o HTML
        widgets = {
            'solicitante': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dataSaida': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'dataEntrega': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # Define os campos corretos para o banco
        labels = {
            'solicitante': 'Nome:',
            'dataSaida': 'Data de Saída:',
            'dataEntrega': 'Previsão de Entrega:',
            'destino': 'Destino:',
        }        

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'placa', 'tipo', 'foto']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control',}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'marca': 'Marca:',
            'modelo': 'Modelo:',
            'placa': 'Placa:',
            'tipo': 'Tipo do veículo:',
            'foto': 'Foto do veículo:',
        }