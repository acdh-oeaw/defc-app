# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0033_auto_20161220_1156"),
    ]

    operations = [
        migrations.CreateModel(
            name="DC_area_constructionshape",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                        auto_created=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, help_text="Short description."),
                ),
                (
                    "name",
                    models.CharField(
                        null=True,
                        blank=True,
                        help_text="Shape of building.",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.AlterField(
            model_name="area",
            name="grave_manipulations_of_graves",
            field=models.ManyToManyField(
                blank=True,
                to="defcdb.DC_area_manipulationofgraves",
                verbose_name="Grave: disturbance of graves",
                help_text="Post-depositional intervention of grave.",
            ),
        ),
        migrations.AlterField(
            model_name="area",
            name="settlement_construction_type",
            field=models.ManyToManyField(
                blank=True,
                to="defcdb.DC_area_constructiontype",
                verbose_name="Building type",
                help_text="Method used for fabricating the buildings.",
            ),
        ),
        migrations.AlterField(
            model_name="area",
            name="settlement_special_features",
            field=models.ManyToManyField(
                blank=True,
                to="defcdb.DC_area_specialfeatures",
                verbose_name="Settlement archaeological features",
                help_text="Parts of the settlement other than buildings.",
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="lithics_core_shape",
            field=models.ManyToManyField(
                blank=True,
                to="defcdb.DC_finds_lithics_core_shape",
                verbose_name="Lithics cores and preparation",
                help_text="Type of the core of the tool.",
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_construction_shape",
            field=models.ManyToManyField(
                blank=True,
                to="defcdb.DC_area_constructionshape",
                verbose_name="Building shape",
                help_text="Shape of the building.",
            ),
        ),
    ]
