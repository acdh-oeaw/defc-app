# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0020_auto_20160120_1223"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dc_chronological_system",
            name="region",
            field=models.ManyToManyField(to="defcdb.DC_region", blank=True),
        ),
        migrations.RemoveField(
            model_name="dc_finds_pottery_decoration",
            name="region",
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_decoration",
            name="region",
            field=models.ManyToManyField(to="defcdb.DC_region", null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name="dc_finds_pottery_detail",
            name="region",
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_detail",
            name="region",
            field=models.ManyToManyField(to="defcdb.DC_region", null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name="dc_finds_pottery_form",
            name="region",
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_form",
            name="region",
            field=models.ManyToManyField(to="defcdb.DC_region", null=True, blank=True),
        ),
    ]
