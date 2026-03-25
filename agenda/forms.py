from django import forms
from .models import Reserva, Carro

# Classe para criar o formulário
class AgendamentoForm(forms.ModelForm):
    class Meta:
        # Diz a qual model esse formulário representa
        model = Reserva
        # Define os campos e a ordem
        fields = ['solicitante', 'dataSaida', 'dataEntrega', 'periodo']
        # Define os atributos para o HTML
        widgets = {
            'solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'dataSaida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dataEntrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-select'})
        }
        # Define os campos corretos para o banco
        labels = {
            'solicitante': 'Nome:',
            'dataSaida': 'Data de Saída:',
            'dataEntrega': 'Data de Entrega:',
            'periodo': 'Período:',
        }