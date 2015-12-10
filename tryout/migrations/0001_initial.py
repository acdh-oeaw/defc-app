# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defcdb', '0018_auto_20151207_1422'),
        ('bib', '0003_auto_20151113_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('modified', models.DateTimeField(null=True, auto_now=True)),
                ('area_nr', models.CharField(null=True, max_length=45, verbose_name='Area ID', blank=True, help_text='An established identifier for this area')),
                ('c14_calibrated', models.CharField(null=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=100, blank=True, help_text='Date is a calibrated date.')),
                ('c14_absolute_from', models.IntegerField(null=True, blank=True, help_text='Year when archaeological period started.')),
                ('c14_absolute_to', models.IntegerField(null=True, blank=True, help_text='Year when archaeological period ended.')),
                ('period_comment', models.TextField(null=True, blank=True, help_text='Additional information on the period not covered in any other field.')),
                ('description', models.TextField(null=True, blank=True, help_text='Free text summary account on the settlement/cave&rockshelters/quarry/cemetery&graves')),
                ('comment', models.TextField(null=True, blank=True, help_text='Additional information not covered in any other field.')),
                ('dated_by', models.ManyToManyField(to='defcdb.DC_period_datedby', max_length=100, blank=True, help_text='Source providing information about date.')),
                ('dating_method', models.ManyToManyField(to='defcdb.DC_period_datingmethod', blank=True, help_text='Method used for dating the site.')),
                ('period', models.ForeignKey(to='defcdb.DC_chronological_system', related_name='areatry_period', blank=True, null=True, help_text='Period defined by the archaeologist')),
                ('period_reference', models.ManyToManyField(to='bib.Book', related_name='areatry_referenceForPeriod', blank=True, help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the period.')),
                ('reference', models.ManyToManyField(to='bib.Book', related_name='areatry_reference', blank=True, help_text='Bibliographic and web-based reference(s) to publications and other relevant resources on the settlement.')),
                ('site', models.ForeignKey(to='defcdb.Site', related_name='areatry_site', blank=True, null=True, help_text='The site where this area is located.')),
            ],
            options={
                'ordering': ('site',),
            },
        ),
    ]
