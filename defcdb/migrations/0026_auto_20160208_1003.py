# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0025_auto_20160201_1110"),
    ]

    operations = [
        migrations.AlterField(
            model_name="name",
            name="language",
            field=models.CharField(
                blank=True,
                help_text="The 'name´s' language. Controlled vocab will be provided.",
                null=True,
                max_length=3,
            ),
        ),
    ]
