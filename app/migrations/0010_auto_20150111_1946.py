# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150111_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='attached',
            field=models.ForeignKey(blank=True, to='app.Unit', related_name='units', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='utype',
            field=models.CharField(max_length=2, choices=[('WC', 'Warcaster'), ('WL', 'Warlock'), ('WJ', 'Warjack'), ('WB', 'Warbeast'), ('UN', 'Unit'), ('UA', 'Unit Attachment'), ('SL', 'Solo'), ('BE', 'Battle Engine'), ('CO', 'Colossal'), ('GA', 'Gargantuan')]),
            preserve_default=True,
        ),
    ]
