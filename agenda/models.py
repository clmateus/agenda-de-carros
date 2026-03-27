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

    def __str__(self):
        return f'{self.solicitante} - em {self.dataSaida}'