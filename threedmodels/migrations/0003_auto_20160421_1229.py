# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("threedmodels", "0002_auto_20160421_1006"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inclusion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "inclusion_id",
                    models.CharField(max_length=100, null=True, blank=True),
                ),
                (
                    "inclusion_type",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
                (
                    "inclusion_color",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
                (
                    "inclusion_form",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
                (
                    "inclusion_particle_size",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
                (
                    "inclusion_frequency",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
                (
                    "inclusion_hardness",
                    models.CharField(max_length=500, null=True, blank=True),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_color",
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_form",
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_frequency",
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_hardness",
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_particle_size",
        ),
        migrations.RemoveField(
            model_name="threedmodel",
            name="inclusion_type",
        ),
        migrations.AddField(
            model_name="threedmodel",
            name="model_id",
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="threedmodel",
            name="inclusion",
            field=models.ManyToManyField(to="threedmodels.Inclusion", blank=True),
        ),
    ]
