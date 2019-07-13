# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-14 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.CharField(max_length=200, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uphone',
            field=models.CharField(max_length=11, unique=True, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='user',
            name='upwd',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]