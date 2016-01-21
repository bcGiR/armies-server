# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_listentry_attached'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='attach',
            new_name='attachments',
        ),
    ]
