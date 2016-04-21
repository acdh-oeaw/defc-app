# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threedmodels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='threedmodel',
            name='model_file',
            field=models.FileField(blank=True, null=True, upload_to='static/threedmodels'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='model_metadata',
            field=models.FileField(blank=True, null=True, upload_to='static/threedmodels'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='model_thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='static/threedmodels'),
        ),
    ]
