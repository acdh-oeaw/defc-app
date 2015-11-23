# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bib', '0003_auto_20151113_1104'),
        ('defcdb', '0005_auto_20151110_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='reference',
            field=models.ManyToManyField(to='bib.Book', blank=True, help_text='Bibliographic and web-based references to publications and other relevant information on the site.'),
        ),
    ]
