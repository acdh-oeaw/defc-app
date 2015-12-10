# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0004_auto_20151210_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_14C_age',
            field=models.IntegerField(null=True, blank=True, verbose_name='Earliest date: 14C age (BP)', help_text='The earliest date without calibration BP.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_14C_age_calibrated',
            field=models.IntegerField(null=True, blank=True, verbose_name='Earliest date: 14C age calibrated (BP)', help_text='The earliest date with calibration BP.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_calibration',
            field=models.CharField(help_text='pleaseProvideSomeHelptext', choices=[('yes', 'yes'), ('no', 'no')], max_length=5, null=True, blank=True, verbose_name='Earliest date: Calibration'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_date_of_calibration',
            field=models.DateField(null=True, blank=True, verbose_name='Earliest date: Date of calibration', help_text='When was the date calibrated? If only year is specified, use the first day of the month/year.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_delta13',
            field=models.IntegerField(null=True, blank=True, verbose_name='Earliest date: delta 13C', help_text='Delta 13C information.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_lab_number',
            field=models.CharField(null=True, blank=True, verbose_name='The Laboratory number of 14C sample of the earliest date.', max_length=100, help_text='pleaseProvideSomeHelptext'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_standard_deviation',
            field=models.IntegerField(null=True, blank=True, verbose_name='Earliest date: Standard deviation (+/-)', help_text='The statistical reliability of the dating. Use +/-.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_datedated_by',
            field=models.ManyToManyField(help_text='Dating source material.', related_name='earliestDatedBy', max_length=100, to='defcdb.DC_period_datedby', blank=True, verbose_name='Earliest date: Dated by'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_14C_age',
            field=models.IntegerField(null=True, blank=True, verbose_name='Latest date: 14C age (BP', help_text='The latest date without calibration BP.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_14C_age_calibrated',
            field=models.IntegerField(null=True, blank=True, verbose_name='Latest date: 14C age calibrated (BP)', help_text='The latest date with calibration BP.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_calibration',
            field=models.CharField(help_text='Was the date calibrated or not?', choices=[('yes', 'yes'), ('no', 'no')], max_length=5, null=True, blank=True, verbose_name='Latest date: Calibration'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_date_of_calibration',
            field=models.DateField(null=True, blank=True, verbose_name='Latest date: Date of calibration', help_text='When was the date calibrated? If only year is specified, use the first day of the month/year.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_delta13',
            field=models.IntegerField(null=True, blank=True, verbose_name='Latest date: delta 13C', help_text='Delta 13C information.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_lab_number',
            field=models.CharField(null=True, blank=True, verbose_name='Latest date: Lab Number', max_length=100, help_text='The Laboratory number of 14C sample of the latest date.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_date_standard_deviation',
            field=models.IntegerField(null=True, blank=True, verbose_name='Latest date: Standard deviation (+/-)', help_text='The statistical reliability of the dating. Use +/-.'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='latest_datedated_by',
            field=models.ManyToManyField(help_text='Dating source material.', related_name='latestDatedBy', max_length=100, to='defcdb.DC_period_datedby', blank=True, verbose_name='Latest date: Dated by'),
        ),
    ]
