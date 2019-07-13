# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-12 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20190611_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=120, verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Questions', verbose_name='问题'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='total',
            field=models.IntegerField(default=0, verbose_name='票数'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='quest',
            field=models.CharField(db_index=True, max_length=120, unique=True, verbose_name='问题'),
        ),
        migrations.AlterModelTable(
            name='answers',
            table='answers',
        ),
        migrations.AlterModelTable(
            name='questions',
            table='questions',
        ),
    ]
