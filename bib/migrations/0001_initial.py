# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "zoterokey",
                    models.CharField(serialize=False, max_length=100, primary_key=True),
                ),
                ("item_type", models.CharField(null=True, max_length=100, blank=True)),
                ("author", models.CharField(null=True, max_length=100, blank=True)),
                ("title", models.CharField(null=True, max_length=100, blank=True)),
                (
                    "publication_title",
                    models.CharField(null=True, max_length=100, blank=True),
                ),
                (
                    "short_title",
                    models.CharField(null=True, max_length=100, blank=True),
                ),
                (
                    "publication_year",
                    models.CharField(null=True, max_length=100, blank=True),
                ),
                ("place", models.CharField(null=True, max_length=100, blank=True)),
                ("isbn", models.CharField(null=True, max_length=100, blank=True)),
                ("issn", models.CharField(null=True, max_length=100, blank=True)),
                ("doi", models.CharField(null=True, max_length=100, blank=True)),
                ("url", models.CharField(null=True, max_length=100, blank=True)),
            ],
        ),
    ]
