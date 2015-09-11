# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0011_auto_20150911_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='system',
        ),
        migrations.AddField(
            model_name='period',
            name='system',
            field=models.ForeignKey(blank=True, to='newModel.DC_chronological_system', help_text='Name of the chronological system.', null=True),
        ),
    ]
