# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0002_auto_20150914_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_area_agegroups',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_buildingtechnique',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_caverockshelterstype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_constructiontype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_evidenceofgraveshumanremains',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_evidenceofoccupation',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_exploitationtype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_gravetype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_manipulationofgraves',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_mortuaryfeatures',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_rawmaterial',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_settlementstructure',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_settlementtype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_sexes',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_specialfeatures',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_topography',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='dc_area_typeofhumanremains',
            options={'ordering': ('name',)},
        ),
    ]
