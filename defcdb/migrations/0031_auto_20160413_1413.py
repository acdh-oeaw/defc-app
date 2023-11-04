# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0030_dc_finds_small_finds_type_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="exact_location",
            field=models.CharField(
                help_text="<strong>Yes</strong>: location of site is known and coordinates from the approximate center of the site have been entered.<br/> <strong>No</strong>: Only the region/province/ephorie approximate location of the site is known. Coordinates from the approximate center of the region/province/ ephorie have been entered.",
                max_length=50,
                choices=[("yes", "yes"), ("no", "no")],
                default="no",
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="name",
            field=models.CharField(
                null=True,
                blank=True,
                unique=True,
                max_length=255,
                help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.",
            ),
        ),
    ]
