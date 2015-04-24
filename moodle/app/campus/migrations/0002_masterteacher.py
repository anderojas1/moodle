# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(to='campus.Persona', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('experiencia', models.CharField(max_length=5)),
            ],
            bases=('campus.persona',),
        ),
    ]
