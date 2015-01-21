# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150111_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='attachable',
        ),
        migrations.AlterField(
            model_name='unit',
            name='attached',
            field=models.ForeignKey(blank=True, to='app.Unit', related_name='units', null=True),
            preserve_default=True,
        ),
    ]
