# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('data_nascimento', models.DateField(null=True, verbose_name='Dt. Nasc', blank=True)),
                ('telefone', models.CharField(unique=True, verbose_name='Telefone', max_length=14)),
                ('endereco', models.CharField(verbose_name='Endereço', max_length=255)),
                ('referencia', models.CharField(verbose_name='Referência', max_length=255)),
                ('sexo', models.CharField(verbose_name='Sexo', max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(verbose_name='Nome', max_length=50)),
                ('cnpj', models.CharField(unique=True, verbose_name='CNPJ', max_length=20)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=14)),
                ('endereco', models.CharField(verbose_name='Endereço', max_length=100)),
                ('email', models.EmailField(null=True, verbose_name='Email', max_length=254, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
                'verbose_name': 'Empresa',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=20)),
                ('rg', models.CharField(unique=True, verbose_name='RG', max_length=20)),
                ('celular', models.CharField(verbose_name='Celular', max_length=14)),
                ('empresa', models.ForeignKey(to='controle.Empresa', related_name='Entregadores', verbose_name='Empresa')),
            ],
            options={
                'verbose_name_plural': 'Entregadores',
                'verbose_name': 'Entregador',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_on', models.DateTimeField(auto_now=True, verbose_name='Pedido realizado em')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('status', models.CharField(max_length=2, verbose_name='Status', default='PE', choices=[('PE', 'Pendente'), ('EM', 'Em trânsito'), ('CN', 'Cancelado'), ('ET', 'Entregue')])),
                ('taxa_entrega', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Taxa', default=3.5)),
                ('cliente', models.ForeignKey(to='controle.Cliente', related_name='clientes_pedido', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('descricao', models.TextField(verbose_name='Descrição', max_length=255)),
                ('tamanho', models.CharField(verbose_name='Tamanho', max_length=1, choices=[('P', 'Pequena'), ('M', 'Média'), ('G', 'Grande'), ('T', 'Família')])),
                ('photo', models.ImageField(upload_to='controle/%Y/%m/%d', null=True, blank=True)),
                ('preco', models.DecimalField(max_digits=6, verbose_name='Preço', decimal_places=2)),
                ('destaque', models.BooleanField(verbose_name='Destaque', default=False)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(to='controle.Produto', related_name='prodtudo_pedido', verbose_name='Produto'),
        ),
    ]
