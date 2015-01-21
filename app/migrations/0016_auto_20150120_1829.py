# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_unit_attach'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('armylist', models.ForeignKey(to='app.ArmyList')),
                ('attached', models.ManyToManyField(null=True, to='app.ListEntry', blank=True)),
                ('unit', models.ForeignKey(to='app.Unit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='unit',
            name='armylist',
        ),
        migrations.AddField(
            model_name='armylist',
            name='units',
            field=models.ManyToManyField(through='app.ListEntry', to='app.Unit'),
            preserve_default=True,
        ),
    ]
