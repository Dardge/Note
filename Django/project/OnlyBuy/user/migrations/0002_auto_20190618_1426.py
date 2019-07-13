# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-18 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', '男'), ('0', '女')], default='1', max_length=10, null=True, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否禁用用户'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='手机'),
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(choices=[(0, '管理员'), (1, '买家'), (2, '卖家')], default=2, verbose_name='用户类型'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='昵称'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
