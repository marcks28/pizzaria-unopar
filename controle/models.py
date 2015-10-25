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
