# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150113_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='attached',
        ),
    ]
