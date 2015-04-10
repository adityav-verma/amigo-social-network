# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigo', '0004_auto_20150408_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='pubDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
