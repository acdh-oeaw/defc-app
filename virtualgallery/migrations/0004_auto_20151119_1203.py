# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualgallery', '0003_auto_20151119_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualobject',
            name='upload_preview',
            field=models.FileField(upload_to='documents/virtualgallery', null=True),
        ),
        migrations.AlterField(
            model_name='virtualobject',
            name='upload_file',
            field=models.FileField(upload_to='documents/virtualgallery', null=True),
        ),
    ]
