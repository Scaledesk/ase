# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-27 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_project_aboutproductcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]