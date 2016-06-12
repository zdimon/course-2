# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_musician_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=100, null=True, verbose_name='Surname', blank=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name', blank=True)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
