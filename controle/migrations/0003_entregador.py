# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(unique=True, max_length=20, verbose_name='CPF')),
                ('rg', models.CharField(unique=True, max_length=20, verbose_name='RG')),
                ('celular', models.CharField(max_length=14, verbose_name='Celular')),
                ('empresa', models.ForeignKey(related_name='Entregadores', to='controle.Empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name_plural': 'Entregadores',
                'verbose_name': 'Entregador',
                'ordering': ['nome'],
            },
        ),
    ]
