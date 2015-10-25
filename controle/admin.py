from django.contrib import admin
from .models import Produto,Cliente,Empresa, Entregador
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

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Entregador,EntragadorAdmin)