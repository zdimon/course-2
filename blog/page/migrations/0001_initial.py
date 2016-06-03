# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', models.TextField(blank=True)),
                ('seo_content', models.TextField(verbose_name='\u041c\u0415\u0422\u0410 content')),
                ('seo_title', models.TextField(verbose_name='\u041c\u0415\u0422\u0410 title')),
                ('seo_keywords', models.TextField(verbose_name='\u041c\u0415\u0422\u0410 keywords')),
                ('slug', models.CharField(max_length=250, verbose_name='Slug', blank=True)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
