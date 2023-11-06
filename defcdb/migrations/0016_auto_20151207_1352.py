# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0015_auto_20151207_1210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="finds",
            name="amount",
            field=models.ForeignKey(
                on_delete=models.SET_NULL,
                help_text="Number of pieces within the category.",
                to="defcdb.DC_finds_amount",
                null=True,
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="animal_remains_completeness",
            field=models.ForeignKey(
                help_text="How much was present (complete or part).",
                to="defcdb.DC_finds_animal_remains_completeness",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="animal_remains_part",
            field=models.ManyToManyField(
                help_text="Which part was present.",
                to="defcdb.DC_finds_animal_remains_part",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="animal_remains_species",
            field=models.ManyToManyField(
                help_text="How the zoological sample / find is categorised.",
                to="defcdb.DC_finds_animal_remains_species",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="area",
            field=models.ForeignKey(
                help_text="Location of the find.",
                to="defcdb.Area",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="botany_species",
            field=models.ManyToManyField(
                help_text="How the botanical sample / find is categorised.",
                to="defcdb.DC_finds_botany_species",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="confidence",
            field=models.CharField(
                help_text="How reliable the information is that was entered.",
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                blank=True,
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="finds_type",
            field=models.ForeignKey(
                help_text="Category of finds.",
                to="defcdb.DC_finds_type",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="lithics_cores",
            field=models.ManyToManyField(
                help_text="Type of the core.",
                to="defcdb.DC_finds_lithics_core",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="lithics_debitage",
            field=models.ManyToManyField(
                help_text="Basic form of the tool.",
                to="defcdb.DC_finds_lithics_debitage",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="material",
            field=models.ManyToManyField(
                help_text="What was the small find made of.",
                to="defcdb.DC_finds_material",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="pottery_decoration",
            field=models.ManyToManyField(
                help_text="What the pottery was embellished with.",
                to="defcdb.DC_finds_pottery_decoration",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="pottery_detail",
            field=models.ManyToManyField(
                help_text="Preserved part of the pottery.",
                to="defcdb.DC_finds_pottery_detail",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="pottery_form",
            field=models.ForeignKey(
                help_text="The form of the pottery.",
                to="defcdb.DC_finds_pottery_form",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="reference",
            field=models.ManyToManyField(
                help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the selected small finds.",
                to="bib.Book",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="research_event",
            field=models.ForeignKey(
                help_text="Project / Research the finds are related to.",
                to="defcdb.ResearchEvent",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="small_finds_category",
            field=models.ForeignKey(
                help_text="Superordinate class of small find.",
                to="defcdb.DC_finds_small_finds_category",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="small_finds_type",
            field=models.ManyToManyField(
                help_text="What kind of small find is described.",
                to="defcdb.DC_finds_small_finds_type",
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="interpretation",
            name="area",
            field=models.ManyToManyField(
                help_text="The interpreted area(s).", to="defcdb.Area", blank=True
            ),
        ),
        migrations.AlterField(
            model_name="interpretation",
            name="finds",
            field=models.ManyToManyField(
                help_text="The interpreted find(s).", to="defcdb.Finds", blank=True
            ),
        ),
    ]
