# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='PE', verbose_name='Status', choices=[('PE', 'Pendente'), ('EM', 'Em trânsito'), ('CN', 'Cancelado'), ('ET', 'Entregue')], max_length=2),
        ),
        migrations.AddField(
            model_name='pedido',
            name='taxa_entrega',
            field=models.DecimalField(default=3.5, verbose_name='Taxa', decimal_places=2, max_digits=6),
        ),
    ]
