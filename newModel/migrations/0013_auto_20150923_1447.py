# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0012_interpretation_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='grave_sexes_number',
        ),
        migrations.AddField(
            model_name='area',
            name='grave_number_of_female_sex',
            field=models.IntegerField(help_text='Helptext', null=True, verbose_name='Grave: number of female sex', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_number_of_male_sex',
            field=models.IntegerField(help_text='Helptext', null=True, verbose_name='Grave: number of male sex', blank=True),
        ),
        migrations.AddField(
            model_name='area',
            name='grave_number_of_not_specified_sex',
            field=models.IntegerField(help_text='Helptext', null=True, verbose_name='Grave: number of not specified sex', blank=True),
        ),
    ]
