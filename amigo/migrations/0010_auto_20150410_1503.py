# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigo', '0009_auto_20150410_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='kudos',
            new_name='disLike',
        ),
        migrations.AddField(
            model_name='status',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
