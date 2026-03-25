from django import forms
from .models import Reserva, Carro

# Classe para criar o formulário
class AgendamentoForm(forms.ModelForm):
    class Meta:
        # Diz a qual model esse formulário representa
        model = Reserva
        # Define os campos e a ordem
        fields = ['solicitante',  'data', 'carro', 'periodo']
        # Define o DateInput como um menu de seleção de datas
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        # Define os campos corretos para o banco
        labels = {
            'solicitante': 'Nome:',
            'carro': 'Carro',
            'data': 'Data',
            'periodo': 'Período',
        }