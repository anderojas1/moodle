# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_cohorte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohorte',
            name='id',
            field=models.CharField(serialize=False, max_length=20, primary_key=True),
        ),
    ]
