# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-27 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0002_auto_20170826_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]