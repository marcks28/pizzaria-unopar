from django.contrib import admin
from .models import Produto,Cliente
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

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)