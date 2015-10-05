# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0011_dc_area_specialfeatures_testfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dc_area_specialfeatures',
            name='testfield',
        ),
    ]
