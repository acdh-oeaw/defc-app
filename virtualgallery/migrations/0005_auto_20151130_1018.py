# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0007_auto_20151120_0807'),
        ('virtualgallery', '0004_auto_20151119_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualobject',
            name='catalogue_ID',
            field=models.CharField(help_text="Value from 'CatalogueID' from 'Pottery_Schachermeyr_bearb'.", max_length=25, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualobject',
            name='site',
            field=models.ForeignKey(help_text='Site the Objectes is related with', to='defcdb.Site', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='virtualobject',
            name='upload_file',
            field=models.FileField(upload_to='documents/virtualgallery', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='virtualobject',
            name='upload_preview',
            field=models.FileField(upload_to='documents/virtualgallery', blank=True, null=True),
        ),
    ]
