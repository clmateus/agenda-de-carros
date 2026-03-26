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

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    email= models.EmailField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f'Nome: {self.first_name} {self.last_name} | Setor: {self.setor} | E-mail: {self.email}'
    
class Carro(models.Model):
    marca = models.CharField(max_length=20, null=True, blank=True, default=None)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    placa = models.CharField(max_length=7, null=True, blank=True, unique=True)
    observacao = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'
    
class Reserva(models.Model):
    PERIODO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('dia_inteiro', 'Dia Inteiro')
    ]

    # carro = models.ForeignKey(Carro, on_delete=models.CASCADE, default="")
    solicitante = models.CharField(max_length=100)
    dataSaida = models.DateField(blank=False, default=datetime.now, validators=[validar_data_futura])
    dataEntrega = models.DateField(validators=[validar_data_futura])
    horarioSolicitacao = models.DateTimeField(auto_now=True)
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, default="")
    aprovada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.solicitante} - em {self.dataSaida}'