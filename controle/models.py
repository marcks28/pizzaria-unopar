#encoding: utf-8
from django.db import models

class Produto(models.Model):
	nome = models.CharField(verbose_name='Nome',max_length=100)
	descricao = models.TextField(verbose_name=u'Descrição',max_length=255)
	opcao_choice = (
		('P','Pequena'),
		('M',u'Média'),
		('G','Grande'),
		('T',u'Família'),
	)
	tamanho = models.CharField(verbose_name='Tamanho',choices=opcao_choice,max_length=1)
	photo = models.ImageField(upload_to='controle/%Y/%m/%d',null=True,blank=True)
	preco = models.DecimalField(max_digits=6,decimal_places=2,verbose_name=u'Preço')
	destaque = models.BooleanField(default=False,verbose_name='Destaque')
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Produto'
		verbose_name_plural='Produtos'
		ordering = ['id']

class Cliente(models.Model):
	nome = models.CharField(verbose_name='Nome',max_length=100)
	data_nascimento = models.DateField(null=True,blank=True,verbose_name='Dt. Nasc')
	telefone = models.CharField(verbose_name='Telefone',max_length=14,unique=True)
	endereco = models.CharField(verbose_name=u'Endereço',max_length=255)
	referencia = models.CharField(verbose_name=u'Referência',max_length=255)
	choice_sexo = (
		('M','Masculino'),
		('F','Feminino'),
	)
	sexo = models.CharField(verbose_name='Sexo',choices=choice_sexo,max_length=1)
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
		ordering= ['nome']

class Empresa(models.Model):
	nome =models.CharField(verbose_name='Nome',max_length=50)
	cnpj = models.CharField(verbose_name='CNPJ',max_length=20,unique=True)
	telefone = models.CharField(verbose_name='Telefone',max_length=14)
	endereco = models.CharField(verbose_name=u'Endereço',max_length=100)
	email = models.EmailField(verbose_name='Email',null=True,blank=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural = 'Empresas'
		ordering = ['nome']

class Entregador(models.Model):
	nome = models.CharField(verbose_name='Nome',max_length=100)
	cpf = models.CharField(verbose_name='CPF',max_length=20,unique=True)
	rg = models.CharField(verbose_name='RG',max_length=20,unique=True)
	celular = models.CharField(verbose_name='Celular',max_length=14)
	empresa = models.ForeignKey(Empresa,related_name='Entregadores',verbose_name='Empresa')

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Entregador'
		verbose_name_plural='Entregadores'
		ordering = ['nome']

class Pedido(models.Model):
	create_on = models.DateTimeField(auto_now=True,verbose_name='Pedido realizado em')
	cliente = models.ForeignKey(Cliente,related_name='clientes_pedido',verbose_name='Cliente')
	produto = models.ForeignKey(Produto,related_name='prodtudo_pedido',verbose_name='Produto')
	quantidade = models.IntegerField(verbose_name='Quantidade')
	choice_pedido = (
		('PE','Pendente'),
		('EM',u'Em trânsito'),
		('CN','Cancelado'),
		('ET','Entregue'),
	)
	status = models.CharField(verbose_name='Status',choices=choice_pedido,default='PE',max_length=2)
	taxa_entrega = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='Taxa',default=3.50)

	def __str__(self):
		return str(self.create_on)

	def valor(self):
		return (self.quantidade * self.produto.preco) + self.taxa_entrega
	
	def  valor_Unit(self):
		return self.produto.preco

class Entrega(models.Model):
	created_on = models.DateTimeField(auto_now=True,verbose_name='Data entrega')
	entregador = models.ForeignKey(Entregador,related_name='entregadores',verbose_name='Entregadores')
	pedido = models.ForeignKey(Pedido,related_name='pedido',verbose_name='Pedido')
