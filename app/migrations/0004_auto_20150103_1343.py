# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_armylist_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armylist',
            name='created',
            field=models.DateField(editable=False),
            preserve_default=True,
        ),
    ]
