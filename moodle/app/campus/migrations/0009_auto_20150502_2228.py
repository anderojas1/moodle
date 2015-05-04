# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0008_delete_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterteacher',
            name='experiencia',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
