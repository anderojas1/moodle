# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_masterteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.IntegerField(max_length=5),
        ),
    ]
