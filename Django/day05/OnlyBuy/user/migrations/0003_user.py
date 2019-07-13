# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-13 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True)),
                ('upwd', models.CharField(max_length=50)),
                ('uphone', models.IntegerField()),
                ('uemail', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]