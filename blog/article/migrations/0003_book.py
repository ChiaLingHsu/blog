# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20161104_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('content', models.TextField()),
                ('pubDateTime', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-pubDateTime',),
            },
        ),
    ]