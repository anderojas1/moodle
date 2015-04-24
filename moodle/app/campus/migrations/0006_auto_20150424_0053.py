# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0005_auto_20150424_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fijo',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
    ]
