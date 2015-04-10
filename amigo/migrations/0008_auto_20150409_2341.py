# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigo', '0007_friends_acitve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='acitve',
            new_name='active',
        ),
    ]
