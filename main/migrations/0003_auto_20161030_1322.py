# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-30 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161030_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblrestaurant',
            name='rtcuisine',
            field=models.TextField(db_column='rtCuisine', null=True),
        ),
        migrations.AlterField(
            model_name='tblrestaurant',
            name='rtrating',
            field=models.TextField(db_column='rtRating', null=True),
        ),
    ]
