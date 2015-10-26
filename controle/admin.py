from django.contrib import admin
from .models import Produto,Cliente,Empresa, Entregador, Pedido
# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
	model = Produto
	list_display = ('nome','preco',)
	list_filter = ['tamanho']
	search_fields = ['nome']

class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	list_display = ('nome','telefone',)
	list_filter = ['sexo']
	search_fields = ['nome','telefone']

class EmpresaAdmin(admin.ModelAdmin):
	model = Empresa
	list_display = ('cnpj','nome','telefone','email',)
	search_fields = ['nome','cnpj']
		
class EntragadorAdmin(admin.ModelAdmin):
	model = Entregador
	list_display = ('cpf','nome','celular',)
	list_filter = ['empresa']
	search_fields = ['nome']

class PedidoAdmin(admin.ModelAdmin):
	model= Pedido
	list_display = ('create_on','cliente','produto','valor_Unit','quantidade','taxa_entrega','valor',)
	list_filter = ['status']
	search_fields = ['cliente']
		
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Entregador,EntragadorAdmin)
admin.site.register(Pedido,PedidoAdmin)