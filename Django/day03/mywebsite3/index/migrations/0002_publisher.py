# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-11 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
    ]
