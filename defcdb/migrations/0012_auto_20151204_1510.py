# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0011_auto_20151204_1453"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="area",
            name="geographical_reference",
        ),
        migrations.RemoveField(
            model_name="area",
            name="stratigraphical_unit_id",
        ),
        migrations.AlterField(
            model_name="area",
            name="area_nr",
            field=models.CharField(
                help_text="An established identifier for this area",
                max_length=45,
                verbose_name="Area ID",
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="period",
            name="system",
            field=models.ForeignKey(
                to="defcdb.DC_chronological_system",
                blank=True,
                help_text="chronological period.",
                verbose_name="Period",
                null=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="researchevent",
            name="project_id",
            field=models.CharField(
                help_text="Project unique identifier.",
                max_length=100,
                verbose_name="Project ID",
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="researchevent",
            name="year_of_activity_end_year",
            field=models.IntegerField(
                help_text="Year when research ended.",
                verbose_name="End year of research activity",
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="researchevent",
            name="year_of_activity_start_year",
            field=models.IntegerField(
                help_text="Year when research started.",
                verbose_name="Start year of research activity",
                blank=True,
                null=True,
            ),
        ),
    ]
