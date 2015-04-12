# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20150329_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 3, 29, 13, 10, 18, 548500, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
