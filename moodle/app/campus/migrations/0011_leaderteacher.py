# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0010_secretariaeducacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(to='campus.Persona', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
                ('areaAsignada', models.CharField(max_length=50)),
                ('calificacion', models.CharField(max_length=2)),
                ('certificado', models.CharField(max_length=50)),
            ],
            bases=('campus.persona',),
        ),
    ]
