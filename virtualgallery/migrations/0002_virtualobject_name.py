# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualgallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualobject',
            name='name',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
