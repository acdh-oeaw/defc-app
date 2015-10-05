# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0006_auto_20150916_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_finds_amount',
            options={},
        ),
        migrations.AlterField(
            model_name='area',
            name='cave_rockshelters_evidence_of_graves_human_remains',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_evidenceofgraveshumanremains', help_text='Presence of graves and/or human remains.', null=True, verbose_name='Cave/rockshelters: evidence of graves/human remains'),
        ),
        migrations.AlterField(
            model_name='area',
            name='cave_rockshelters_evidence_of_occupation',
            field=models.ManyToManyField(help_text='Type of evidence indicating occupation found.', to='newModel.DC_area_evidenceofoccupation', verbose_name='Cave/rockshelters: evidence of occupation', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='cave_rockshelters_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_caverockshelterstype', help_text='Type of cave/rockshelter.', null=True, verbose_name='Cave/rockshelters type'),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_age_groups',
            field=models.ManyToManyField(help_text='Age.', to='newModel.DC_area_agegroups', verbose_name='Grave: age groups', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_estimated_number_of_individuals',
            field=models.CharField(help_text='minimum and or maximum', max_length=100, null=True, verbose_name='Grave: estimated number of individuals', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_manipulations_of_graves',
            field=models.ManyToManyField(help_text='If and how the space with the graves is marked.', to='newModel.DC_area_manipulationofgraves', verbose_name='Grave: manipulations of graves', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_number_of_graves',
            field=models.CharField(help_text='Number of graves.', max_length=100, null=True, verbose_name='Grave: number of graves', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_sexes',
            field=models.ManyToManyField(help_text='Sex.', to='newModel.DC_area_sexes', verbose_name='Grave: sexes', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_sexes_number',
            field=models.IntegerField(help_text='Helptext', null=True, verbose_name='Grave: sexes number', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='grave_type_of_human_remains',
            field=models.ManyToManyField(help_text='How the humans were treated after death and buried.', to='newModel.DC_area_typeofhumanremains', verbose_name='Grave: type of human remains', blank=True),
        ),
    ]
