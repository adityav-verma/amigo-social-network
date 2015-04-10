# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amigo', '0003_auto_20150408_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='subject',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
