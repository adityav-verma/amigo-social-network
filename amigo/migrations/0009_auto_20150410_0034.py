# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amigo', '0008_auto_20150409_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='user',
        ),
        migrations.AddField(
            model_name='friends',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='friends',
            name='user1',
            field=models.ForeignKey(related_name='user1', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='friends',
            name='user2',
            field=models.ForeignKey(related_name='user2', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
