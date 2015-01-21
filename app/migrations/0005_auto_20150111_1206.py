# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150103_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unit',
            name='utype',
            field=models.CharField(max_length=254),
            preserve_default=True,
        ),
    ]
