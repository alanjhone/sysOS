# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171002_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='core.Customer'),
            preserve_default=False,
        ),
    ]
