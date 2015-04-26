# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 10, 33, 28, 33811, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 10, 33, 36, 355638, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
