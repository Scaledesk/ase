# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_project_projectname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.AddField(
            model_name='project',
            name='userdipp',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to='core.UserDipp'),
            preserve_default=False,
        ),
    ]
