# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-19 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='goods_type',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='goodsspecification',
            name='goods',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='GoodsSpecification',
        ),
        migrations.DeleteModel(
            name='GoodsType',
        ),
    ]
