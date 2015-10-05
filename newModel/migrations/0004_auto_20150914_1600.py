# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0003_auto_20150914_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_chronological_system',
            options={'ordering': ('cs_name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_country',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_amount',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_animal_remains_completeness',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_animal_remains_part',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_animal_remains_species',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_botany_species',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_lithics_core',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_lithics_debitage',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_lithics_modified_tools',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_lithics_technology',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_material',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_pottery_decoration',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_pottery_detail',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_pottery_form',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_small_finds_category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_small_finds_type',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_finds_type',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_interpretation_productiontype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_interpretation_subsistencetype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_period_datedby',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_period_datingmethod',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_province',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_region',
            options={'ordering': ('name',)},
        ),
    ]
