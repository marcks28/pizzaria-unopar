# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(verbose_name='Nome', max_length=50)),
                ('cnpj', models.CharField(verbose_name='CNPJ', unique=True, max_length=20)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=14)),
                ('endereco', models.CharField(verbose_name='Endereço', max_length=100)),
                ('email', models.EmailField(verbose_name='Email', null=True, max_length=254, blank=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'ordering': ['nome'],
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
