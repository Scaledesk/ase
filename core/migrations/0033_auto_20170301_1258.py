# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20170301_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]
