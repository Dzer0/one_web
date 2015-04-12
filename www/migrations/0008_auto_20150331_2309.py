# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_auto_20150331_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 9, 13, 607041)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 9, 13, 610461)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='members',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 9, 13, 604734)),
            preserve_default=True,
        ),
    ]
