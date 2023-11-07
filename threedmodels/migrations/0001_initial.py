# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0031_auto_20160413_1413"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                ("first_name", models.CharField(null=True, blank=True, max_length=500)),
                ("last_name", models.CharField(null=True, blank=True, max_length=500)),
                (
                    "institution",
                    models.ManyToManyField(blank=True, to="defcdb.ResearchEvent"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                ("name", models.CharField(null=True, blank=True, max_length=500)),
                ("title", models.CharField(null=True, blank=True, max_length=500)),
                ("source", models.CharField(null=True, blank=True, max_length=500)),
                ("language", models.CharField(null=True, blank=True, max_length=500)),
                ("keywords", models.CharField(null=True, blank=True, max_length=500)),
                ("publisher", models.CharField(null=True, blank=True, max_length=500)),
                ("issued", models.CharField(null=True, blank=True, max_length=500)),
                ("license", models.CharField(null=True, blank=True, max_length=500)),
                (
                    "access_rights",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "contact",
                    models.ManyToManyField(blank=True, to="threedmodels.Contact"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Threedmodel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                ("part", models.CharField(null=True, blank=True, max_length=500)),
                ("diameter", models.CharField(null=True, blank=True, max_length=500)),
                (
                    "wall_thickness",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "surface_treatment_i",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "surface_treatment_o",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "surface_color_i",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "surface_color_o",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "decoration_color",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "decoration_description",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "fabric_color",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                ("hardness", models.CharField(null=True, blank=True, max_length=500)),
                ("sorting", models.CharField(null=True, blank=True, max_length=500)),
                ("density", models.CharField(null=True, blank=True, max_length=500)),
                ("pores", models.CharField(null=True, blank=True, max_length=500)),
                ("core_form", models.CharField(null=True, blank=True, max_length=500)),
                ("core_color", models.CharField(null=True, blank=True, max_length=500)),
                (
                    "inclusion_type",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "inclusion_color",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "inclusion_form",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "inclusion_particle_size",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "inclusion_frequency",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "inclusion_hardness",
                    models.CharField(null=True, blank=True, max_length=500),
                ),
                (
                    "finds",
                    models.ForeignKey(
                        null=True,
                        blank=True,
                        to="defcdb.Finds",
                        on_delete=models.SET_NULL,
                    ),
                ),
                (
                    "resource_metadata",
                    models.ForeignKey(
                        null=True,
                        blank=True,
                        to="threedmodels.Project",
                        on_delete=models.SET_NULL,
                    ),
                ),
            ],
        ),
    ]
