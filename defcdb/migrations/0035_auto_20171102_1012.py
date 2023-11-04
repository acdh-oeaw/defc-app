# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0034_auto_20161220_1254"),
    ]

    operations = [
        migrations.AlterField(
            model_name="area",
            name="settlement_construction_shape",
            field=models.ManyToManyField(
                verbose_name="Settlement building shape",
                blank=True,
                to="defcdb.DC_area_constructionshape",
                help_text="Shape of the building.",
            ),
        ),
        migrations.AlterField(
            model_name="area",
            name="settlement_construction_type",
            field=models.ManyToManyField(
                verbose_name="Settlement building type",
                blank=True,
                to="defcdb.DC_area_constructiontype",
                help_text="Method used for fabricating the buildings.",
            ),
        ),
    ]
