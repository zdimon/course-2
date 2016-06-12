# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
