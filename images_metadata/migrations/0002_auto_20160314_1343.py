# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images_metadata", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagethesaurus",
            name="region",
            field=models.ManyToManyField(to="defcdb.DC_region", blank=True),
        ),
    ]
