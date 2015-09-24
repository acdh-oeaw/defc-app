# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0010_auto_20150922_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_area_specialfeatures',
            name='testfield',
            field=models.CharField(help_text='Parts of the settlement other than buildings.', max_length=100, null=True, blank=True),
        ),
    ]
