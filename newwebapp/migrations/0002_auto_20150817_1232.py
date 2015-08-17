# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newwebapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='absolute_date_from',
            field=models.CharField(help_text=b'Year when archaeological period started.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='absolute_date_to',
            field=models.CharField(help_text=b'Year when archaeological period ended.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='period',
            name='dated_by',
            field=models.CharField(blank=True, max_length=100, null=True, help_text=b'Source providing information about date.', choices=[(b'charcoal', b'charcoal'), (b'bone', b'bone'), (b'grain', b'grain'), (b'Samen', b'Samen')]),
        ),
        migrations.AddField(
            model_name='period',
            name='dating_method',
            field=models.CharField(blank=True, max_length=100, null=True, help_text=b'Method used for dating the site.', choices=[(b'radiocarbon dating', b'radiocarbon dating'), (b'dendrochronology', b'dendrochronology'), (b'material culture', b'material culture'), (b'none recorded', b'none recorded')]),
        ),
        migrations.AddField(
            model_name='period',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, help_text=b'Name of archaeological period for which evidence was found.', choices=[(b'Pre-Pottery Neolithic', b'Pre-Pottery Neolithic'), (b'Pre-Pottery Neolithic/Neolithic', b'Pre-Pottery Neolithic/Neolithic'), (b'Neolithic', b'Early Chalcolithic'), (b'more to come', b'more to come')]),
        ),
        migrations.AlterField(
            model_name='period',
            name='chronological_system',
            field=models.CharField(blank=True, max_length=100, null=True, help_text=b'Name of chronological reference system used for data entry.', choices=[(b'Anatolia', b'Anatolia'), (b'Crete:Evans/Vagnetti', b'Crete:Evans/Vagnetti'), (b'Crete:Tomkins 2007a', b'Crete:Tomkins 2007a'), (b'more to come', b'more to come')]),
        ),
    ]
