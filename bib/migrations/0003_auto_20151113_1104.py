# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bib", "0002_auto_20151113_1102"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publication_year",
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
