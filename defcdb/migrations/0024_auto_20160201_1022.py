# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0023_auto_20160129_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='finds',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='name',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='reference',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='researchevent',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
        migrations.AddField(
            model_name='site',
            name='public',
            field=models.BooleanField(default=False, help_text='Make this record public or not?'),
        ),
    ]
