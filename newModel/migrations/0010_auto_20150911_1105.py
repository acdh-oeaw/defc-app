# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0009_area_cemetery_or_grave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_age_groups',
            new_name='cemetery_or_graves_age_groups',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_estimated_number_of_individuals',
            new_name='cemetery_or_graves_estimated_number_of_individuals',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_grave_type',
            new_name='cemetery_or_graves_grave_type',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_manipulations_of_graves',
            new_name='cemetery_or_graves_manipulations_of_graves',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_mortuary_features',
            new_name='cemetery_or_graves_mortuary_features',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_number_of_graves',
            new_name='cemetery_or_graves_number_of_graves',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_sexes',
            new_name='cemetery_or_graves_sexes',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_sexes_number',
            new_name='cemetery_or_graves_sexes_number',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_topography',
            new_name='cemetery_or_graves_topography',
        ),
        migrations.RenameField(
            model_name='area',
            old_name='cemetery_graves_type_of_human_remains',
            new_name='cemetery_or_graves_type_of_human_remains',
        ),
    ]
