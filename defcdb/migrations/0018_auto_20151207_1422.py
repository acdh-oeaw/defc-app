# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0017_dc_site_topography"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="topography",
            field=models.ForeignKey(
                blank=True,
                help_text="Description of surface shape and features.",
                null=True,
                to="defcdb.DC_site_topography",
            ),
        ),
    ]
