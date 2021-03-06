# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-14 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.IntegerField()),
                ('type', models.CharField(choices=[('T', 'Tractor'), ('I', 'Implement'), ('H', 'Harvester')], max_length=1)),
                ('text', models.CharField(max_length=64)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationFieldRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Documentation')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationMachineRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Documentation')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationPersonRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Documentation')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('area', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='documentationfieldrelation',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Field'),
        ),
    ]
