# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0004_auto_20150911_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='DC_area_settlementstructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Layout of settlement.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='area',
            name='settlement_constructiontype',
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_construction_type',
            field=models.ManyToManyField(help_text='Type of buildings.', to='newModel.DC_area_constructiontype', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cave_rockshelters_evidence_of_occupation',
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_evidence_of_occupation',
            field=models.ManyToManyField(help_text='Type of evidence indicating occupation found.', to='newModel.DC_area_evidenceofoccupation', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_age_groups',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_age_groups',
            field=models.ManyToManyField(help_text='Age.', to='newModel.DC_area_agegroups', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_grave_type',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_grave_type',
            field=models.ManyToManyField(help_text='Types of graves.', to='newModel.DC_area_gravetype', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_manipulations_of_graves',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_manipulations_of_graves',
            field=models.ManyToManyField(help_text='If and how the space with the graves is marked.', to='newModel.DC_area_manipulationofgraves', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_mortuary_features',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_mortuary_features',
            field=models.ManyToManyField(help_text='Parts of the cemetery other than graves.', to='newModel.DC_area_mortuaryfeatures', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_sexes',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_sexes',
            field=models.ManyToManyField(help_text='Sex.', to='newModel.DC_area_sexes', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_topography',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_topography',
            field=models.ManyToManyField(help_text='Connection of the cemetery/graves with other archaeological /natural or modified landscape features.', to='newModel.DC_area_topography', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='cemetery_graves_type_of_human_remains',
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_type_of_human_remains',
            field=models.ManyToManyField(help_text='How the humans were treated after death and buried.', to='newModel.DC_area_typeofhumanremains', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='period',
        ),
        migrations.AddField(
            model_name='area',
            name='period',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Period', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='quarry_exploitation_type',
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_exploitation_type',
            field=models.ManyToManyField(help_text='Type of extraction.', to='newModel.DC_area_exploitationtype', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='quarry_raw_material',
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_raw_material',
            field=models.ManyToManyField(help_text='Resource that was extracted.', to='newModel.DC_area_rawmaterial', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='settlement_building_technique',
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_building_technique',
            field=models.ManyToManyField(help_text='Method used for fabricating the buildings.', to='newModel.DC_area_buildingtechnique', blank=True),
        ),
        migrations.RemoveField(
            model_name='area',
            name='settlement_type',
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_type',
            field=models.ManyToManyField(help_text='Classification of settlement.', to='newModel.DC_area_settlementtype', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='animal_remains_part',
        ),
        migrations.AddField(
            model_name='finds',
            name='animal_remains_part',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_animal_remains_part', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='animal_remains_species',
        ),
        migrations.AddField(
            model_name='finds',
            name='animal_remains_species',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_animal_remains_species', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='botany_species',
        ),
        migrations.AddField(
            model_name='finds',
            name='botany_species',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_botany_species', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_cores',
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_cores',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_core', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_debitage',
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_debitage',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_debitage', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_modified_tools',
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_modified_tools',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_modified_tools', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='lithics_technology',
        ),
        migrations.AddField(
            model_name='finds',
            name='lithics_technology',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_technology', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='material',
        ),
        migrations.AddField(
            model_name='finds',
            name='material',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_material', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='pottery_decoration',
        ),
        migrations.AddField(
            model_name='finds',
            name='pottery_decoration',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_decoration', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='pottery_detail',
        ),
        migrations.AddField(
            model_name='finds',
            name='pottery_detail',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_detail', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='pottery_form',
        ),
        migrations.AddField(
            model_name='finds',
            name='pottery_form',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_form', blank=True),
        ),
        migrations.RemoveField(
            model_name='finds',
            name='small_finds_type',
        ),
        migrations.AddField(
            model_name='finds',
            name='small_finds_type',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_small_finds_type', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_structure',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE HELPTEXT', to='newModel.DC_area_settlementstructure', blank=True),
        ),
    ]
