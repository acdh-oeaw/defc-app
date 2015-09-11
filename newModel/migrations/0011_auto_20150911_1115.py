# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0010_auto_20150911_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_age_groups',
            new_name='grave_age_groups',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_estimated_number_of_individuals',
            new_name='grave_estimated_number_of_individuals',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_manipulations_of_graves',
            new_name='grave_manipulations_of_graves',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_number_of_graves',
            new_name='grave_number_of_graves',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_sexes',
            new_name='grave_sexes',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_sexes_number',
            new_name='grave_sexes_number',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_grave_type',
            new_name='grave_type',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_or_graves_type_of_human_remains',
            new_name='grave_type_of_human_remains',
        ),
        migrations.AddField(
            model_name='area',
            name='settlement_human_remains',
            field=models.CharField(blank=True, max_length=3, null=True, help_text='Any human remains found in this Settlement?', choices=[('yes', 'yes'), ('no', 'no')]),
        ),
    ]
