# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualgallery', '0002_virtualobject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualobject',
            name='upload_file',
            field=models.FileField(upload_to='documents/virtualgallery'),
        ),
    ]
