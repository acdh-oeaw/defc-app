# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0006_auto_20150911_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpretation',
            name='description',
            field=models.TextField(help_text='Free text summary account on subsistence & production of the site.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.TextField(help_text='Free text summary account on the site.', null=True, blank=True),
        ),
    ]
