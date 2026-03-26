from django.contrib import admin
from .models import Carro, Reserva

class ListandoCarros(admin.ModelAdmin):
    list_display = ("id", "modelo", "marca", "placa")
    list_display_links = ("id", "modelo")
    search_fields = ("modelo",)
    list_filter = ("modelo",)

class ListandoReservas(admin.ModelAdmin):
    list_display = ("id", "solicitante", "horarioSolicitacao", "dataSaida", "dataEntrega", "periodo", "aprovada",)
    list_display_links = ("id", "solicitante", )
    list_editable = ("aprovada", )
    search_fields = ("solicitante",)

admin.site.register(Carro, ListandoCarros)
admin.site.register(Reserva, ListandoReservas)