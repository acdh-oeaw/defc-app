# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0027_auto_20160224_1805'),
        ('bib', '0004_auto_20160205_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageThesaurus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('creator', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.FileField(upload_to='static/images', null=True, blank=True)),
                ('thumbnail', models.FileField(upload_to='static/thumbnails', null=True, blank=True)),
                ('page', models.CharField(max_length=100, null=True, blank=True)),
                ('literature', models.ForeignKey(null=True, to='bib.Book', blank=True)),
                ('pottery_decoration', models.ForeignKey(null=True, to='defcdb.DC_finds_pottery_decoration', blank=True)),
                ('pottery_detail', models.ForeignKey(null=True, to='defcdb.DC_finds_pottery_detail', blank=True)),
                ('pottery_form', models.ForeignKey(null=True, to='defcdb.DC_finds_pottery_form', blank=True)),
                ('region', models.ManyToManyField(null=True, to='defcdb.DC_region')),
                ('small_finds', models.ForeignKey(null=True, to='defcdb.DC_finds_small_finds_type', blank=True)),
            ],
        ),
    ]
