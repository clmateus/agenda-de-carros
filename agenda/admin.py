from django.contrib import admin
from .models import Carro, Reserva

class ListandoCarros(admin.ModelAdmin):
    list_display = ("id", "modelo", "marca", "placa")
    list_display_links = ("id", "modelo")
    search_fields = ("modelo",)

class ListandoReservas(admin.ModelAdmin):
    list_display = ("id", "solicitante", "data", "periodo")
    list_display_links = ("id", "solicitante")

admin.site.register(Carro, ListandoCarros)
admin.site.register(Reserva, ListandoReservas)

# admin.site.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#    list_display = 'Registro'

# admin.site.register(Carro)


# @admin.register(models.Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = 'Registro'

# @admin.register(Estoque)
# class EstoqueAdmin(admin.ModelAdmin):
#     list_display = ['empresa', 'produto', 'saldo', 'reserva', 'conserto', 'data_conferencia', 'usuario_conferencia']

# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = 'desc','sku',

# @admin.register(TipoMovimentacao)
# class TipoMovimentacaoAdmin(admin.ModelAdmin):
#     list_display = ['nome']



# class PedidoAdmin(admin.ModelAdmin):
#     list_display = ['id','empresa','status','usuario_pedido']
    
# class PedidoProdutoInline(admin.TabularInline):
#     model = PedidoProduto
#     extra = 1

# class PedidosMultAdmin(admin.ModelAdmin):
#     inlines = [PedidoProdutoInline]

# admin.site.register(PedidoProduto)
# admin.site.register(Pedido, PedidosMultAdmin)

# class MovimentacaoAdmin(admin.ModelAdmin):
#     list_display = ['id']

# class MovimecacaoItemADM(admin.TabularInline):
#     model = MovimentacaoItem
#     extra = 1

# class MovMult(admin.ModelAdmin):
#     inlines = [MovimecacaoItemADM]

# admin.site.register(MovimentacaoItem)
# admin.site.register(Movimentacao, MovMult)



# class SaidaAdmin(admin.ModelAdmin):
#     list_display = '__all__'

# class SaidaItemADM(admin.TabularInline):
#     model = SaidaItem
#     extra = 1

# class saidaMult(admin.ModelAdmin):
#     inlines = [SaidaItemADM]

# admin.site.register(SaidaItem)
# admin.site.register(Saida, saidaMult)