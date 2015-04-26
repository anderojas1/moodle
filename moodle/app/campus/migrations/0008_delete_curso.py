# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0007_auto_20150426_1133'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
