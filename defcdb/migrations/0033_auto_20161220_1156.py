# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0032_auto_20160421_1006"),
    ]

    operations = [
        migrations.CreateModel(
            name="DC_finds_lithics_unretouched_tools",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, help_text="Short description."),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="finds",
            name="pottery_type",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="finds",
            name="lithics_unretouched_tools",
            field=models.ManyToManyField(
                blank=True,
                verbose_name="Lithics unretouched tools (types)",
                to="defcdb.DC_finds_lithics_unretouched_tools",
            ),
        ),
    ]
