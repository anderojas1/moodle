# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0006_auto_20150424_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(serialize=False, max_length=15, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)]),
        ),
    ]
