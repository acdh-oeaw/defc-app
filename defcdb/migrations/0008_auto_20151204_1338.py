# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("defcdb", "0007_auto_20151120_0807"),
    ]

    operations = [
        migrations.CreateModel(
            name="Name",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        verbose_name="ID",
                        auto_created=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_with_session_key",
                    audit_log.models.fields.CreatingSessionKeyField(
                        editable=False, null=True, max_length=40
                    ),
                ),
                (
                    "modified_with_session_key",
                    audit_log.models.fields.LastSessionKeyField(
                        editable=False, null=True, max_length=40
                    ),
                ),
                ("created", models.DateTimeField(null=True, auto_now_add=True)),
                ("modified", models.DateTimeField(null=True, auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="The entities name",
                        null=True,
                        max_length=100,
                        blank=True,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        help_text="The 'name´s' language. Controlled vocab will be provided.",
                        null=True,
                        max_length=100,
                        blank=True,
                    ),
                ),
                (
                    "created_by",
                    audit_log.models.fields.CreatingUserField(
                        related_name="created_defcdb_name_set",
                        to=settings.AUTH_USER_MODEL,
                        editable=False,
                        null=True,
                        verbose_name="created by",
                    ),
                ),
                (
                    "modified_by",
                    audit_log.models.fields.LastUserField(
                        related_name="modified_defcdb_name_set",
                        to=settings.AUTH_USER_MODEL,
                        editable=False,
                        null=True,
                        verbose_name="modified by",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("name",),
            },
        ),
        migrations.AlterField(
            model_name="site",
            name="alias_name",
            field=models.ForeignKey(
                related_name="aliasName",
                to="defcdb.Name",
                blank=True,
                help_text="Other name of the site.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="alternative_name",
            field=models.ForeignKey(
                related_name="alternativeName",
                to="defcdb.Name",
                blank=True,
                help_text="Different spelling of the name of the site.",
                null=True,
            ),
        ),
    ]
