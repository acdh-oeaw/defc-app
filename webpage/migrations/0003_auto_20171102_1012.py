# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webpage", "0002_auto_20151125_1809"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateField(
                max_length=200,
                null=True,
                blank=True,
                help_text="In format 'year-month-day', e.g. 2016-04-24",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(
                max_length=200,
                null=True,
                blank=True,
                help_text="In format 'year-month-day', e.g. 2016-04-24",
            ),
        ),
    ]
