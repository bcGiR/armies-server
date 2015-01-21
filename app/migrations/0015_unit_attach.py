# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_unit_attached'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='attach',
            field=models.ManyToManyField(blank=True, null=True, to='app.Unit'),
            preserve_default=True,
        ),
    ]
