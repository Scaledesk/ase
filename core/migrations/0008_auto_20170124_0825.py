# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170124_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='userdipp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.UserDipp'),
            preserve_default=False,
        ),
    ]
