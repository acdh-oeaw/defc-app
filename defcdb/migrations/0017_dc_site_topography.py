# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0016_auto_20151207_1352"),
    ]

    operations = [
        migrations.CreateModel(
            name="DC_site_topography",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Description of surface shape and features.",
                        null=True,
                        max_length=100,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
    ]
