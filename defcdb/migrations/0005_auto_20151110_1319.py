# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("defcdb", "0004_remove_reference_reference_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="area",
            name="period_reference",
            field=models.ManyToManyField(
                help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the period.",
                blank=True,
                to="bib.Book",
                related_name="referenceForPeriod",
            ),
        ),
        migrations.AlterField(
            model_name="area",
            name="reference",
            field=models.ManyToManyField(
                help_text="Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.",
                blank=True,
                to="bib.Book",
            ),
        ),
        migrations.AlterField(
            model_name="finds",
            name="reference",
            field=models.ManyToManyField(
                help_text="Relevant resources on the finds.", blank=True, to="bib.Book"
            ),
        ),
        migrations.AlterField(
            model_name="interpretation",
            name="reference",
            field=models.ManyToManyField(
                help_text="Bibliographic and web-based reference(s)to publications and other relevant resources on industry & subsistence of the site/phase of the site.",
                blank=True,
                to="bib.Book",
            ),
        ),
        migrations.AlterField(
            model_name="researchevent",
            name="reference",
            field=models.ManyToManyField(
                help_text="Bibliographic and/or web-based reference(s) to publications and other relevant resources related to the project.",
                blank=True,
                to="bib.Book",
            ),
        ),
    ]
