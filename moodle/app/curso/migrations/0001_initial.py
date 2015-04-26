# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=40)),
            ],
        ),
    ]
