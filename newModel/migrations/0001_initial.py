# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newModel.customTypes


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_nr', models.CharField(help_text='An established identifier for this area', max_length=45, null=True, blank=True)),
                ('stratigraphical_unit_id', models.CharField(help_text='The identifier of the area\xb4s stratigraphical unit', max_length=100, null=True, blank=True)),
                ('geographical_reference', models.CharField(help_text='Locates the Area in the Site', max_length=100, null=True, blank=True)),
                ('description', models.TextField(help_text='Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves', null=True, blank=True)),
                ('settlement_human_remains', models.CharField(blank=True, max_length=3, null=True, help_text='Any human remains found in this Settlement?', choices=[('yes', 'yes'), ('no', 'no')])),
                ('cemetery_or_grave', models.CharField(blank=True, max_length=100, null=True, choices=[('cemetery', 'cemetery'), ('grave', 'grave')])),
                ('grave_number_of_graves', models.CharField(help_text='Number of graves.', max_length=100, null=True, blank=True)),
                ('grave_estimated_number_of_individuals', models.CharField(help_text='minimum and or maximum', max_length=100, null=True, blank=True)),
                ('grave_sexes_number', models.IntegerField(help_text='Helptext', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_agegroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Age.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_areatype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The type of the area.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_buildingtechnique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Method used for fabricating the buildings.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_caverockshelterstype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Type of cave/rockshelter.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_constructiontype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Type of buildings.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_evidenceofgraveshumanremains',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Presence of graves and/or human remains.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_evidenceofoccupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Type of evidence indicating occupation found.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_exploitationtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Type of extraction.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_gravetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Types of graves.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_manipulationofgraves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='If and how the space with the graves is marked.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_mortuaryfeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Parts of the cemetery other than graves.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_rawmaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Resource that was extracted.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_settlementstructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Layout of settlement.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_settlementtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Classification of settlement.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_sexes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Sex.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_specialfeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Parts of the settlement other than buildings.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_topography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Connection of the cemetery/graves with other archaeological /natural or modified landscape features.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_area_typeofhumanremains',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='How the humans were treated after death and buried.', max_length=100, null=True, blank=True)),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='DC_country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the country', max_length=100, blank=True)),
                ('original_name', models.CharField(help_text='The original or local name of the country', max_length=100, null=True, blank=True)),
                ('authorityfile_id', models.CharField(help_text='Identifier provided by some authority file', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_amount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_animal_remains_completeness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_animal_remains_part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_animal_remains_species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
                ('latin_name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_botany_species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
                ('latin_name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_lithics_core',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_lithics_debitage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_lithics_modified_tools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_lithics_technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_pottery_decoration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_pottery_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_pottery_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_small_finds_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_small_finds_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_finds_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_interpretation_productiontype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Types of production for which evidence was found.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_interpretation_subsistencetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Types of livelihood for which evidence was found.', max_length=100, null=True, blank=True)),
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
        migrations.CreateModel(
            name='DC_province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the province', max_length=100, null=True, blank=True)),
                ('original_name', models.CharField(help_text='The original or local name of the province', max_length=100, null=True, blank=True)),
                ('authorityfile_id', models.CharField(help_text='Identifier provided by some authority file', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_reference_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the region', max_length=100, null=True, blank=True)),
                ('original_name', models.CharField(help_text='The original or local name of the region', max_length=100, null=True, blank=True)),
                ('authorityfile_id', models.CharField(help_text='Identifier provided by some authority file', max_length=100, null=True, blank=True)),
                ('country', models.ForeignKey(blank=True, to='newModel.DC_country', help_text='The name of the country', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_researchevent_institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Organisation that carried out a research project at the site.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_researchevent_researchtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Methods used for researching the site.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_researchevent_special_analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Analyses other than excavation that were carried out to research the site.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DC_site_geographicalreferencesystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of system uniquely determining the position of the site.', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Finds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confidence', models.CharField(blank=True, max_length=50, null=True, help_text='Confidence in finds', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('comment', models.TextField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True)),
                ('amount', models.ForeignKey(blank=True, to='newModel.DC_finds_amount', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('animal_remains_completeness', models.ForeignKey(blank=True, to='newModel.DC_finds_animal_remains_completeness', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('animal_remains_part', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_animal_remains_part', blank=True)),
                ('animal_remains_species', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_animal_remains_species', blank=True)),
                ('area', models.ForeignKey(blank=True, to='newModel.Area', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('botany_species', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_botany_species', blank=True)),
                ('finds_type', models.ForeignKey(blank=True, to='newModel.DC_finds_type', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('lithics_cores', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_core', blank=True)),
                ('lithics_debitage', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_debitage', blank=True)),
                ('lithics_modified_tools', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_modified_tools', blank=True)),
                ('lithics_technology', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_lithics_technology', blank=True)),
                ('material', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_material', blank=True)),
                ('pottery_decoration', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_decoration', blank=True)),
                ('pottery_detail', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_detail', blank=True)),
                ('pottery_form', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_pottery_form', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text='Free text summary account on subsistence & production of the site.', null=True, blank=True)),
                ('comment', models.TextField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True)),
                ('finds', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Finds', blank=True)),
                ('production_type', models.ManyToManyField(help_text='Types of production for which evidence was found.', to='newModel.DC_interpretation_productiontype', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c14_calibrated', models.CharField(blank=True, max_length=100, null=True, help_text='Date is a calibrated date.', choices=[('yes', 'yes'), ('no', 'no')])),
                ('comment', models.TextField(help_text='Additional information on the chronology not covered in any other field.', max_length=500, null=True, blank=True)),
                ('dated_by', models.ManyToManyField(help_text='Source providing information about date.', to='newModel.DC_period_datedby', max_length=100, blank=True)),
                ('dating_method', models.ManyToManyField(help_text='HELPTEXT', to='newModel.DC_period_datingmethod', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='The title of the ressource.', max_length=100, null=True, blank=True)),
                ('creator', models.CharField(help_text='The person who is main responsible for creating the resource', max_length=100, null=True, blank=True)),
                ('creation_time', newModel.customTypes.CustomIntegerField(help_text='The date of the creation date of the ressource.', null=True, blank=True)),
                ('url', models.URLField(help_text='The URL to the ressource', max_length=100, null=True, blank=True)),
                ('reference_type', models.ForeignKey(blank=True, to='newModel.DC_reference_type', help_text='The type of the resource.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_of_activity_start_year', newModel.customTypes.CustomIntegerField(help_text='Year when research started.', null=True, blank=True)),
                ('year_of_activity_end_year', newModel.customTypes.CustomIntegerField(help_text='Year when research ended.', null=True, blank=True)),
                ('project_name', models.CharField(help_text='Name of project.', max_length=100, null=True, blank=True)),
                ('project_id', models.CharField(help_text='Project unique identifier.', max_length=100, null=True, blank=True)),
                ('project_leader', models.CharField(help_text='Leader of the research project.', max_length=100, null=True, blank=True)),
                ('comment', models.TextField(help_text='Additional information on the research history not covered in any other field.', null=True, blank=True)),
                ('institution', models.ManyToManyField(help_text='Organisation that carried out a research project at the site.', to='newModel.DC_researchevent_institution', blank=True)),
                ('reference', models.ManyToManyField(help_text='Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.', to='newModel.Reference', blank=True)),
                ('research_type', models.ManyToManyField(help_text='Methods used for researching the site.', to='newModel.DC_researchevent_researchtype', blank=True)),
                ('special_analysis', models.ManyToManyField(help_text='Analyses other than excavation that were carried out to research the site.', to='newModel.DC_researchevent_special_analysis', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.', max_length=350, null=True, blank=True)),
                ('alias_name', models.CharField(help_text='Alias name of the site.', max_length=350, null=True, blank=True)),
                ('alternative_name', models.CharField(help_text='Alternative name of the site.', max_length=350, null=True, blank=True)),
                ('description', models.TextField(help_text='Free text summary account on the site.', null=True, blank=True)),
                ('topography', models.CharField(help_text='Description of surface shape and features.', max_length=400, null=True, blank=True)),
                ('gps_data_n', models.CharField(help_text='North value of coordinate.', max_length=50, null=True, blank=True)),
                ('gps_data_e', models.CharField(help_text='East value of coordinate.', max_length=50, null=True, blank=True)),
                ('gps_data_z', models.CharField(help_text='Z value of coordinate (elevation).', max_length=50, null=True, blank=True)),
                ('coordinate_source', models.CharField(help_text='Source providing information about the global position of site.', max_length=100, null=True, blank=True)),
                ('number_of_activity_periods', models.CharField(help_text='Number of times past activity was recorded at the site.', max_length=100, null=True, blank=True)),
                ('geographical_coordinate_reference_system', models.ForeignKey(blank=True, to='newModel.DC_site_geographicalreferencesystem', help_text='Name of system uniquely determining the position of the site.', null=True)),
                ('province', models.ForeignKey(blank=True, to='newModel.DC_province', help_text='Geographical area where the site is located.', null=True)),
                ('reference_site', models.ManyToManyField(help_text='Bibliographic and web-based references to publications and other relevant information on the site.', to='newModel.Reference', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='reference',
            field=models.ManyToManyField(help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='system',
            field=models.ForeignKey(blank=True, to='newModel.DC_chronological_system', help_text='Name of the chronological system.', null=True),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='reference',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='subsistence_type',
            field=models.ManyToManyField(help_text='Types of livelihood for which evidence was found.', to='newModel.DC_interpretation_subsistencetype', blank=True),
        ),
        migrations.AddField(
            model_name='finds',
            name='reference',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='finds',
            name='research_event',
            field=models.ForeignKey(blank=True, to='newModel.ResearchEvent', help_text='PLEASE PROVIDE SOME HELPTEX', null=True),
        ),
        migrations.AddField(
            model_name='finds',
            name='small_finds_category',
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_small_finds_category', help_text='either a tool, jewellery or figurines', null=True),
        ),
        migrations.AddField(
            model_name='finds',
            name='small_finds_type',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.DC_finds_small_finds_type', blank=True),
        ),
        migrations.AddField(
            model_name='dc_province',
            name='region',
            field=models.ForeignKey(blank=True, to='newModel.DC_region', help_text='The name of the country', null=True),
        ),
        migrations.AddField(
            model_name='dc_chronological_system',
            name='region',
            field=models.ForeignKey(blank=True, to='newModel.DC_region', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='area_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_areatype', help_text='The type of the area.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_evidence_of_graves_human_remains',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_evidenceofgraveshumanremains', help_text='Presence of graves and/or human remains.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_evidence_of_occupation',
            field=models.ManyToManyField(help_text='Type of evidence indicating occupation found.', to='newModel.DC_area_evidenceofoccupation', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_caverockshelterstype', help_text='Type of cave/rockshelter.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_or_graves_mortuary_features',
            field=models.ManyToManyField(help_text='Parts of the cemetery other than graves.', to='newModel.DC_area_mortuaryfeatures', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_or_graves_topography',
            field=models.ManyToManyField(help_text='Connection of the cemetery/graves with other archaeological /natural or modified landscape features.', to='newModel.DC_area_topography', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_age_groups',
            field=models.ManyToManyField(help_text='Age.', to='newModel.DC_area_agegroups', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_manipulations_of_graves',
            field=models.ManyToManyField(help_text='If and how the space with the graves is marked.', to='newModel.DC_area_manipulationofgraves', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_sexes',
            field=models.ManyToManyField(help_text='Sex.', to='newModel.DC_area_sexes', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_type',
            field=models.ManyToManyField(help_text='Types of graves.', to='newModel.DC_area_gravetype', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_type_of_human_remains',
            field=models.ManyToManyField(help_text='How the humans were treated after death and buried.', to='newModel.DC_area_typeofhumanremains', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='period',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Period', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_exploitation_type',
            field=models.ManyToManyField(help_text='Type of extraction.', to='newModel.DC_area_exploitationtype', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_raw_material',
            field=models.ManyToManyField(help_text='Resource that was extracted.', to='newModel.DC_area_rawmaterial', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='reference',
            field=models.ManyToManyField(help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_building_technique',
            field=models.ManyToManyField(help_text='Method used for fabricating the buildings.', to='newModel.DC_area_buildingtechnique', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_construction_type',
            field=models.ManyToManyField(help_text='Type of buildings.', to='newModel.DC_area_constructiontype', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_special_features',
            field=models.ManyToManyField(help_text='Parts of the settlement other than buildings.', to='newModel.DC_area_specialfeatures', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_structure',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE HELPTEXT', to='newModel.DC_area_settlementstructure', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_type',
            field=models.ManyToManyField(help_text='Classification of settlement.', to='newModel.DC_area_settlementtype', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='site',
            field=models.ForeignKey(blank=True, to='newModel.Site', help_text='The site where this area is located.', null=True),
        ),
    ]
