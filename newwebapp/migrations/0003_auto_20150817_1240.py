# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newwebapp', '0002_auto_20150817_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='c14_absolute_from',
            field=models.CharField(help_text=b'Year when archaeological period started.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='c14_absolute_to',
            field=models.CharField(help_text=b'Year when archaeological period ended.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='c14_calibrated',
            field=models.CharField(help_text=b'Date is a calibrated date.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='comment',
            field=models.CharField(help_text=b'Additional information on the chronology not covered in any other field.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='reference',
            field=models.CharField(help_text=b'Bibliographic and web-based reference(s) to publications and other relevant resources on the chronology.', max_length=100, null=True, blank=True),
        ),
    ]
