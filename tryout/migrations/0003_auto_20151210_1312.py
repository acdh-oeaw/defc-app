# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0018_auto_20151207_1422'),
        ('tryout', '0002_auto_20151210_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areatry',
            name='dated_by',
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_14C_age',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: 14C age (BC/BP'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_14C_age_calibrated',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: 14C age calibrated (BC/BP)'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_calibration',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: Calibration'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_date_of_calibration',
            field=models.DateField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: Date of calibration'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_delta13',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: delta 13C'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_lab_number',
            field=models.CharField(verbose_name='Earliest date: Lab Number', null=True, help_text='pleaseProvideSomeHelptext', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_date_standard_deviation',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Earliest date: Standard deviation (+/-)'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='earliest_datedated_by',
            field=models.ManyToManyField(help_text='Source providing information about date.', blank=True, verbose_name='Earliest date: Dated by', to='defcdb.DC_period_datedby', max_length=100, related_name='earliestDatedBy'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_14C_age',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: 14C age (BC/BP'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_14C_age_calibrated',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: 14C age calibrated (BC/BP)'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_calibration',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: Calibration'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_date_of_calibration',
            field=models.DateField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: Date of calibration'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_delta13',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: delta 13C'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_lab_number',
            field=models.CharField(verbose_name='Latest date: Lab Number', null=True, help_text='pleaseProvideSomeHelptext', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_date_standard_deviation',
            field=models.IntegerField(null=True, help_text='pleaseProvideSomeHelptext', blank=True, verbose_name='Latest date: Standard deviation (+/-)'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='latest_datedated_by',
            field=models.ManyToManyField(help_text='Source providing information about date.', blank=True, verbose_name='Latest date: Dated by', to='defcdb.DC_period_datedby', max_length=100, related_name='latestDatedBy'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='radiocarbon_dated',
            field=models.CharField(null=True, choices=[('yes', 'yes'), ('no', 'no')], help_text='Radiocarbon dated?', blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='period',
            field=models.ForeignKey(help_text='Chronological period', related_name='areatry_period', null=True, to='defcdb.DC_chronological_system', blank=True),
        ),
    ]
