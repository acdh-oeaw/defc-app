# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-start_date',)},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='url',
            new_name='webpage',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
    ]
