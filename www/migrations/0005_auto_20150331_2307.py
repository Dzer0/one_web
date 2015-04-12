# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150331_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 7, 53, 530750))),
                ('article_id', models.ForeignKey(to='www.Article')),
                ('com_user', models.ForeignKey(to='www.Members')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 23, 7, 53, 527528)),
            preserve_default=True,
        ),
    ]
