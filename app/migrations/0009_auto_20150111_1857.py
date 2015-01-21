# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_unit_allowance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='allowance',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
