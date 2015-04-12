# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0019_auto_20150412_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_img_thumb',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 13, 1, 133494)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='books',
            name='book_img',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 13, 1, 136766)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='members',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 13, 1, 131602)),
            preserve_default=True,
        ),
    ]
