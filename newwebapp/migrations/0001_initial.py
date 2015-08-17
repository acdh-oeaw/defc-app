# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chronological_system', models.CharField(blank=True, max_length=100, null=True, help_text=b'Please Provide some help_text', choices=[(b'Anatolia', b'Anatolia'), (b'Crete:Evans/Vagnetti', b'Crete:Evans/Vagnetti'), (b'Crete:Tomkins 2007a', b'Crete:Tomkins 2007a'), (b'more to come', b'more to come')])),
            ],
        ),
    ]
