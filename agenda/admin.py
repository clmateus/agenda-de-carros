from django.contrib import admin
from .models import Veiculo, Reserva

class ListandoVeiculos(admin.ModelAdmin):
    list_display = ("id", "modelo", "marca", "placa", "tipo", "status")
    list_display_links = ("id", "modelo")
    search_fields = ("modelo",)
    list_filter = ("modelo",)

class ListandoReservas(admin.ModelAdmin):
    list_display = ("id", "solicitante", "horarioSolicitacao", "dataSaida", "dataEntrega", "destino", "aprovada",)
    list_display_links = ("id", "solicitante", )
    list_editable = ("aprovada", )
    search_fields = ("solicitante",)

admin.site.register(Veiculo, ListandoVeiculos)
admin.site.register(Reserva, ListandoReservas)