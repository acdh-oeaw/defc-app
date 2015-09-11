# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0002_dc_reference_type_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dc_reference_type',
            name='test',
        ),
    ]
