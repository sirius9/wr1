# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikestatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('station_name', models.CharField(max_length=30, default='')),
                ('available_bike', models.IntegerField(default=0)),
                ('all_dock', models.IntegerField(default=0)),
                ('using_dock', models.IntegerField(default=0)),
                ('available_dock', models.IntegerField(default=0)),
            ],
        ),
    ]
