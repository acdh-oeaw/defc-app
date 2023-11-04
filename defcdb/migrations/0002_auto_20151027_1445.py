# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("defcdb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "area_nr",
                    models.CharField(
                        max_length=45,
                        help_text="An established identifier for this area",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "stratigraphical_unit_id",
                    models.CharField(
                        max_length=100,
                        help_text="The identifier of the area´s stratigraphical unit",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "geographical_reference",
                    models.CharField(
                        max_length=100,
                        help_text="Locates the Area in the Site",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "c14_calibrated",
                    models.CharField(
                        max_length=100,
                        choices=[("yes", "yes"), ("no", "no")],
                        help_text="Date is a calibrated date.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "c14_absolute_from",
                    models.IntegerField(
                        help_text="Year when archaeological period started.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "c14_absolute_to",
                    models.IntegerField(
                        help_text="Year when archaeological period ended.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "period_comment",
                    models.TextField(
                        help_text="Additional information on the period not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "settlement_human_remains",
                    models.CharField(
                        max_length=3,
                        choices=[("yes", "yes"), ("no", "no")],
                        help_text="Any human remains found in this Settlement?",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "cemetery_or_grave",
                    models.CharField(
                        max_length=100,
                        choices=[("cemetery", "cemetery"), ("grave", "grave")],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "grave_number_of_graves",
                    models.CharField(
                        max_length=100,
                        verbose_name="Grave: number of graves",
                        help_text="Number of graves.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "grave_estimated_number_of_individuals",
                    models.CharField(
                        max_length=100,
                        verbose_name="Grave: estimated number of individuals",
                        help_text="minimum and or maximum",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "grave_number_of_female_sex",
                    models.IntegerField(
                        verbose_name="Grave: number of female sex",
                        help_text="Helptext",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "grave_number_of_male_sex",
                    models.IntegerField(
                        verbose_name="Grave: number of male sex",
                        help_text="Helptext",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "grave_number_of_not_specified_sex",
                    models.IntegerField(
                        verbose_name="Grave: number of not specified sex",
                        help_text="Helptext",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional information not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "area_type",
                    models.ForeignKey(
                        help_text="The type of the area.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_area_areatype",
                    ),
                ),
                (
                    "cave_rockshelters_evidence_of_graves_human_remains",
                    models.ForeignKey(
                        verbose_name="Cave/rockshelters: evidence of graves/human remains",
                        help_text="Presence of graves and/or human remains.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_area_evidenceofgraveshumanremains",
                    ),
                ),
                (
                    "cave_rockshelters_evidence_of_occupation",
                    models.ManyToManyField(
                        to="defcdb.DC_area_evidenceofoccupation",
                        verbose_name="Cave/rockshelters: evidence of occupation",
                        help_text="Type of evidence indicating occupation found.",
                        blank=True,
                    ),
                ),
                (
                    "cave_rockshelters_type",
                    models.ForeignKey(
                        verbose_name="Cave/rockshelters type",
                        help_text="Type of cave/rockshelter.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_area_caverockshelterstype",
                    ),
                ),
                (
                    "cemetery_or_graves_mortuary_features",
                    models.ManyToManyField(
                        to="defcdb.DC_area_mortuaryfeatures",
                        help_text="Parts of the cemetery other than graves.",
                        blank=True,
                    ),
                ),
                (
                    "cemetery_or_graves_topography",
                    models.ManyToManyField(
                        to="defcdb.DC_area_topography",
                        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.",
                        blank=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_area_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "grave_age_groups",
                    models.ManyToManyField(
                        to="defcdb.DC_area_agegroups",
                        verbose_name="Grave: age groups",
                        help_text="Age.",
                        blank=True,
                    ),
                ),
                (
                    "grave_manipulations_of_graves",
                    models.ManyToManyField(
                        to="defcdb.DC_area_manipulationofgraves",
                        verbose_name="Grave: manipulations of graves",
                        help_text="If and how the space with the graves is marked.",
                        blank=True,
                    ),
                ),
                (
                    "grave_sexes",
                    models.ManyToManyField(
                        to="defcdb.DC_area_sexes",
                        verbose_name="Grave: sexes",
                        help_text="Sex.",
                        blank=True,
                    ),
                ),
                (
                    "grave_type",
                    models.ManyToManyField(
                        to="defcdb.DC_area_gravetype",
                        help_text="Types of graves.",
                        blank=True,
                    ),
                ),
                (
                    "grave_type_of_human_remains",
                    models.ManyToManyField(
                        to="defcdb.DC_area_typeofhumanremains",
                        verbose_name="Grave: type of human remains",
                        help_text="How the humans were treated after death and buried.",
                        blank=True,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_area_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("site",),
            },
        ),
        migrations.CreateModel(
            name="DC_chronological_system",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "cs_name",
                    models.CharField(
                        max_length=100,
                        help_text="Name of the chronological system.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "period_name",
                    models.CharField(
                        max_length=100,
                        help_text="Name of archaeological period for which evidence was found.",
                        blank=True,
                        null=True,
                    ),
                ),
                ("start_date1_BC", models.IntegerField(blank=True, null=True)),
                ("start_date2_BC", models.IntegerField(blank=True, null=True)),
                ("end_date1_BC", models.IntegerField(blank=True, null=True)),
                ("end_date2_BC", models.IntegerField(blank=True, null=True)),
                (
                    "region",
                    models.ForeignKey(blank=True, null=True, to="defcdb.DC_region"),
                ),
            ],
            options={
                "ordering": ("cs_name",),
            },
        ),
        migrations.CreateModel(
            name="Finds",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "confidence",
                    models.CharField(
                        max_length=50,
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        help_text="Confidence in finds",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional information not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "amount",
                    models.ForeignKey(
                        help_text="Amount of finds.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_finds_amount",
                    ),
                ),
                (
                    "animal_remains_completeness",
                    models.ForeignKey(
                        help_text="Condition of the zoological sample / find (complete or part).",
                        blank=True,
                        null=True,
                        to="defcdb.DC_finds_animal_remains_completeness",
                    ),
                ),
                (
                    "animal_remains_part",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_animal_remains_part",
                        help_text="Part of the species the sample / find belongs to.",
                        blank=True,
                    ),
                ),
                (
                    "animal_remains_species",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_animal_remains_species",
                        help_text="Species the zoological sample / find belongs to.",
                        blank=True,
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                        to="defcdb.Area",
                    ),
                ),
                (
                    "botany_species",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_botany_species",
                        help_text="Species the botanical sample / find belongs to.",
                        blank=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_finds_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "finds_type",
                    models.ForeignKey(
                        help_text="Type of the finds.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_finds_type",
                    ),
                ),
                (
                    "lithics_cores",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_lithics_core",
                        help_text="Type of the cores.",
                        blank=True,
                    ),
                ),
                (
                    "lithics_debitage",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_lithics_debitage",
                        help_text="Which basic form used (for tools).",
                        blank=True,
                    ),
                ),
                (
                    "lithics_modified_tools",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_lithics_modified_tools",
                        help_text="Kind of tool which was made out of the debitage.",
                        blank=True,
                    ),
                ),
                (
                    "lithics_technology",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_lithics_technology",
                        help_text="Which technology was used to produce the debitage or tools.",
                        blank=True,
                    ),
                ),
                (
                    "material",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_material",
                        help_text="Material used for find.",
                        blank=True,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_finds_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pottery_decoration",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_pottery_decoration",
                        help_text="Type of decoration.",
                        blank=True,
                    ),
                ),
                (
                    "pottery_detail",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_pottery_detail",
                        help_text="Pottery type.",
                        blank=True,
                    ),
                ),
                (
                    "pottery_form",
                    models.ManyToManyField(
                        to="defcdb.DC_finds_pottery_form",
                        help_text="Form of pottery.",
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ("area",),
            },
        ),
        migrations.CreateModel(
            name="Interpretation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "description",
                    models.TextField(
                        help_text="Free text summary account on subsistence & production of the site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional information on subsistence and production not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "area",
                    models.ManyToManyField(
                        to="defcdb.Area",
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_interpretation_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "finds",
                    models.ManyToManyField(
                        to="defcdb.Finds",
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_interpretation_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "production_type",
                    models.ManyToManyField(
                        to="defcdb.DC_interpretation_productiontype",
                        help_text="Types of production for which evidence was found.",
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Period",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_period_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "dated_by",
                    models.ManyToManyField(
                        to="defcdb.DC_period_datedby",
                        max_length=100,
                        help_text="Source providing information about date.",
                        blank=True,
                    ),
                ),
                (
                    "dating_method",
                    models.ManyToManyField(
                        to="defcdb.DC_period_datingmethod",
                        help_text="Method used for dating the site.",
                        blank=True,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_period_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "system",
                    models.ForeignKey(
                        help_text="Name of the chronological system.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_chronological_system",
                    ),
                ),
            ],
            options={
                "ordering": ("system",),
            },
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        help_text="The title of the ressource.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "creator",
                    models.CharField(
                        max_length=100,
                        help_text="The person who is main responsible for creating the resource",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "creation_time",
                    models.IntegerField(
                        help_text="The date of the creation date of the ressource.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        max_length=100,
                        help_text="The URL to the ressource",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_reference_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_reference_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reference_type",
                    models.ForeignKey(
                        help_text="The type of the resource.",
                        blank=True,
                        null=True,
                        to="defcdb.DC_reference_type",
                    ),
                ),
            ],
            options={
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="ResearchEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        primary_key=True,
                        auto_created=True,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, max_length=40, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "year_of_activity_start_year",
                    models.IntegerField(
                        help_text="Year when research started.", blank=True, null=True
                    ),
                ),
                (
                    "year_of_activity_end_year",
                    models.IntegerField(
                        help_text="Year when research ended.", blank=True, null=True
                    ),
                ),
                (
                    "project_name",
                    models.CharField(
                        max_length=100,
                        help_text="Name of project.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "project_id",
                    models.CharField(
                        max_length=100,
                        help_text="Project unique identifier.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "project_leader",
                    models.CharField(
                        max_length=100,
                        help_text="Leader of the research project.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional information on the research history not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        editable=False,
                        verbose_name="created by",
                        related_name="created_defcdb_researchevent_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "institution",
                    models.ManyToManyField(
                        to="defcdb.DC_researchevent_institution",
                        help_text="Organisation that carried out a research project at the site.",
                        blank=True,
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        editable=False,
                        verbose_name="modified by",
                        related_name="modified_defcdb_researchevent_set",
                        null=True,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reference",
                    models.ManyToManyField(
                        to="defcdb.Reference",
                        help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.",
                        blank=True,
                    ),
                ),
                (
                    "research_type",
                    models.ManyToManyField(
                        to="defcdb.DC_researchevent_researchtype",
                        help_text="Methods used for researching the site.",
                        blank=True,
                    ),
                ),
                (
                    "special_analysis",
                    models.ManyToManyField(
                        to="defcdb.DC_researchevent_special_analysis",
                        help_text="Analyses other than excavation that were carried out to research the site.",
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.AddField(
            model_name="interpretation",
            name="reference",
            field=models.ManyToManyField(
                to="defcdb.Reference",
                help_text="Bibliographic and web-based reference(s)to publications and other relevant resources on industry & subsistence of the site/phase of the site.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="interpretation",
            name="subsistence_type",
            field=models.ManyToManyField(
                to="defcdb.DC_interpretation_subsistencetype",
                help_text="Types of livelihood for which evidence was found.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="finds",
            name="reference",
            field=models.ManyToManyField(
                to="defcdb.Reference",
                help_text="Relevant resources on the finds.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="finds",
            name="research_event",
            field=models.ForeignKey(
                help_text="Related research event.",
                blank=True,
                null=True,
                to="defcdb.ResearchEvent",
            ),
        ),
        migrations.AddField(
            model_name="finds",
            name="small_finds_category",
            field=models.ForeignKey(
                help_text="Either a tool, jewellery or figurines",
                blank=True,
                null=True,
                to="defcdb.DC_finds_small_finds_category",
            ),
        ),
        migrations.AddField(
            model_name="finds",
            name="small_finds_type",
            field=models.ManyToManyField(
                to="defcdb.DC_finds_small_finds_type",
                help_text="Type of small find.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="period",
            field=models.ManyToManyField(
                to="defcdb.Period", help_text="PLEASE PROVIDE SOME HELPTEX", blank=True
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="period_reference",
            field=models.ManyToManyField(
                to="defcdb.Reference",
                help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the period.",
                blank=True,
                related_name="referenceForPeriod",
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="quarry_exploitation_type",
            field=models.ManyToManyField(
                to="defcdb.DC_area_exploitationtype",
                help_text="Type of extraction.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="quarry_raw_material",
            field=models.ManyToManyField(
                to="defcdb.DC_area_rawmaterial",
                help_text="Resource that was extracted.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="reference",
            field=models.ManyToManyField(
                to="defcdb.Reference",
                help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_building_technique",
            field=models.ManyToManyField(
                to="defcdb.DC_area_buildingtechnique",
                help_text="Method used for fabricating the buildings.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_construction_type",
            field=models.ManyToManyField(
                to="defcdb.DC_area_constructiontype",
                help_text="Type of buildings.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_special_features",
            field=models.ManyToManyField(
                to="defcdb.DC_area_specialfeatures",
                help_text="Parts of the settlement other than buildings.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_structure",
            field=models.ManyToManyField(
                to="defcdb.DC_area_settlementstructure",
                help_text="Layout of settlement.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="settlement_type",
            field=models.ManyToManyField(
                to="defcdb.DC_area_settlementtype",
                help_text="Classification of settlement.",
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="area",
            name="site",
            field=models.ForeignKey(
                help_text="The site where this area is located.",
                blank=True,
                null=True,
                to="defcdb.Site",
            ),
        ),
    ]
