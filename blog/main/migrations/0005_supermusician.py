# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160516_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supermusician',
            fields=[
                ('musician_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Musician')),
                ('supername', models.CharField(max_length=100)),
            ],
            bases=('main.musician',),
        ),
    ]
