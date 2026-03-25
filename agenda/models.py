from django.db import models
from django.utils import timezone

# Create your models here.
# first_name (string), last_name (string), id (primary key)
# email (email), setor (string), modelo (string), marca (string)
# descrição (text)

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

    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, default="")
    solicitante = models.CharField(max_length=100)
    data = models.DateField()
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, default="")

    def __str__(self):
        return f'{self.solicitante} - {self.carro} em {self.data}'