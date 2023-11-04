# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0028_dc_finds_small_finds_type_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dc_finds_small_finds_type",
            name="category",
        ),
    ]
