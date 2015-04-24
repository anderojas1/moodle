# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0003_auto_20150424_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.IntegerField(),
        ),
    ]
