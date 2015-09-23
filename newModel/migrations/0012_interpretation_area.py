# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0011_auto_20150923_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='interpretation',
            name='area',
            field=models.ManyToManyField(help_text='PLEASE PROVIDE SOME HELPTEX', to='newModel.Area', blank=True),
        ),
    ]
