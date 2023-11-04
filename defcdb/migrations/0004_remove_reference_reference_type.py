# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0003_auto_20151109_1908"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reference",
            name="reference_type",
        ),
    ]
