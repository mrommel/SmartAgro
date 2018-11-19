# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-19 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181118_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantprotectantCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('valid_cultures', models.ManyToManyField(blank=True, null=True, to='core.Culture')),
            ],
        ),
        migrations.AddField(
            model_name='plantprotectant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PlantprotectantCategory'),
        ),
    ]
