# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0003_auto_20151210_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areatry',
            name='c14_absolute_from',
        ),
        migrations.RemoveField(
            model_name='areatry',
            name='c14_absolute_to',
        ),
        migrations.RemoveField(
            model_name='areatry',
            name='c14_calibrated',
        ),
        migrations.RemoveField(
            model_name='areatry',
            name='cave_rockshelters_evidence_of_graves_human_remains',
        ),
        migrations.AddField(
            model_name='areatry',
            name='cave_rockshelters_human_remains',
            field=models.CharField(help_text='Any human remains found in this cave or rockshelter?', choices=[('yes', 'yes'), ('no', 'no')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='earliest_date_14C_age',
            field=models.IntegerField(help_text='pleaseProvideSomeHelptext', null=True, blank=True, verbose_name='Earliest date: 14C age (BC/BP)'),
        ),
        migrations.AlterField(
            model_name='areatry',
            name='period',
            field=models.ForeignKey(null=True, blank=True, help_text='Chronological period. This contains information about the name, the period, start/enddate1/2, and the region.', to='defcdb.DC_chronological_system', related_name='areatry_period'),
        ),
    ]
