# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170124_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userdipp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.UserDipp'),
        ),
    ]
