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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_nascimento', models.DateField(null=True, blank=True, verbose_name='Dt. Nasc')),
                ('telefone', models.CharField(max_length=14, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('referencia', models.CharField(max_length=255, verbose_name='Referência')),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Sexo')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=255, verbose_name='Descrição')),
                ('tamanho', models.CharField(max_length=1, choices=[('P', 'Pequena'), ('M', 'Média'), ('G', 'Grande'), ('T', 'Família')], verbose_name='Tamanho')),
                ('photo', models.ImageField(null=True, upload_to='controle/%Y/%m/%d', blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('destaque', models.BooleanField(default=False, verbose_name='Destaque')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
