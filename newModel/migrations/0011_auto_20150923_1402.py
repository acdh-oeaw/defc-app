# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0010_auto_20150922_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='c14_absolute_from',
        ),
        migrations.RemoveField(
            model_name='period',
            name='c14_absolute_to',
        ),
        migrations.RemoveField(
            model_name='period',
            name='c14_calibrated',
        ),
        migrations.AddField(
            model_name='area',
            name='c14_absolute_from',
            field=models.IntegerField(help_text='Year when archaeological period started.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='c14_absolute_to',
            field=models.IntegerField(help_text='Year when archaeological period ended.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='c14_calibrated',
            field=models.CharField(blank=True, max_length=100, null=True, help_text='Date is a calibrated date.', choices=[('yes', 'yes'), ('no', 'no')]),
        ),
    ]
