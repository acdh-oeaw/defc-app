# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('start_date', models.CharField(max_length=200, blank=True, null=True)),
                ('end_date', models.CharField(max_length=200, blank=True, null=True)),
                ('name', models.CharField(max_length=500, blank=True, null=True)),
                ('place', models.CharField(max_length=200, blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('comment', models.TextField(max_length=500, blank=True, null=True)),
            ],
        ),
    ]
