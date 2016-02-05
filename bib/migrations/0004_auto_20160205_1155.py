# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bib', '0003_auto_20151113_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='short_title',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
