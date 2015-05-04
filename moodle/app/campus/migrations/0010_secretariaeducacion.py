# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0009_auto_20150502_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretariaEducacion',
            fields=[
                ('codigo', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('entidadTerritorial', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('fijo', models.CharField(max_length=30, blank=True, null=True)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
    ]
