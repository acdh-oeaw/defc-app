# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("threedmodels", "0005_auto_20160428_0859"),
    ]

    operations = [
        migrations.AlterField(
            model_name="threedmodel",
            name="model_file",
            field=models.FileField(upload_to="models", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="threedmodel",
            name="model_metadata",
            field=models.FileField(upload_to="metadata", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="threedmodel",
            name="model_parameters",
            field=models.FileField(upload_to="parameters", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="threedmodel",
            name="model_thumbnail",
            field=models.FileField(upload_to="thumbnails", null=True, blank=True),
        ),
    ]
