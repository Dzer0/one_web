# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0021_auto_20150412_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.CharField(default=datetime.datetime(2015, 4, 12, 15, 14, 55, 672233, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 14, 38, 803202)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 14, 38, 806474)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='members',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 14, 38, 801339)),
            preserve_default=True,
        ),
    ]
