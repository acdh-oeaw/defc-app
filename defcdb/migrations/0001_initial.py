# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DC_area_agegroups",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, help_text="Age.", blank=True, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_areatype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="The type of the area.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_buildingtechnique",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Method used for fabricating the buildings.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_caverockshelterstype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Type of cave/rockshelter.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_constructiontype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Type of buildings.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_evidenceofgraveshumanremains",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Presence of graves and/or human remains.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_evidenceofoccupation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Type of evidence indicating occupation found.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_exploitationtype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Type of extraction.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_gravetype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Types of graves.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_manipulationofgraves",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="If and how the space with the graves is marked.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_mortuaryfeatures",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Parts of the cemetery other than graves.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_rawmaterial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Resource that was extracted.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_settlementstructure",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Layout of settlement.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_settlementtype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Classification of settlement.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_sexes",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, help_text="Sex.", blank=True, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_specialfeatures",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Parts of the settlement other than buildings.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_topography",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Connection of the cemetery/graves with other archaeological /natural or modified landscape features.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_area_typeofhumanremains",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="How the humans were treated after death and buried.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, help_text="The name of the country", blank=True
                    ),
                ),
                (
                    "original_name",
                    models.CharField(
                        max_length=100,
                        help_text="The original or local name of the country",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "authorityfile_id",
                    models.CharField(
                        max_length=100,
                        help_text="Identifier provided by some authority file",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_amount",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_animal_remains_completeness",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_animal_remains_part",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_animal_remains_species",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "latin_name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_botany_species",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "latin_name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_lithics_core",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_lithics_debitage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_lithics_modified_tools",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_lithics_technology",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_material",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_pottery_decoration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_pottery_detail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_pottery_form",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_small_finds_category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_small_finds_type",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_finds_type",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="PLEASE PROVIDE SOME HELPTEX",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_interpretation_productiontype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Types of production for which evidence was found.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_interpretation_subsistencetype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Types of livelihood for which evidence was found.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_period_datedby",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="please provide helptext",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_period_datingmethod",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="please provide helptext",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_province",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="The name of the province",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "original_name",
                    models.CharField(
                        max_length=100,
                        help_text="The original or local name of the province",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "authorityfile_id",
                    models.CharField(
                        max_length=100,
                        help_text="Identifier provided by some authority file",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_reference_type",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                ("name", models.CharField(max_length=100, blank=True, null=True)),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="The name of the region",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "original_name",
                    models.CharField(
                        max_length=100,
                        help_text="The original or local name of the region",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "authorityfile_id",
                    models.CharField(
                        max_length=100,
                        help_text="Identifier provided by some authority file",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        to="defcdb.DC_country",
                        on_delete=models.SET_NULL,
                        help_text="The name of the country",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_researchevent_institution",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Organisation that carried out a research project at the site.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_researchevent_researchtype",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Methods used for researching the site.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_researchevent_special_analysis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Analyses other than excavation that were carried out to research the site.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="DC_site_geographicalreferencesystem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        help_text="Name of system uniquely determining the position of the site.",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                # (
                #     "created_with_session_key",
                #     audit_log.models.fields.CreatingSessionKeyField(
                #         max_length=40, editable=False, null=True
                #     ),
                # ),
                # (
                #     "modified_with_session_key",
                #     audit_log.models.fields.LastSessionKeyField(
                #         max_length=40, editable=False, null=True
                #     ),
                # ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "name",
                    models.CharField(
                        max_length=350,
                        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "alias_name",
                    models.CharField(
                        max_length=350,
                        help_text="Alias name of the site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "alternative_name",
                    models.CharField(
                        max_length=350,
                        help_text="Alternative name of the site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Free text summary account on the site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "topography",
                    models.CharField(
                        max_length=400,
                        help_text="Description of surface shape and features.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "gps_data_n",
                    models.CharField(
                        max_length=50,
                        help_text="North value of coordinate.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "gps_data_e",
                    models.CharField(
                        max_length=50,
                        help_text="East value of coordinate.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "gps_data_z",
                    models.CharField(
                        max_length=50,
                        help_text="Z value of coordinate (elevation).",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "coordinate_source",
                    models.CharField(
                        max_length=100,
                        help_text="Source providing information about the global position of site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "number_of_activity_periods",
                    models.CharField(
                        max_length=100,
                        help_text="Number of times past activity was recorded at the site.",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Additional information on the site not covered in any other field.",
                        blank=True,
                        null=True,
                    ),
                ),
                # (
                #     "created_by",
                #     audit_log.models.fields.CreatingUserField(
                #         editable=False,
                #         verbose_name="created by",
                #         to=settings.AUTH_USER_MODEL,
                #         related_name="created_defcdb_site_set",
                #         null=True,
                #     ),
                # ),
                (
                    "geographical_coordinate_reference_system",
                    models.ForeignKey(
                        to="defcdb.DC_site_geographicalreferencesystem",
                        help_text="Name of system uniquely determining the position of the site.",
                        blank=True,
                        null=True,
                        on_delete=models.SET_NULL,
                    ),
                ),
                # (
                #     "modified_by",
                #     audit_log.models.fields.LastUserField(
                #         editable=False,
                #         verbose_name="modified by",
                #         to=settings.AUTH_USER_MODEL,
                #         related_name="modified_defcdb_site_set",
                #         null=True,
                #     ),
                # ),
                (
                    "province",
                    models.ForeignKey(
                        to="defcdb.DC_province",
                        help_text="Geographical area where the site is located.",
                        blank=True,
                        null=True,
                        on_delete=models.SET_NULL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="dc_province",
            name="region",
            field=models.ForeignKey(
                to="defcdb.DC_region",
                help_text="The name of the country",
                blank=True,
                null=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_form",
            name="region",
            field=models.ForeignKey(to="defcdb.DC_region", null=True, blank=True, on_delete=models.SET_NULL,),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_detail",
            name="region",
            field=models.ForeignKey(to="defcdb.DC_region", null=True, blank=True, on_delete=models.SET_NULL,),
        ),
        migrations.AddField(
            model_name="dc_finds_pottery_decoration",
            name="region",
            field=models.ForeignKey(to="defcdb.DC_region", null=True, blank=True, on_delete=models.SET_NULL,),
        ),
    ]
