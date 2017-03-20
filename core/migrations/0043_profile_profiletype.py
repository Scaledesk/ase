# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20170303_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profileType',
            field=models.CharField(choices=[('Startup Companies', 'Startup Companies'), ('Mentors/Consultants', 'Mentors/Consultants'), ('Investors(Angels/VC Funds)', 'Investors(Angels/VC Funds)'), ('Accelerators', 'Accelerators'), ('Incubators', 'Incubators'), ('Event Manager', 'Event Manager')], default='Incubators', max_length=100),
            preserve_default=False,
        ),
    ]
