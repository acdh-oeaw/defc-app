# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0005_auto_20151210_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_calibration',
            field=models.CharField(null=True, max_length=5, blank=True, help_text='Was the date calibrated or not?', choices=[('yes', 'yes'), ('no', 'no')], verbose_name='Earliest date: Calibration'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_lab_number',
            field=models.CharField(blank=True, help_text='The Laboratory number of 14C sample of the earliest date.', max_length=100, null=True, verbose_name='Earliest date: Lab Number'),
        ),
    ]
