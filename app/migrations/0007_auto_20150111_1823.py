# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150111_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='armylist',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='armylist',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
