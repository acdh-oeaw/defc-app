# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0024_auto_20160201_1022"),
    ]

    operations = [
        migrations.AddField(
            model_name="dc_area_agegroups",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_areatype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_buildingtechnique",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_caverockshelterstype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_constructiontype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_evidenceofgraveshumanremains",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_evidenceofoccupation",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_exploitationtype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_gravetype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_manipulationofgraves",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_mortuaryfeatures",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_rawmaterial",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_settlementstructure",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_settlementtype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_sexes",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_specialfeatures",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_topography",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_area_typeofhumanremains",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_chronological_system",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_country",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_amount",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_animal_remains_completeness",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_animal_remains_part",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_animal_remains_species",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_botany_species",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_lithics_core_shape",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_lithics_industry",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_lithics_raw_material",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_lithics_retouched_tools",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_lithics_technology",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_material",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_decoration",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_detail",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_form",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_small_finds_category",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_small_finds_type",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_finds_type",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_interpretation_productiontype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_interpretation_subsistencetype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_period_datedby",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_period_datingmethod",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_province",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_reference_type",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_region",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_researchevent_institution",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_researchevent_researchtype",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_researchevent_special_analysis",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_site_coordinatesource",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_site_geographicalreferencesystem",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
        migrations.AddField(
            model_name="dc_site_topography",
            name="description",
            field=models.TextField(blank=True, help_text="Short description."),
        ),
    ]
