# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0010_auto_20151204_1445"),
    ]

    operations = [
        migrations.CreateModel(
            name="DC_site_coordinatesource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="please provide helptext",
                        null=True,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="site",
            name="coordinate_source",
            field=models.ForeignKey(
                on_delete=models.SET_NULL,
                help_text="Source providing information about the global position of site.",
                blank=True,
                to="defcdb.DC_site_coordinatesource",
                null=True,
            ),
        ),
    ]
