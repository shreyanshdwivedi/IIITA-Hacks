# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-28 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.FileField(default='images/%Y/%m/%d/', upload_to='images/%Y/%m/%d/'),
        ),
    ]