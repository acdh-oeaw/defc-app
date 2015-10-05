# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dc_area_areatype',
            options={'ordering': ('name',)},
        ),
    ]
