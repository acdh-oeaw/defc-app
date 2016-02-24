# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0026_auto_20160208_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc_finds_pottery_decoration',
            name='german_name',
            field=models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='dc_finds_pottery_detail',
            name='german_name',
            field=models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='dc_finds_pottery_form',
            name='german_name',
            field=models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='dc_finds_small_finds_type',
            name='german_name',
            field=models.CharField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True, max_length=100),
        ),
    ]
