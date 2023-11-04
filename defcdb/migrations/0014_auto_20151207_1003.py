# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0013_auto_20151207_1002"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="alias_name",
            field=models.ManyToManyField(
                related_name="aliasName",
                to="defcdb.Name",
                blank=True,
                help_text="Other name of the site.",
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="alternative_name",
            field=models.ManyToManyField(
                related_name="alternativeName",
                to="defcdb.Name",
                blank=True,
                help_text="Different spelling of the name of the site.",
            ),
        ),
    ]
