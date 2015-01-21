# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150111_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='faction',
            field=models.CharField(default='CY', choices=[('CY', 'Cygnar'), ('ME', 'The Protectorate of Menoth'), ('KD', 'Khador'), ('CX', 'Cryx'), ('RT', 'Retribution of Scyrah'), ('CV', 'Convergence of Cyriss'), ('MC', 'Mercenaries'), ('TR', 'Trollbloods'), ('CO', 'Circle Orboros'), ('SK', 'Skorne'), ('LG', 'Legion of Everblight'), ('MN', 'Minions')], max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unit',
            name='utype',
            field=models.CharField(choices=[('WC', 'Warcaster'), ('WL', 'Warlock'), ('WJ', 'Warjack'), ('WB', 'Warbeast'), ('UN', 'Unit'), ('SL', 'Solo'), ('BE', 'Battle Engine'), ('CO', 'Colossal'), ('GA', 'Gargantuan')], max_length=2),
            preserve_default=True,
        ),
    ]
