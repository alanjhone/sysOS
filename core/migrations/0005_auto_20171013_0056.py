# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171013_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Rua'),
        ),
    ]
