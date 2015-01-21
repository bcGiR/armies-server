# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150111_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='attachable',
            field=models.ForeignKey(blank=True, related_name='units.attachable', to='app.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='attached',
            field=models.ForeignKey(blank=True, related_name='units.attached', to='app.Unit', null=True),
            preserve_default=True,
        ),
    ]
