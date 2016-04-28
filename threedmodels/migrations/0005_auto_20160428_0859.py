# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threedmodels', '0004_auto_20160425_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='institution',
            field=models.ManyToManyField(to='defcdb.DC_researchevent_institution', blank=True),
        ),
    ]
