# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0018_auto_20151207_1422'),
        ('tryout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='areatry',
            name='area_type',
            field=models.ForeignKey(help_text='The type of the area.', null=True, to='defcdb.DC_area_areatype', blank=True),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cave_rockshelters_evidence_of_graves_human_remains',
            field=models.ForeignKey(help_text='Presence of graves and/or human remains.', null=True, verbose_name='Cave/rockshelters: evidence of graves/human remains', blank=True, to='defcdb.DC_area_evidenceofgraveshumanremains'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cave_rockshelters_evidence_of_occupation',
            field=models.ManyToManyField(blank=True, help_text='Type of evidence indicating occupation found.', to='defcdb.DC_area_evidenceofoccupation', verbose_name='Cave/rockshelters: evidence of occupation'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cave_rockshelters_type',
            field=models.ForeignKey(help_text='Type of cave/rockshelter.', null=True, verbose_name='Cave/rockshelters type', blank=True, to='defcdb.DC_area_caverockshelterstype'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cemetery_or_grave',
            field=models.CharField(blank=True, null=True, max_length=100, choices=[('cemetery', 'cemetery'), ('grave', 'grave')]),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cemetery_or_graves_mortuary_features',
            field=models.ManyToManyField(blank=True, help_text='Parts of the cemetery other than graves.', to='defcdb.DC_area_mortuaryfeatures'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='cemetery_or_graves_topography',
            field=models.ManyToManyField(blank=True, help_text='Connection of the cemetery/graves with other archaeological /natural or modified landscape features.', to='defcdb.DC_area_topography'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_age_groups',
            field=models.ManyToManyField(blank=True, help_text='Age.', to='defcdb.DC_area_agegroups', verbose_name='Grave: age groups'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_estimated_number_of_individuals',
            field=models.CharField(blank=True, help_text='minimum and or maximum', null=True, max_length=100, verbose_name='Grave: estimated number of individuals'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_manipulations_of_graves',
            field=models.ManyToManyField(blank=True, help_text='If and how the space with the graves is marked.', to='defcdb.DC_area_manipulationofgraves', verbose_name='Grave: manipulations of graves'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_number_of_female_sex',
            field=models.IntegerField(blank=True, help_text='Helptext', null=True, verbose_name='Grave: number of female sex'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_number_of_graves',
            field=models.CharField(blank=True, help_text='Number of graves.', null=True, max_length=100, verbose_name='Grave: number of graves'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_number_of_male_sex',
            field=models.IntegerField(blank=True, help_text='Helptext', null=True, verbose_name='Grave: number of male sex'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_number_of_not_specified_sex',
            field=models.IntegerField(blank=True, help_text='Helptext', null=True, verbose_name='Grave: number of not specified sex'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_sexes',
            field=models.ManyToManyField(blank=True, help_text='Sex.', to='defcdb.DC_area_sexes', verbose_name='Grave: sexes'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_type',
            field=models.ManyToManyField(blank=True, help_text='Types of graves.', to='defcdb.DC_area_gravetype'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='grave_type_of_human_remains',
            field=models.ManyToManyField(blank=True, help_text='How the humans were treated after death and buried.', to='defcdb.DC_area_typeofhumanremains', verbose_name='Grave: type of human remains'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='quarry_exploitation_type',
            field=models.ManyToManyField(blank=True, help_text='Type of extraction.', to='defcdb.DC_area_exploitationtype'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='quarry_raw_material',
            field=models.ManyToManyField(blank=True, help_text='Resource that was extracted.', to='defcdb.DC_area_rawmaterial'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_building_technique',
            field=models.ManyToManyField(blank=True, help_text='Method used for fabricating the buildings.', to='defcdb.DC_area_buildingtechnique'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_construction_type',
            field=models.ManyToManyField(blank=True, help_text='Type of buildings.', to='defcdb.DC_area_constructiontype'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_human_remains',
            field=models.CharField(blank=True, help_text='Any human remains found in this Settlement?', null=True, max_length=3, choices=[('yes', 'yes'), ('no', 'no')]),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_special_features',
            field=models.ManyToManyField(blank=True, help_text='Parts of the settlement other than buildings.', to='defcdb.DC_area_specialfeatures'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_structure',
            field=models.ManyToManyField(blank=True, help_text='Layout of settlement.', to='defcdb.DC_area_settlementstructure'),
        ),
        migrations.AddField(
            model_name='areatry',
            name='settlement_type',
            field=models.ManyToManyField(blank=True, help_text='Classification of settlement.', to='defcdb.DC_area_settlementtype'),
        ),
    ]
