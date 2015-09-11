# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newModel.customTypes


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0003_remove_dc_reference_type_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='DC_chronological_system',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cs_name', models.CharField(help_text='Name of the chronological system.', max_length=100, null=True, blank=True)),
                ('period_name', models.CharField(help_text='Name of archaeological period for which evidence was found.', max_length=100, null=True, blank=True)),
                ('start_date1_BC', newModel.customTypes.CustomIntegerField(null=True, blank=True)),
                ('start_date2_BC', newModel.customTypes.CustomIntegerField(null=True, blank=True)),
                ('end_date1_BC', newModel.customTypes.CustomIntegerField(null=True, blank=True)),
                ('end_date2_BC', newModel.customTypes.CustomIntegerField(null=True, blank=True)),
                ('region', models.ForeignKey(blank=True, to='newModel.DC_region', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_period_datedby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='please provide helptext', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_period_datingmethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='please provide helptext', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='period',
            name='chronological_system',
        ),
        migrations.RemoveField(
            model_name='period',
            name='end_date1_BC',
        ),
        migrations.RemoveField(
            model_name='period',
            name='end_date2_BC',
        ),
        migrations.RemoveField(
            model_name='period',
            name='period_name',
        ),
        migrations.RemoveField(
            model_name='period',
            name='region',
        ),
        migrations.RemoveField(
            model_name='period',
            name='start_date1_BC',
        ),
        migrations.RemoveField(
            model_name='period',
            name='start_date2_BC',
        ),
        migrations.AlterField(
            model_name='period',
            name='c14_calibrated',
            field=models.CharField(blank=True, max_length=100, null=True, help_text='Date is a calibrated date.', choices=[('yes', 'yes'), ('no', 'no')]),
        ),
        migrations.RemoveField(
            model_name='period',
            name='dated_by',
        ),
        migrations.RemoveField(
            model_name='period',
            name='dating_method',
        ),
        migrations.AddField(
            model_name='period',
            name='system',
            field=models.ManyToManyField(help_text='Name of the chronological system.', to='newModel.DC_chronological_system', blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='dated_by',
            field=models.ManyToManyField(help_text='Source providing information about date.', to='newModel.DC_period_datedby', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='dating_method',
            field=models.ManyToManyField(help_text='HELPTEXT', to='newModel.DC_period_datingmethod', blank=True),
        ),
    ]
