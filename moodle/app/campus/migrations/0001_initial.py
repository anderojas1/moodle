# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=30)),
                ('fijo', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
