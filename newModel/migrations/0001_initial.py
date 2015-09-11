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
                ('description', models.CharField(help_text='Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves', max_length=100, null=True, blank=True)),
                ('cemetery_graves_number_of_graves', models.CharField(help_text='Number of graves.', max_length=100, null=True, blank=True)),
                ('cemetery_graves_estimated_number_of_individuals', models.CharField(help_text='minimum and or maximum', max_length=100, null=True, blank=True)),
                ('cemetery_graves_sexes_number', models.IntegerField(help_text='Helptext', null=True, blank=True)),
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
                ('comment', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
                ('amount', models.ForeignKey(blank=True, to='newModel.DC_finds_amount', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('animal_remains_completeness', models.ForeignKey(blank=True, to='newModel.DC_finds_animal_remains_completeness', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('animal_remains_part', models.ForeignKey(blank=True, to='newModel.DC_finds_animal_remains_part', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('animal_remains_species', models.ForeignKey(blank=True, to='newModel.DC_finds_animal_remains_species', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('area', models.ForeignKey(blank=True, to='newModel.Area', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('botany_species', models.ForeignKey(blank=True, to='newModel.DC_finds_botany_species', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('finds_type', models.ForeignKey(blank=True, to='newModel.DC_finds_type', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('lithics_cores', models.ForeignKey(blank=True, to='newModel.DC_finds_lithics_core', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('lithics_debitage', models.ForeignKey(blank=True, to='newModel.DC_finds_lithics_debitage', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('lithics_modified_tools', models.ForeignKey(blank=True, to='newModel.DC_finds_lithics_modified_tools', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('lithics_technology', models.ForeignKey(blank=True, to='newModel.DC_finds_lithics_technology', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('material', models.ForeignKey(blank=True, to='newModel.DC_finds_material', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('pottery_decoration', models.ForeignKey(blank=True, to='newModel.DC_finds_pottery_decoration', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('pottery_detail', models.ForeignKey(blank=True, to='newModel.DC_finds_pottery_detail', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
                ('pottery_form', models.ForeignKey(blank=True, to='newModel.DC_finds_pottery_form', help_text='PLEASE PROVIDE SOME HELPTEX', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(help_text='Free text summary account on subsistence & production of the site.', max_length=500, null=True, blank=True)),
                ('comment', models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', max_length=100, null=True, blank=True)),
                ('finds', models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Finds', blank=True)),
                ('production_type', models.ForeignKey(blank=True, to='newModel.DC_interpretation_productiontype', help_text='Types of production for which evidence was found.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chronological_system', models.CharField(help_text='Name of the chronological system.', max_length=100, null=True, blank=True)),
                ('period_name', models.CharField(help_text='Name of archaeological period for which evidence was found.', max_length=100, null=True, blank=True)),
                ('start_date1_BC', models.IntegerField(help_text='Helptext')),
                ('start_date2_BC', models.IntegerField(help_text='Helptext')),
                ('end_date1_BC', models.IntegerField(help_text='Helptext')),
                ('end_date2_BC', models.IntegerField(help_text='Helptext')),
                ('dating_method', models.CharField(help_text='Method used for dating the site.', max_length=100, null=True, blank=True)),
                ('dated_by', models.CharField(help_text='Source providing information about date.', max_length=100, null=True, blank=True)),
                ('c14_calibrated', models.CharField(help_text='Date is a calibrated date.', max_length=100, null=True, blank=True)),
                ('comment', models.CharField(help_text='Additional information on the chronology not covered in any other field.', max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of project.', max_length=100, null=True, blank=True)),
                ('project_id', models.CharField(help_text='Project unique identifier.', max_length=100, null=True, blank=True)),
                ('project_leader', models.CharField(help_text='Leader of the research project.', max_length=100, null=True, blank=True)),
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
                ('comment', models.TextField(help_text='Additional information on the research history not covered in any other field.', null=True, blank=True)),
                ('institution', models.ForeignKey(blank=True, to='newModel.DC_researchevent_institution', help_text='Organisation that carried out a research project at the site.', null=True)),
                ('project', models.ForeignKey(blank=True, to='newModel.Project', help_text='The project providing the context for the research event.', null=True)),
                ('reference', models.ManyToManyField(help_text='Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.', to='newModel.Reference', blank=True)),
                ('research_type', models.ForeignKey(blank=True, to='newModel.DC_researchevent_researchtype', help_text='Methods used for researching the site.', null=True)),
                ('special_analysis', models.ForeignKey(blank=True, to='newModel.DC_researchevent_special_analysis', help_text='Analyses other than excavation that were carried out to research the site.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.', max_length=350, null=True, blank=True)),
                ('alias_name', models.CharField(help_text='Alias name of the site.', max_length=350, null=True, blank=True)),
                ('alternative_name', models.CharField(help_text='Alternative name of the site.', max_length=350, null=True, blank=True)),
                ('description', models.CharField(help_text='Free text summary account on the site.', max_length=400, null=True, blank=True)),
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
            name='region',
            field=models.ForeignKey(to='newModel.DC_region'),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='reference',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='subsistence_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_interpretation_subsistencetype', help_text='Types of livelihood for which evidence was found.', null=True),
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
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_small_finds_type', help_text='PLEASE PROVIDE SOME HELPTEX', null=True),
        ),
        migrations.AddField(
            model_name='dc_province',
            name='region',
            field=models.ForeignKey(blank=True, to='newModel.DC_region', help_text='The name of the country', null=True),
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
            field=models.ForeignKey(blank=True, to='newModel.DC_area_evidenceofoccupation', help_text='Type of evidence indicating occupation found.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cave_rockshelters_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_caverockshelterstype', help_text='Type of cave/rockshelter.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_age_groups',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_agegroups', help_text='Age.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_grave_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_gravetype', help_text='Types of graves.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_manipulations_of_graves',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_manipulationofgraves', help_text='If and how the space with the graves is marked.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_mortuary_features',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_mortuaryfeatures', help_text='Parts of the cemetery other than graves.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_sexes',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_sexes', help_text='Sex.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_topography',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_topography', help_text='Connection of the cemetery/graves with other archaeological /natural or modified landscape features.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='cemetery_graves_type_of_human_remains',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_typeofhumanremains', help_text='How the humans were treated after death and buried.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='period',
            field=models.ForeignKey(blank=True, to='newModel.Period', help_text='PLEASE PROVIDE SOME HELPTEX', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_exploitation_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_exploitationtype', help_text='Type of extraction.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='quarry_raw_material',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_rawmaterial', help_text='Resource that was extracted.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='reference',
            field=models.ManyToManyField(help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.', to='newModel.Reference', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_building_technique',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_buildingtechnique', help_text='Method used for fabricating the buildings.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_constructiontype',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_constructiontype', help_text='Type of buildings.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_special_features',
            field=models.ManyToManyField(help_text='Parts of the settlement other than buildings.', to='newModel.DC_area_specialfeatures', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_area_settlementtype', help_text='Classification of settlement.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='site',
            field=models.ForeignKey(blank=True, to='newModel.Site', help_text='The site where this area is located.', null=True),
        ),
    ]
