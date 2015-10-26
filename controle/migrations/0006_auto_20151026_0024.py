# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0005_auto_20151026_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='create_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Pedido realizado em'),
        ),
    ]
