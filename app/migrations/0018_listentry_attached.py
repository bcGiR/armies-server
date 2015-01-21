# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_listentry_attached'),
    ]

    operations = [
        migrations.AddField(
            model_name='listentry',
            name='attached',
            field=models.ForeignKey(blank=True, to='app.ListEntry', null=True),
            preserve_default=True,
        ),
    ]
