# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("threedmodels", "0003_auto_20160421_1229"),
    ]

    operations = [
        migrations.AddField(
            model_name="threedmodel",
            name="model_parameters",
            field=models.FileField(
                null=True, upload_to="static/threedmodels/parameters", blank=True
            ),
        ),
        migrations.AlterField(
            model_name="threedmodel",
            name="model_metadata",
            field=models.FileField(
                null=True, upload_to="static/threedmodels/metadata", blank=True
            ),
        ),
        migrations.AlterField(
            model_name="threedmodel",
            name="model_thumbnail",
            field=models.FileField(
                null=True, upload_to="static/threedmodels/thumbnails", blank=True
            ),
        ),
    ]
