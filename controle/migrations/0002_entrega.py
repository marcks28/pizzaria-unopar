# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_entrega', models.DateTimeField(verbose_name='Dt. Entrega', auto_now=True)),
                ('status_entrega', models.CharField(choices=[('EN', 'Entregue'), ('ET', 'Em trânsito'), ('CN', 'Cancelado')], max_length=2, verbose_name='Situação', default='ET')),
                ('entregador', models.ForeignKey(verbose_name='Entregador', related_name='entrega_entregador', to='controle.Entregador')),
                ('pedido', models.ForeignKey(verbose_name='Pedido', related_name='pedido_entrega', to='controle.Pedido')),
            ],
        ),
    ]
