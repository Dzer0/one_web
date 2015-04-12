# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0014_auto_20150331_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=150)),
                ('book_img', models.ImageField(upload_to=b'media/book_img')),
                ('book_img_thumb', models.FilePathField(path=b'media/book_img/thumb')),
                ('book_describe', ckeditor.fields.RichTextField(verbose_name=b'\xe4\xb9\xa6\xe7\x9a\x84\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('book_source', models.URLField()),
                ('book_support', models.CharField(max_length=20)),
                ('book_static', models.TextField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='context',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 2, 11, 818681)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 2, 11, 821958)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='members',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 2, 11, 816817)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webintroduction',
            name='About',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xe5\x85\xb3\xe4\xba\x8e\xe6\x88\x91\xe4\xbb\xac'),
            preserve_default=True,
        ),
    ]
