# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141230_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='armylist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 11, 10, 29, 77888), editable=False),
            preserve_default=False,
        ),
    ]
