# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0012_auto_20151204_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='alias_name',
        ),
        migrations.AddField(
            model_name='site',
            name='alias_name',
            field=models.ManyToManyField(help_text='Other name of the site.', null=True, to='defcdb.Name', related_name='aliasName', blank=True),
        ),
        migrations.RemoveField(
            model_name='site',
            name='alternative_name',
        ),
        migrations.AddField(
            model_name='site',
            name='alternative_name',
            field=models.ManyToManyField(help_text='Different spelling of the name of the site.', null=True, to='defcdb.Name', related_name='alternativeName', blank=True),
        ),
    ]
