# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_auto_20150424_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fijo',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
