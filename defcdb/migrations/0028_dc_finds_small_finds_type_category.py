# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0027_auto_20160224_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_finds_small_finds_type',
            name='category',
            field=models.ForeignKey(blank=True, null=True, to='defcdb.DC_finds_small_finds_category'),
        ),
    ]
