# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0008_auto_20151204_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='elevation',
            field=models.IntegerField(null=True, blank=True, help_text='If available'),
        ),
        migrations.AlterField(
            model_name='site',
            name='authorityfile_id',
            field=models.CharField(null=True, blank=True, max_length=100, help_text="Identifier provided by www.GeoNames.org. E.g. the number in 'http://www.geonames.org/2772400/linz.html'.", verbose_name='Authorityfile ID'),
        ),
        migrations.AlterField(
            model_name='site',
            name='exact_location',
            field=models.CharField(help_text='Yes: location of site is known and coordinates from the approximate center of the site have been entered. No: Only the region/province/ephorie approximate location of the site is known. Coordinates from the approximate center of the region/province/ ephorie have been entered.', max_length=50, choices=[('yes', 'yes'), ('no', 'no')], default='yes'),
        ),
    ]
