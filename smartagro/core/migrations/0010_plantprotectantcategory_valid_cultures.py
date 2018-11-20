# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-19 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_plantprotectantcategory_valid_cultures'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprotectantcategory',
            name='valid_cultures',
            field=models.ManyToManyField(blank=True, null=True, to='core.Culture'),
        ),
    ]