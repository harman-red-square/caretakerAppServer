# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20151021_0138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='settings',
            new_name='setting',
        ),
    ]
