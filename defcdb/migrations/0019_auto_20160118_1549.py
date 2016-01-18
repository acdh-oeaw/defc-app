# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0018_auto_20151207_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='DC_finds_lithics_retouched_tools',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=100, help_text='PLEASE PROVIDE SOME HELPTEX')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DC_finds_lithics_core',
            new_name='DC_finds_lithics_core_shape',
        ),
        migrations.RenameModel(
            old_name='DC_finds_lithics_modified_tools',
            new_name='DC_finds_lithics_industry',
        ),
        migrations.RenameModel(
            old_name='DC_finds_lithics_debitage',
            new_name='DC_finds_lithics_raw_material',
        ),
        migrations.RemoveField(
            model_name='period',
            name='dated_by',
        ),
        migrations.RemoveField(
            model_name='period',
            name='dating_method',
        ),
        migrations.RemoveField(
            model_name='period',
            name='system',
        ),
        migrations.RemoveField(
            model_name='area',
            name='c14_absolute_from',
        ),
        migrations.RemoveField(
            model_name='area',
            name='c14_absolute_to',
        ),
        migrations.RemoveField(
            model_name='area',
            name='c14_calibrated',
        ),
        migrations.RemoveField(
            model_name='area',
            name='cave_rockshelters_evidence_of_graves_human_remains',
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_cores',
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_debitage',
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_modified_tools',
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_human_remains',
            field=models.CharField(blank=True, help_text='Any human remains found in this cave or rockshelter?', null=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=3),
        ),
        migrations.AddField(
            model_name='area',
            name='dating_method',
            field=models.ManyToManyField(to='defcdb.DC_period_datingmethod', blank=True, help_text='Method used for dating the site.'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_14C_age',
            field=models.IntegerField(blank=True, help_text='The earliest date without calibration BP.', null=True, verbose_name='Earliest date: 14C age (BP)'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_14C_age_calibrated',
            field=models.IntegerField(blank=True, help_text='The earliest date with calibration in BC.', null=True, verbose_name='Earliest date: 14C age calibrated (BC)'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_calibration',
            field=models.CharField(null=True, verbose_name='Earliest date: Calibration', help_text='Was the date calibrated or not?', blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=5),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_date_of_calibration',
            field=models.DateField(blank=True, help_text='When was the date calibrated? If only year is specified, use the first day of the month/year.', null=True, verbose_name='Earliest date: Date of calibration'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_delta13',
            field=models.IntegerField(blank=True, help_text='Delta 13C information.', null=True, verbose_name='Earliest date: delta 13C'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_lab_number',
            field=models.CharField(blank=True, help_text='The Laboratory number of 14C sample of the earliest date.', null=True, max_length=100, verbose_name='Earliest date: Lab Number'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_date_standard_deviation',
            field=models.IntegerField(blank=True, help_text='The statistical reliability of the dating. Use +/-.', null=True, verbose_name='Earliest date: Standard deviation (+/-)'),
        ),
        migrations.AddField(
            model_name='area',
            name='earliest_datedated_by',
            field=models.ManyToManyField(related_name='earliestdatedatedby', to='defcdb.DC_period_datedby', verbose_name='Earliest date: Dated by', help_text='Dating source material.', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_14C_age',
            field=models.IntegerField(blank=True, help_text='The latest date without calibration BP (raw).', null=True, verbose_name='Latest date: 14C age (BP)'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_14C_age_calibrated',
            field=models.IntegerField(blank=True, help_text='The latest date with calibration in BC.', null=True, verbose_name='Latest date: 14C age calibrated (BC)'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_calibration',
            field=models.CharField(null=True, verbose_name='Latest date: Calibration', help_text='Was the date calibrated or not?', blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=5),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_date_of_calibration',
            field=models.DateField(blank=True, help_text='When was the date calibrated? If only year is specified, use the first day of the month/year.', null=True, verbose_name='Latest date: Date of calibration'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_delta13',
            field=models.IntegerField(blank=True, help_text='Delta 13C information.', null=True, verbose_name='Latest date: delta 13C'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_lab_number',
            field=models.CharField(blank=True, help_text='The Laboratory number of 14C sample of the latest date.', null=True, max_length=100, verbose_name='Latest date: Lab Number'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_date_standard_deviation',
            field=models.IntegerField(blank=True, help_text='The statistical reliability of the dating. Use +/-.', null=True, verbose_name='Latest date: Standard deviation (+/-)'),
        ),
        migrations.AddField(
            model_name='area',
            name='latest_datedated_by',
            field=models.ManyToManyField(related_name='latestdatedatedby', to='defcdb.DC_period_datedby', verbose_name='Latest date: Dated by', help_text='Dating source material.', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='area',
            name='radiocarbon_dated',
            field=models.CharField(blank=True, help_text='Radiocarbon dated?', null=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=5),
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_core_shape',
            field=models.ManyToManyField(to='defcdb.DC_finds_lithics_core_shape', blank=True, help_text='Type of the core of the tool.'),
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_industry',
            field=models.ManyToManyField(to='defcdb.DC_finds_lithics_industry', blank=True, help_text='Blade/Flake/Microlithic industry.'),
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_raw_material',
            field=models.ManyToManyField(to='defcdb.DC_finds_lithics_raw_material', blank=True, help_text='Material from which the tool was made.'),
        ),
        migrations.AddField(
            model_name='finds',
            name='obsidian',
            field=models.CharField(blank=True, help_text='Are there traces of obsidian in the tool?', null=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
        migrations.AddField(
            model_name='finds',
            name='obsidian_amount',
            field=models.IntegerField(blank=True, help_text='The percentage of obsidian in the tool.', null=True, verbose_name='Obsidian amount (%)'),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_manipulations_of_graves',
            field=models.ManyToManyField(to='defcdb.DC_area_manipulationofgraves', help_text='Post-depositional intervention of grave.', blank=True, verbose_name='Grave: manipulations of graves'),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_number_of_female_sex',
            field=models.IntegerField(blank=True, help_text='Number of female individuals in a grave/settlement.', null=True, verbose_name='Grave: number of female sex'),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_number_of_male_sex',
            field=models.IntegerField(blank=True, help_text='Number of male individuals in a grave/settlement.', null=True, verbose_name='Grave: number of male sex'),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_number_of_not_specified_sex',
            field=models.IntegerField(blank=True, help_text='Number of those individuals whose sex could not be determined.', null=True, verbose_name='Grave: number of not specified sex'),
        ),
        migrations.RemoveField(
            model_name='area',
            name='period',
        ),
        migrations.AddField(
            model_name='area',
            name='period',
            field=models.ManyToManyField(to='defcdb.DC_chronological_system', blank=True, help_text='Chronological period. This contains information about the name, the period, start/enddate1/2, and the region.'),
        ),
        migrations.AlterField(
            model_name='area',
            name='period_reference',
            field=models.ManyToManyField(to='bib.Book', related_name='periodreference', blank=True, help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the period.'),
        ),
        migrations.RemoveField(
            model_name='area',
            name='quarry_exploitation_type',
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_exploitation_type',
            field=models.ForeignKey(null=True, help_text='Type of extraction.', to='defcdb.DC_area_exploitationtype', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='reference',
            field=models.ManyToManyField(to='bib.Book', related_name='referencereference', blank=True, help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.'),
        ),
        migrations.AlterField(
            model_name='area',
            name='settlement_building_technique',
            field=models.ManyToManyField(to='defcdb.DC_area_buildingtechnique', blank=True, help_text='Type of buildings.'),
        ),
        migrations.AlterField(
            model_name='area',
            name='settlement_construction_type',
            field=models.ManyToManyField(to='defcdb.DC_area_constructiontype', blank=True, help_text='Method used for fabricating the buildings.'),
        ),
        migrations.RemoveField(
            model_name='area',
            name='settlement_type',
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_type',
            field=models.ForeignKey(null=True, help_text='Classification of settlement.', to='defcdb.DC_area_settlementtype', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='lithics_technology',
            field=models.ManyToManyField(to='defcdb.DC_finds_lithics_technology', blank=True, help_text='Technology of lithic production.'),
        ),
        migrations.AlterField(
            model_name='site',
            name='province',
            field=models.ForeignKey(null=True, help_text='Geographical area where the site is located.', to='defcdb.DC_province', verbose_name='District', blank=True),
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_retouched_tools',
            field=models.ManyToManyField(to='defcdb.DC_finds_lithics_retouched_tools', help_text='Type of the retouched tool.', blank=True, verbose_name='Lithics retouched tools (types)'),
        ),
    ]
