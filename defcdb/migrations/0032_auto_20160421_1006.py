# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0031_auto_20160413_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={},
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=255, help_text='Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.'),
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set([('name', 'province')]),
        ),
    ]
