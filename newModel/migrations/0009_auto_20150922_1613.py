# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0008_dc_finds_pottery_form_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_finds_pottery_decoration',
            options={},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_pottery_detail',
            options={},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_pottery_form',
            options={},
        ),
        migrations.AddField(
            model_name='dc_finds_pottery_decoration',
            name='region',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_finds_pottery_detail',
            name='region',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dc_finds_pottery_form',
            name='region',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
