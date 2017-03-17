# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20170303_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.AddField(
            model_name='project',
            name='userdipp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.UserDipp'),
            preserve_default=False,
        ),
    ]
