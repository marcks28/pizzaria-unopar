# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_entregador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_on', models.DateTimeField(auto_now=True)),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('cliente', models.ForeignKey(verbose_name='Cliente', related_name='clientes_pedido', to='controle.Cliente')),
                ('produto', models.ForeignKey(verbose_name='Produto', related_name='prodtudo_pedido', to='controle.Produto')),
            ],
        ),
    ]
