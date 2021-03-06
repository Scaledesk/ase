# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userdipp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('designatePerson', models.CharField(max_length=50)),
                ('founderCofounder', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('facebook', models.CharField(max_length=256)),
                ('linkedin', models.CharField(max_length=256)),
                ('twitter', models.CharField(max_length=256)),
                ('industry', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.UserDipp')),
            ],
        ),
    ]
