# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20170831_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.CharField(choices=[('PRIVATE', 'only me'), ('PUBLIC', 'everyone')], max_length=7),
        ),
    ]
