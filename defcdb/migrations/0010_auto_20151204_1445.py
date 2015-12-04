# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0009_auto_20151204_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='authorityfile_id',
            field=models.CharField(help_text="Identifier provided by www.GeoNames.org. E.g. the number in <a href='http://www.geonames.org/2772400/linz.html'>http://www.geonames.org/2772400/linz.html</a>.", null=True, max_length=100, blank=True, verbose_name='Authorityfile ID'),
        ),
        migrations.AlterField(
            model_name='site',
            name='exact_location',
            field=models.CharField(help_text='<strong>Yes</strong>: location of site is known and coordinates from the approximate center of the site have been entered.<br/> <strong>No</strong>: Only the region/province/ephorie approximate location of the site is known. Coordinates from the approximate center of the region/province/ ephorie have been entered.', choices=[('yes', 'yes'), ('no', 'no')], max_length=50, default='yes'),
        ),
        migrations.AlterField(
            model_name='site',
            name='number_of_activity_periods',
            field=models.IntegerField(help_text='How many past activities have been recorded on the site?', null=True, blank=True),
        ),
    ]
