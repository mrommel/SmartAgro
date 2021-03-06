# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181110_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/machines'),
        ),
        migrations.AlterField(
            model_name='model',
            name='type',
            field=models.CharField(choices=[('T', 'Tractor'), ('I', 'Implement'), ('H', 'Harvester')], max_length=1),
        ),
    ]
