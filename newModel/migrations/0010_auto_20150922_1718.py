# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0009_auto_20150922_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='c14_absolute_from',
            field=models.IntegerField(help_text='Year when archaeological period started.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='c14_absolute_to',
            field=models.IntegerField(help_text='Year when archaeological period ended.', null=True, blank=True),
        ),
    ]
