from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.
# first_name (string), last_name (string), id (primary key)
# email (email), setor (string), modelo (string), marca (string)
# descrição (text)

def validar_data_futura(value):
    if value < timezone.now().date():
        raise ValidationError('A data não pode ser anterior a hoje.')
    
class Veiculo(models.Model):
    TIPO_VEICULO_CHOICES = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('caminhonete', 'Caminhonete')
    ]

    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    placa = models.CharField(max_length=7, unique=True)
    tipo = models.CharField(choices=TIPO_VEICULO_CHOICES, default='')
    status = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='veiculos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'
    
    def checa_rodizio(self, data_checar):
        # Se não for passada uma data, não é possível checar. Retorna True.
        if not data_checar:
            return True

        final_placa = self.placa[-1]
        # Pega o dia da semana (0=Segunda, 1=Terça, ..., 6=Domingo)
        dia_da_semana = data_checar.weekday()

        # Rodízio não se aplica em fins de semana
        if dia_da_semana > 4: # 5=Sábado, 6=Domingo
            return True

        rodizio = {
            0: ['1', '2'], # Segunda-feira
            1: ['3', '4'], # Terça-feira
            2: ['5', '6'], # Quarta-feira
            3: ['7', '8'], # Quinta-feira
            4: ['9', '0'], # Sexta-feira
        } 

        placas_proibidas = rodizio.get(dia_da_semana, [])
        
        return final_placa not in placas_proibidas
    
class Reserva(models.Model):
    PERIODO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('dia_inteiro', 'Dia Inteiro')
    ]

    solicitante = models.CharField(max_length=100)
    dataSaida = models.DateField(blank=False, default=datetime.now, validators=[validar_data_futura])
    dataEntrega = models.DateField(validators=[validar_data_futura])
    horarioSolicitacao = models.DateTimeField(auto_now=True)
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, default="")
    aprovada = models.BooleanField(default=False)

    veiculo = models.ForeignKey('Veiculo', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Veículo')

    status_escolha = (
        'P', 'Pendente',
        'A', 'Aprovado',
        'R', 'Recusado'
    )

    def __str__(self):
        return f'{self.solicitante} - em {self.dataSaida}'