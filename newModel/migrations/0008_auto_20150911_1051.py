# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0007_auto_20150911_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.TextField(help_text='Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='comment',
            field=models.TextField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='interpretation',
            name='comment',
            field=models.TextField(help_text='PLEASE PROVIDE SOME HELPTEX', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='comment',
            field=models.TextField(help_text='Additional information on the chronology not covered in any other field.', max_length=500, null=True, blank=True),
        ),
    ]
