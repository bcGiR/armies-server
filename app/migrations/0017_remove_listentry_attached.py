# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20150120_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listentry',
            name='attached',
        ),
    ]
