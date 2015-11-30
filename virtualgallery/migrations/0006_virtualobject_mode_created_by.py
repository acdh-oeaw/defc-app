# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualgallery', '0005_auto_20151130_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualobject',
            name='mode_created_by',
            field=models.CharField(null=True, max_length=250, blank=True, help_text='Name of the person who is responsible for the creation of the 3D model.'),
        ),
    ]
