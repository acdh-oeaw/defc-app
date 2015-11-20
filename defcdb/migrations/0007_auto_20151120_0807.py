# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0006_site_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_country',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_country',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_province',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_province',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_region',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dc_region',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='authorityfile_id',
            field=models.CharField(max_length=100, help_text='Identifier provided by www.GeoNames.org', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dc_country',
            name='authorityfile_id',
            field=models.CharField(max_length=100, help_text='Identifier provided by www.GeoNames.org', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dc_province',
            name='authorityfile_id',
            field=models.CharField(max_length=100, help_text='Identifier provided by www.GeoNames.org', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dc_region',
            name='authorityfile_id',
            field=models.CharField(max_length=100, help_text='Identifier provided by www.GeoNames.org', null=True, blank=True),
        ),
    ]
