# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-11 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20190611_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='quest',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
