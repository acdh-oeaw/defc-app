# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0019_auto_20160118_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dc_chronological_system',
            name='region',
        ),
        migrations.AddField(
            model_name='dc_chronological_system',
            name='region',
            field=models.ManyToManyField(to='defcdb.DC_region', null=True, blank=True),
        ),
    ]
