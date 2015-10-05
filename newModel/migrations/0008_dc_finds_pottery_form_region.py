# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0007_auto_20150922_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_finds_pottery_form',
            name='region',
            field=models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True),
        ),
    ]
