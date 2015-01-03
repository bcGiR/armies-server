# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='armylist',
            field=models.ForeignKey(related_name='units', blank=True, null=True, to='app.ArmyList'),
            preserve_default=True,
        ),
    ]
