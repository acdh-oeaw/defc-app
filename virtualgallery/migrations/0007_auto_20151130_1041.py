# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualgallery', '0006_virtualobject_mode_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='virtualobject',
            old_name='mode_created_by',
            new_name='model_created_by',
        ),
    ]
