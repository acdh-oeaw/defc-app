# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images_metadata", "0002_auto_20160314_1343"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagethesaurus",
            name="filename",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
