# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0022_auto_20160129_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dc_chronological_system',
            name='period_name',
            field=models.CharField(blank=True, null=True, help_text='Name of archaeological period for which evidence was found.', max_length=256),
        ),
    ]
