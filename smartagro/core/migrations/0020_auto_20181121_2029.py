# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-21 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20181121_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentationfertilizerrelation',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plantprotectant',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PlantProtectantCategory'),
        ),
        migrations.AlterField(
            model_name='plantprotectantrelation',
            name='plant_protectant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PlantProtectant'),
        ),
    ]
