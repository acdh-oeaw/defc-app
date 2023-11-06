# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0002_auto_20151027_1445"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="site",
            name="gps_data_e",
        ),
        migrations.RemoveField(
            model_name="site",
            name="gps_data_n",
        ),
        migrations.RemoveField(
            model_name="site",
            name="gps_data_z",
        ),
        migrations.AddField(
            model_name="site",
            name="exact_location",
            field=models.CharField(
                max_length=50, default="yes", choices=[("yes", "yes"), ("no", "no")]
            ),
        ),
        migrations.AddField(
            model_name="site",
            name="latitude",
            field=models.DecimalField(
                null=True, decimal_places=12, blank=True, max_digits=20
            ),
        ),
        migrations.AddField(
            model_name="site",
            name="longitude",
            field=models.DecimalField(
                null=True, decimal_places=12, blank=True, max_digits=20
            ),
        ),
        migrations.RemoveField(
            model_name="area",
            name="period",
        ),
        migrations.AddField(
            model_name="area",
            name="period",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET_NULL,
                to="defcdb.Period",
                blank=True,
                help_text="Period defined by the archaeologist",
            ),
        ),
        migrations.RemoveField(
            model_name="finds",
            name="pottery_form",
        ),
        migrations.AddField(
            model_name="finds",
            name="pottery_form",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET_NULL,
                to="defcdb.DC_finds_pottery_form",
                blank=True,
                help_text="Form of pottery.",
            ),
        ),
    ]
