# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0021_auto_20160128_1627"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dc_finds_pottery_decoration",
            name="region",
            field=models.ManyToManyField(blank=True, to="defcdb.DC_region"),
        ),
        migrations.AlterField(
            model_name="dc_finds_pottery_detail",
            name="region",
            field=models.ManyToManyField(blank=True, to="defcdb.DC_region"),
        ),
        migrations.AlterField(
            model_name="dc_finds_pottery_form",
            name="region",
            field=models.ManyToManyField(blank=True, to="defcdb.DC_region"),
        ),
    ]
