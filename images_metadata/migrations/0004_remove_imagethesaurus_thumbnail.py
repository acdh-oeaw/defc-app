# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_metadata', '0003_imagethesaurus_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagethesaurus',
            name='thumbnail',
        ),
    ]
