# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_metadata', '0004_remove_imagethesaurus_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagethesaurus',
            name='image',
            field=models.FileField(upload_to='images', null=True, blank=True),
        ),
    ]
