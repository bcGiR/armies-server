# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmyList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=254)),
                ('faction', models.CharField(choices=[('CY', 'Cygnar'), ('ME', 'The Protectorate of Menoth'), ('KD', 'Khador'), ('CX', 'Cryx'), ('RT', 'Retribution of Scyrah'), ('CV', 'Convergence of Cyriss'), ('MC', 'Mercenaries'), ('TR', 'Trollbloods'), ('CO', 'Circle Orboros'), ('SK', 'Skorne'), ('LG', 'Legion of Everblight'), ('MN', 'Minions')], max_length=2)),
                ('points', models.IntegerField(choices=[(15, '15 pts'), (25, '25 pts'), (35, '35 pts'), (50, '50 pts')])),
                ('owner', models.ForeignKey(related_name='armylists', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('utype', models.CharField(choices=[('CS', 'Warcaster/Warlock'), ('WJ', 'Warjack/Warbeast'), ('UN', 'Unit'), ('SO', 'Solo'), ('CO', 'Colossal/Gargantuan'), ('EN', 'Battle Engine')], max_length=2)),
                ('armylist', models.ForeignKey(to='app.ArmyList', related_name='units')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
