# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0004_auto_20150914_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_chronological_system',
            options={},
        ),
        migrations.AlterModelOptions(
            name='dc_province',
            options={},
        ),
        migrations.AlterModelOptions(
            name='dc_reference_type',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_researchevent_institution',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_researchevent_researchtype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_researchevent_special_analysis',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_site_geographicalreferencesystem',
            options={'ordering': ('name',)},
        ),
    ]
