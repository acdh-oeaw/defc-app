# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0029_remove_dc_finds_small_finds_type_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="dc_finds_small_finds_type",
            name="category",
            field=models.ForeignKey(
                blank=True,
                to="defcdb.DC_finds_small_finds_category",
                null=True,
                on_delete=models.SET_NULL,
            ),
        ),
    ]
