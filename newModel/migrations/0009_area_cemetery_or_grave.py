# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0008_auto_20150911_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='cemetery_or_grave',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[('cemetery', 'cemetery'), ('grave', 'grave')]),
        ),
    ]
