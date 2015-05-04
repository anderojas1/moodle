# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('curso', models.ForeignKey(to='curso.Curso')),
            ],
        ),
    ]
