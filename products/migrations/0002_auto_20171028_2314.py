# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-28 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_status',
            field=models.BooleanField(default=False),
        ),
    ]
