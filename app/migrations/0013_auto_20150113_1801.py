# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150111_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armylist',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='armylist',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
